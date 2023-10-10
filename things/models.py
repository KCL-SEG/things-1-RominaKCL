from django.db import models
from django.db.models import Model

class Thing(Model):
    name=models.CharField(max_length=10, unique=True)
    description=models.CharField(max_length=20)
    quantity=models.IntegerField()
