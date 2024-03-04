from django.urls import path

from .views import *

app_name = 'user'
urlpatterns = [
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("authorization/", AuthorizationView.as_view(), name="authorization"),
    path("logout/", logout_user, name="logout_user"),
]
