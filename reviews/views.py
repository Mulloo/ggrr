from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review, Equipment
from .forms import ReviewForm


def home_page(request):
    reviews = Review.objects.all()
    return render(request, "../templates/home_page.html", {"reviews": reviews})


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
            return redirect("reviews:equipment_detail", equipment_id=equipment.id)
    else:
        form = ReviewForm()
    return render(
        request, "reviews/add_review.html", {"form": form, "equipment": equipment}
    )


@login_required
def update_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect(
                "reviews:equipment_detail", equipment_id=review.equipment.id
            )
    else:
        form = ReviewForm(instance=review)
    return render(
        request, "reviews/update_review.html", {"form": form, "review": review}
    )


@login_required
def confirm_delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == "POST":
        if request.user == review.user:
            review.delete()
            return redirect(
                "reviews:equipment_detail", equipment_id=review.equipment.id
            )
    return render(request, "reviews/delete_review.html", {"review": review})


def equipment_detail(request, equipment_id):
    equipment = get_object_or_404(Equipment, id=equipment_id)
    reviews = Review.objects.filter(equipment=equipment)
    return render(
        request,
        "reviews/equipment_detail.html",
        {"equipment": equipment, "reviews": reviews},
    )
