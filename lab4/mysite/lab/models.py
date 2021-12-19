from django.db import models

class Cat(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    img = models.CharField(max_length=30)
