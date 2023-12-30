from django.urls import path
from . import views
from .views import hello

urlpatterns = [
    path('hello/', hello),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('about-us/', views.about_us, name='about-us'),
]
