from django.db import models

# Create your models here.


# class Customer(models.Model):
#     name = models.CharField('Customer', max_length=120)
#     age = models.IntegerField()
#     email = models.EmailField(max_length=255, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     role = models.CharField(max_length=255, choices=[('admin', 'Admin'), ('user', 'User')], default='user')

#     TYPE_CHOICES = (
#         ('Customer', 'Customer'),
#         ('Manufacturer', 'Manufacturer'),
#         ('Guest', 'Guest'),
#     )
#     type = models.CharField(choices=TYPE_CHOICES)

#     def __str__(self):
#         return self.name


from django.contrib.auth.models import AbstractUser
from django.db import models


class Customer(AbstractUser):
    # Add additional roles or fields if needed
    USER_ROLES = (
        ('admin', 'Admin'),
        ('user', 'User'),
        ('guest', 'Guest'),  # Even though guests typically won't have an account
    )
    role = models.CharField(max_length=10, choices=USER_ROLES, default='user')

    def __str__(self):
        return self.username
