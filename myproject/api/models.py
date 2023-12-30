# api/models.py
from django.db import models

class Review(models.Model):
    dealership = models.ForeignKey('Dealership', on_delete=models.CASCADE)
    review = models.TextField()
    # Add more fields as necessary
