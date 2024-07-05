from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path(
        "equipment/<int:equipment_id>/", views.equipment_detail, name="equipment_detail"
    ),
    path(
        "equipment/<int:equipment_id>/add_review/", views.add_review, name="add_review"
    ),
    path("review/<int:review_id>/edit/", views.update_review, name="edit_review"),
    path(
        "review/<int:review_id>/delete/",
        views.confirm_delete_review,
        name="delete_review",
    ),
]
