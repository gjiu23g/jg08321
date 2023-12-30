# myproject/api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Dealership, Review
from api.serializers import DealershipSerializer, ReviewSerializer

class DealershipsView(APIView):
    def get(self, request):
        dealership = Dealership.objects.all()
        serializer = DealershipSerializer(dealership, many=True)
        return Response(serializer.data)

class ReviewsView(APIView):
    def get(self, request):
        dealer_id = request.query_params.get('dealerId', None)
        if dealer_id is not None:
            reviews = Review.objects.filter(dealership__id=dealer_id)
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
        return Response({'reviews': []})