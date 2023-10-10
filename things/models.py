from django.db import models
from django.contrib.auth.models import AbstractUser

class Thing(AbstractUser):
    name=models.CharField(max_length=10, unique=True)
    description=models.CharField(max_length=20)
    quantity=models.IntegerField()
