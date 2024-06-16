from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import CustomerCreationForm, CustomerLoginForm, EquipmentForm
from .models import Equipment


# Create your views here.

def home_page(request):
    return render(request, 'reviews/home_page.html')


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


def main_page(request):
    reviews = reviews.view.object.all()
    return render(request, 'reviews/main_page.html', {'reviews':reviews})


def equipment_list(request):
    equipment = Equipment.object.all()
    return render(request, 'reviews/equipment_list.html', {'equipment':equipment})

def equipment_detail(request, id):
    equipment = get_object_or_404(Equipment, id=id)
    return render(request, 'reviews/equipment_detail.html', {'equipment': equipment})

def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm()
    return render(request, 'reviews/add_equipment.html', {'form': form})