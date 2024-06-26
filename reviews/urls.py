from django.urls import path
from . import views
from .views import home_page

urlpatterns = [
    path("", home_page, name="home_page"),
    path("main/", views.main_page, name="main_page"),
    path('equipment/<int:equipment_id>/', views.equipment_detail, name='equipment_detail'),
    path('equipment/<int:equipment_id>/add_review/', views.add_review, name='add_review'),
]