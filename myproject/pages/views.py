# myproject/pages/views.py
from django.shortcuts import render
from django.http import HttpResponse
import requests

def contact_us(request):
  return render(request, 'contact_us.html')

def about_us(request):
  return render(request, 'about_us.html')

def hello(request):
  return HttpResponse("Hello!")

def about_us(request):
  context = {
    'company_name': 'DriveSafe Insurance',
    'company_history': 'DriveSafe Insurance was founded in 2005 by John Smith. We started as a small local company and have grown to serve customers nationwide.',
    'company_mission': 'Our mission is to provide affordable and reliable car insurance to all drivers.', 
    'company_values': ['Trust', 'Customer Service', 'Affordability'],
    'company_team': [
      {'name': 'John Smith', 'title': 'CEO'},
      {'name': 'Jane Doe', 'title': 'COO'},
      {'name': 'Bob Johnson', 'title': 'CFO'}
    ],
    'company_location': '123 Main St, Anytown USA'
  }

  return render(request, 'about_us.html', context)

def dealerships(request):
  response = requests.get("http://localhost:8000/api/dealerships/")
  dealerships = response.json()['dealerships']

  context = {
    'dealerships': dealerships
  }

  return render(request, 'dealerships.html', context)

def dealership_details(request, dealer_id):

  response = requests.get("http://localhost:8000/api/reviews/")
  data = response.json()

  reviews = response.json()['reviews']
  print(reviews) 

  reviews = [
    {'text': 'Great dealership, friendly staff', 'author': 'Jane'},
    {'text': 'Terrible customer service, would not recommend', 'author': 'John'},
    {'text': 'Great selection of cars and fair prices', 'author': 'Bob'},
    {'text': 'Staff were not helpful and lacked product knowledge', 'author': 'Mary'}
  ]

  context = {
    'reviews': reviews
  }

  return render(request, 'dealership_details.html', context)
