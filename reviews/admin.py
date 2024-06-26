from django.contrib import admin
from .models import  Review, Equipment

# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('equipment', 'user', 'created_at')
    search_fields = ('equipment', 'user')
    list_filter = ('created_at',)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'created_at')
    search_fields = ('name', 'manufacturer')
    list_filter = ('created_at',)