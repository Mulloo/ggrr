from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review, Equipment
from .forms import ReviewForm


# Create your views here.


def home_page(request):
    return render(request, "reviews/home_page.html")


def main_page(request):
    reviews = Review.objects.all()
    return render(request, "reviews/main_page.html", {"reviews": reviews})


def equipment_list(request):
    equipment = Equipment.objects.all()
    return render(request, "reviews/equipment_list.html", {"equipment": equipment})

@login_required
def add_review(request, equipment_id):
    equipment = get_object_or_404(Equipment, id=equipment_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.equipment = equipment
            review.user = request.user
            review.save()
            return redirect("reviews:equipment_detail", id=equipment_id)
    else:
        form = ReviewForm()
    return render(request, "reviews/add_review.html", {"form": form, "equipment": equipment})


def equipment_detail(request, equipment_id):
    equipment = get_object_or_404(Equipment, id=equipment_id)
    reviews = Review.objects.filter(equipment=equipment_id)
    return render(request, "reviews/equipment_detail.html", {"equipment": equipment})