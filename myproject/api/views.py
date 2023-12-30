from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class DealershipsView(APIView):
    def get(self, request):
        # Implement logic to retrieve dealerships
        return Response({"dealerships": []})
