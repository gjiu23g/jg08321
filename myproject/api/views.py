# myproject/api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer

class ReviewsView(APIView):
    def get(self, request):
        dealer_id = request.query_params.get('dealerId', None)
        if dealer_id is not None:
            reviews = Review.objects.filter(dealership__id=dealer_id)
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
        return Response({'reviews': []})
