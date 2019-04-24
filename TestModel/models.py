from django.db import models

# Create your models here.
from django.db import models


class Box(models.Model):
    name = models.CharField(max_length=15)
    status = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

