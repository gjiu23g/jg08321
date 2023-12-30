# myproject/api/serializiers.py
from rest_framework import serializers
from .models import Review, Dealership

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'dealership', 'review']

class DealershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealership
        fields = ['id', 'name', 'location']