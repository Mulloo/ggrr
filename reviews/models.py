from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Equipment(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    manufacturer = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    equipment = models.ForeignKey("Equipment", on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.equipment.name}"
