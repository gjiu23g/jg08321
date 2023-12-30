from django.urls import path
from .views import DealershipsView

urlpatterns = [
    path('dealerships/', DealershipsView.as_view(), name='dealerships'),
]
