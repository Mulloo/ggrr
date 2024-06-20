from django.urls import path
from . import views
from .views import home_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('main/', views.main_page, name='main_page'),
    path('add_review', views.add_review, name='add_review'),
    path('equipment/', views.equipment_list, name='equipment_list'),
    path('equipment/<int:id>/', views.equipment_detail, name='equipment_detail'),
]
