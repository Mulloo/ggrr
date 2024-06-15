from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Customer


class CustomerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Customer
        fields = UserCreationForm.Meta.fields + ('role',)


class CustomerLoginForm(AuthenticationForm):
    class Meta:
        model = Customer
        fields = ['username', 'password']
