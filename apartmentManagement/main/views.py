from django.shortcuts import render

def index(request):
    return render(request, "main/base.html")

def home(request):
    return render(request, "main/home.html")

def aboutus(request):
    return render(request, "main/aboutus.html")

def apartments(request):
    return render(request, "main/apartments.html")

def apartmentDetails(request):
    return render(request, "main/apartment-details.html")

def contactus(request):
    return render(request, "main/contact.html")