from django.contrib import admin
from .models import User, Review, Equipment

# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author__username')
    list_filter = ('created_at',)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'created_at')
    search_fields = ('name', 'manufacturer')
    list_filter = ('created_at',)