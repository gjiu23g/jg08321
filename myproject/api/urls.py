# api/urls.py
from django.urls import path
from .views import DealershipsView, ReviewsView

urlpatterns = [
    path('dealerships/', DealershipsView.as_view()),
    path('reviews/', ReviewsView.as_view(), name='reviews-list'),
]
