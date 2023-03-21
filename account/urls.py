from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from account.views import *

urlpatterns = [

    path('login/', login_account, name="accountLogin"),
    path('register/', register_account, name="accountRegister"),
    path('logout/', LogoutView.as_view(template_name="account/logout.html"), name="accountLogout"),
]