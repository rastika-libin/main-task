from django.db import models
from login.models import UserRole

# Create your models here.
class Submit_Details(models.Model):
    user = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateField()