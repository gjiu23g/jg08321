# myproject/pages/views.py
from django.shortcuts import render

def contact_us(request):
    return render(request, 'contact_us.html')

def about_us(request):
    return render(request, 'about_us.html')

# Add more views here as needed

from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello!")


from django.shortcuts import render

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



# pages/views.py

from django.shortcuts import render

def contact_us(request):

  context = {
    'company_name': 'DriveSafe Insurance',
    'company_phone': '1-800-123-4567',
    'company_email': 'contact@drivesafe.com',
    'company_address': '123 Main St, Anytown USA'  
  }

  return render(request, 'contact_us.html', context)



# pages/views.py

from django.shortcuts import render
import requests

def dealership_list(request):

  response = requests.get("http://localhost:8000/api/dealerships/")
  dealerships = response.json()['dealerships']
  
  context = {
    'dealerships': dealerships
  }

  return render(request, 'dealership_list.html', context)


def dealership_details(request, dealer_id):
  
  response = requests.get(f"http://localhost:8000/api/reviews/?dealerId={dealer_id}")
  reviews = response.json()['reviews']

  context = {
    'dealer_id': dealer_id,
    'reviews': reviews
  }

  return render(request, 'dealership_details.html', context)