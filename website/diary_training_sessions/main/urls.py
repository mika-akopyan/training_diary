from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('registration/', UserRegistrationView.as_view(), name='user_registration'),
    path('authentication/', UserAuthenticationView.as_view(), name='user_authentication'),
]