from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404

# from ..accounts.forms import ReviewForm
from .models import Review, Equipment

# Create your views here.


def home_page(request):
    return render(request, "reviews/home_page.html")


def main_page(request):
    reviews = Review.objects.all()
    return render(request, "reviews/main_page.html", {"reviews": reviews})


def equipment_list(request):
    equipment = Equipment.objects.all()
    return render(request, "reviews/equipment_list.html", {"equipment": equipment})


def equipment_detail(request, id):
    equipment = get_object_or_404(Equipment, id=id)
    return render(request, "reviews/equipment_detail.html", {"equipment": equipment})


# def add_review(request):
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.author = request.user
#             review.save()
#             return redirect("main_page")
#     else:
#         form = ReviewForm()
#     return render(request, "reviews/add_review.html", {"form": form})
