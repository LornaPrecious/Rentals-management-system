from django.urls import path
from . import views 

urlpatterns = [
    path("", views.home, name = "home"),
    path("home/", views.home, name = "home"),
    path("aboutus/", views.aboutus, name = "aboutus"),
    path("contactus/", views.contactus, name = "contact"),
    path("apartments/", views.apartments, name = "apartments"),
    path("apartment-details/", views.apartmentDetails, name = "apartment-details"),
]