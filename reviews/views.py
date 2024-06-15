from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomerCreationForm, CustomerLoginForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomerCreationForm()
    return render(request, 'reviews/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = CustomerLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = CustomerLoginForm()
    return render(request, 'reviews/login.html', {'form': form})
