from django import forms


class Sharkform(forms.Form):
    author = forms.CharField(required=True)
    parents = forms.CharField(required=True)


class TextForm(Sharkform):
    full_text = forms.CharField(max_length=10000)


class LinkForm(Sharkform):
    url = forms.CharField(max_length=150)


class MediaForm(Sharkform):
    file = forms.FileField(required=False)



class SubmitSharkTooth(forms.Form):
    types = (
        ("T1", "Short text"),
        ("T2", "Medium text"),
        ("T3", "Long text"),
        ("IM", "Image"),
        ("VD", "Video"),
        ("LK", "Link"),

    )
    type = forms.ChoiceField(label="Type of media", choices=types)
    url = forms.CharField(label="URL", required=False)
    text = forms.CharField(label="text", max_length=10000, required=False)
    title = forms.CharField(label="title", max_length=50, required=True)
    sub_title = forms.CharField(label="sub_title", max_length=100, required=True)
    description = forms.CharField(label="description", max_length=300, required=True)


class SignUp(forms.Form):
    username = forms.CharField(label="User name", max_length=30)
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput())
    confirm_password = forms.CharField(label="Confirm Password", max_length=50, widget=forms.PasswordInput())
    e_mail = forms.CharField(label="Email", max_length=100, required=False)
    real_name = forms.CharField(label="Real Name", max_length=70)


class LogIn(forms.Form):
    username = forms.CharField(label="User name", max_length=30)
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput())
