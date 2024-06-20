from django.db import models
from django.contrib.auth.models import User
from django.conf import settings





class Review(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    manufacturer = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.name


