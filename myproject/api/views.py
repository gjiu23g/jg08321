# myproject/api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Dealership, Review
from api.serializers import DealershipSerializer, ReviewSerializer

class DealershipsView(APIView):

    def get(self, request):

        dealerships = [
            {"id": 1, "name": "Best Deal Auto", "location": "123 Main St"},
            {"id": 2, "name": "Great Deals Auto", "location": "456 Oak Rd"},
            {"id": 3, "name": "Auto Mart", "location": "789 Elm St"},
            {"id": 4, "name": "Value Auto", "location": "321 Pine Rd"},
            {"id": 5, "name": "Discount Auto", "location": "654 Maple Ln"},
            {"id": 6, "name": "Car Lot", "location": "987 Oak Dr"},
            {"id": 7, "name": "Auto Warehouse", "location": "753 Pine St"},
            {"id": 8, "name": "Car City", "location": "159 Elm Rd"},
            {"id": 9, "name": "Auto Emporium", "location": "357 Park St"},
            {"id": 10, "name": "Affordable Autos", "location": "246 Pine Ln"},
            {"id": 11, "name": "Quality Cars", "location": "135 Oak Ave"},
            {"id": 12, "name": "Bargain Auto", "location": "426 Elm Dr"},
            {"id": 13, "name": "Budget Car Sales", "location": "327 Park Rd"},
            {"id": 14, "name": "Auto Outlet", "location": "492 Maple St"},
            {"id": 15, "name": "Car Superstore", "location": "753 Elm Ln"},
        ]
        
        return Response({"dealerships": dealerships})

class ReviewsView(APIView):
    def get(self, request):
        dealer_id = request.query_params.get('dealerId', None)
        if dealer_id is not None:
            reviews = Review.objects.filter(dealership__id=dealer_id)
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
        return Response({'reviews': []})