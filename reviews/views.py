from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import UserCreationForm, UserLoginForm, ReviewForm
from .models import Review, Equipment

# Create your views here.


def home_page(request):
    return render(request, 'reviews/home_page.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You are now registered!')
            return redirect('home_page') 
    else:
        form = UserCreationForm()
    return render(request, 'reviews/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                message = f'You are now logged in as {username}'
                return redirect('home_page')
            else:
                form.add_error(None, 'Invalid username or password')
        else:
            form = UserLoginForm()
        return render(request, 'reviews/login.html', {'form': form})
    else:
        form = UserLoginForm()
    return render(request, 'reviews/login.html', {'form': form})

def main_page(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/main_page.html', {'reviews': reviews})


def equipment_list(request):
    equipment = Equipment.objects.all()
    return render(request, 'reviews/equipment_list.html', {'equipment': equipment})


def equipment_detail(request, id):
    equipment = get_object_or_404(Equipment, id=id)
    return render(request, 'reviews/equipment_detail.html', {'equipment': equipment})


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user  
            review.save()
            return redirect('main_page')
    else:
        form = ReviewForm()
    return render(request, 'reviews/add_review.html', {'form': form})