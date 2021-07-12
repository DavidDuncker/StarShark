from django.contrib.auth import authenticate, login
from django.shortcuts import render
from . import forms
from . import models
from .models import Emoji, Text, Media, Submission, SiteUser
from random import randint
from pathlib import Path
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    context = {"Teeth": Squeal.objects.all(), "request": request}
    return render(request, 'shark/base.html', context)


def submit(request):
    #If the form has been submitted
    if request.method == "POST":
        #Encapsulate the form data
        form = forms.SubmitSharkTooth(request.POST, request.FILES)
        #Validate form data
        if form.is_valid():
            #Splice form data
            author = request.user
            reply_id = None
            tooth_type = form.cleaned_data['tooth_type']
            url = form.cleaned_data['url']
            text = form.cleaned_data['text']
            #Create new Tooth with data
            newTooth = Tooth()
            newTooth.reply_id = reply_id
            newTooth.author = author
            newTooth.url = url
            newTooth.type = tooth_type
            newTooth.text = text
            try:
                #Get the file
                file = request.FILES['file']
                #Name a directory for the file
                directory = 'shark/uploads/' + str(randint(0, 999999))
                #Make directory if not exists
                Path(directory).mkdir(parents=True, exist_ok=True)
                #Write the file in the directory
                with open(directory + "/" + file.name, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                newTooth.file_url = directory + "/" + file.name
            except KeyError:
                pass
            newTooth.save()
        else:
            print(form.errors)
        return render(request, 'shark/base.html', context={})
    else:
        context = {'form': forms.SubmitSharkTooth()}
    return render(request, 'shark/submit.html', context)


def sign_up(request):
    #If the form has been submitted
    if request.method == "POST":
        #Encapsulate the form data
        form = forms.SignUp(request.POST)
        #Validate form data
        if form.is_valid():
            #Splice form data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            e_mail = form.cleaned_data['e_mail']
            real_name = form.cleaned_data['real_name']
            #Create new User with data
            if password == confirm_password:
                user = models.SiteUser.objects.create_user(username, password, email=e_mail, name=real_name)
                user.save()
                #Log the User in
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
        else:
            return render(request, form.errors, context={})
        return render(request, 'shark/sign_up.html', context={})
    else:
    #If the form is unbound:
        context = {'form': forms.SignUp()}
    return render(request, 'shark/sign_up.html', context)


def log_in(request):
    print("User: " + str(request.user))
    #If the form has been submitted
    if request.method == "POST":
        #Encapsulate the form data
        form = forms.LogIn(request.POST)
        #Validate form data
        if form.is_valid():
            #Splice form data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #Log user in
            user = authenticate(username=username, password=password)
            print(str(user))
            if user is not None:
                print(str(login(request, user)))
        else:
            print(form.errors)
        return render(request, 'shark/log_in.html', context={})
    else:
    #If the form is unbound:
        context = {'form': forms.LogIn()}
    return render(request, 'shark/log_in.html', context)


def profile(request, id):
    user_profile = SiteUser.objects.filter(pk=id)
    context = {'profile': user_profile}
    return render(request, 'shark/profile.html', context)


def debug(request):
    context = {'request_data': request}
    return render(request, "shark/debug.html", context)


def react(request, post_id, react_type):
    user = request.user
    tooth = Tooth.objects.filter(pk=id)
    tooth.reactions[react_type] += 1
