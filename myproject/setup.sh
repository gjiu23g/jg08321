# Navigate to the pages app directory
cd pages

# Create views.py if it doesn't exist
touch views.py
echo "from django.shortcuts import render

def contact_us(request):
    return render(request, 'contact_us.html')

def about_us(request):
    return render(request, 'about_us.html')

# Add more views here as needed
" > views.py

# Navigate to templates directory, create if doesn't exist
mkdir -p templates
cd templates

# Create HTML files
touch contact_us.html about_us.html
echo "<html>
<head><title>Contact Us</title></head>
<body><h1>Contact Us Page</h1></body>
</html>" > contact_us.html

echo "<html>
<head><title>About Us</title></head>
<body><h1>About Us Page</h1></body>
</html>" > about_us.html

# Navigate back to the root of the Django project
cd ../../..

# Navigate to the api app directory
cd api

# Create urls.py if it doesn't exist
touch urls.py
echo "from django.urls import path
from . import views

urlpatterns = [
    # Define your API URLs here
]" > urls.py

# Navigate back to the root
cd ..

# Display the contents of the created files
echo "Contents of pages/views.py:"
cat pages/views.py
echo ""

echo "Contents of pages/templates/contact_us.html:"
cat pages/templates/contact_us.html
echo ""

echo "Contents of pages/templates/about_us.html:"
cat pages/templates/about_us.html
echo ""

echo "Contents of api/urls.py:"
cat api/urls.py
echo ""
