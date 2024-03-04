from django.shortcuts import render

def index(request):
    return render(request, "main/base.html")

def home(request):
    return render(request, "main/home.html")

def aboutus(request):
    return render(request, "main/aboutus.html")

def contactus(request):
    return render(request, "main/contact.html")
