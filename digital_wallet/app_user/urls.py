from django.urls import path

from app_user.views import LoginView, RegisterView
from .views_apis.api_userDetail import *


app_name = "user_app"

urlpatterns = [
    # path('register', UserRegister.as_view(), name='register'),
    # path('login', UserLogin.as_view(), name='login'),
    # path('logout', UserLogout.as_view(), name='logout'),
    # path('user', Userview.as_view(), name='user'),
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
]
