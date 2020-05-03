from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
# from django.urls import reverse


class CustomLoginView(LoginView):
    template_name = "registration/login.html"    


class RegisterView(TemplateView):
    template_name = "registration/register.html"