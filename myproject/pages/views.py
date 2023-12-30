from django.shortcuts import render

def contact_us(request):
    return render(request, 'contact_us.html')

def about_us(request):
    return render(request, 'about_us.html')

# Add more views here as needed

def contact_us(request):
    return render(request, 'pages/contact_us.html')

from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello!")