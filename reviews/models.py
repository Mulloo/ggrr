from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Refactored Customer model inheriting from AbstractUser
class Customer(AbstractUser):
    USER_ROLES = (
        ('admin', 'Admin'),
        ('user', 'User'),
        ('guest', 'Guest'),
    )
    role = models.CharField(max_length=10, choices=USER_ROLES, default='user')

    def __str__(self):
        return self.username

# Review model with a ForeignKey to the Customer model
class Review(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

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