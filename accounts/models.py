from django.db import models
from django.shortcuts import render, redirect


# Create your models here.


def register_user(request):
    context = {}
    return render(request, 'accounts/register.html', context)


def login_user(request):
    context = {}
    return render(request, 'accounts/login.html', context)