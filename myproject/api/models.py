# api/models.py
from django.db import models

class Dealership(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    # Add more fields as necessary

class Review(models.Model):
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE)
    review = models.TextField()
