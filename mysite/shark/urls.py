from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit.html', views.submit, name="submit"),
    path('sign_up.html', views.sign_up, name="sign up"),
    path('log_in.html', views.log_in, name="log in"),
    path('profiles/<int:id>', views.profile, name="profile"),
    path('debug.html', views.debug, name="debug"),
    path("react/<int:post_id>/<str:react_type>", views.react, name="react")
]
