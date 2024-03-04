from django.urls import path

from .views import *


urlpatterns = [
    path("registration/", RegistrationView.as_view(), name="registration"),
    path(
        "authentication/", UserAuthenticationView.as_view(), name="user_authentication"
    ),
    path("logout/", logout_user, name="logout_user"),
]
