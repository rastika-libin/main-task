from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class UserRole(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('User', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='User')
