# myproject/api/serializiers.py
from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'dealership', 'review']  # Adjust fields as needed
