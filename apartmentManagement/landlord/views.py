import os
from django.shortcuts import get_object_or_404, render, redirect
from .models import ParentProperty, Units
from main.models import Customer
from django.contrib.auth.models import User
from django.contrib import messages
from userAccount.tokens import generate_token
from django.utils.encoding import force_bytes, force_str, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site 
from apartmentManagement import settings
from django.core.mail import EmailMessage

# Create your views here.
def apartments(request):
    properties = ParentProperty.objects.all()
    context = {'properties': properties}
    return render(request, "landlord/apartments.html", context)

def apartmentDetails(request, property_code):
   property = get_object_or_404(ParentProperty, property_code=property_code)
    # Render a template with the property details
   return render(request, 'landlord/apartment-details.html', {'property': property})


def profile(request):
    customer = None  # Initialize customer variable
    if request.user.is_authenticated:
        customer, created = Customer.objects.get_or_create(user=request.user)  

    if request.method == "POST":
        username=request.POST['username']
        fname = request.POST.get('fname')
        lname = request.POST.get('lname') 
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        gender = request.POST.get('gender')

        #password = request.POST['newPassword']
        #pass2 = request.POST['renewPassword']     

        # if User.objects.filter(username=username):
        #     messages.error(request, "Username already exist! Please try again")
        #     return redirect('register')
        
        #if password != pass2:
        #          messages.error(request, "Passwords did not match!")        
        

        user = User.objects.get(username=username)  
        if user.email != email:
                # Email has changed, update and send verification email
            user.email = email
            user.is_active = False  # Set user as inactive until email is verified
            user.save()

                #Verification email
            current_site = get_current_site(request)    
            verification_message = render_to_string('email_verification.html',{
                  'user': user,
                  'domain': current_site.domain,
                  'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                  'token':generate_token.make_token(user),
            })
            subject="Verify your email"
            from_email=settings.EMAIL_HOST_USER
            to_list=[user.email]
            message = EmailMessage(subject, verification_message, from_email, to_list)            
            message.content_subtype="html"
            message.fail_silently = False
            message.send()
        else:
                user.first_name = fname
                user.last_name = lname
                user.save()

        # Update the customer instance
        customer.first_name = fname
        customer.last_name = lname
        customer.email = email
        customer.phone_number = phonenumber
        customer.gender = gender
        customer.save()
    #else:
        # If the request method is GET and the user is authenticated, fetch the customer associated with the user
        #if request.user.is_authenticated:
            #customer = Customer.objects.get(user=request.user)  # Assuming there's a OneToOneField linking Customer to User

    return render(request, "landlord/profile.html", {'customer': customer})

def propertyManagement(request):
    if request.method =="POST":
            property_image = request.POST['property_image']
            name = request.POST['name'] 
            address = request.POST['address']       
            property_type = request.POST['property_types']
            totalunits = request.POST['totalunits'] 
            property_size = request.POST['property_size'] 
            building_age = request.POST['building_age'] 
            amenities = request.POST['amenities'] 
            utilities = request.POST['utilities'] 
            maintenance = request.POST['maintenance'] 
            parking = request.POST['parking'] 
            security = request.POST['security'] 
            rules = request.POST['rules'] 
            accessibility = request.POST['accessibility'] 
            management_company = request.POST['management_company'] 
            lease_terms = request.POST['lease_terms'] 
            description = request.POST['description'] 

            if property_image:
                  # Construct the file path using MEDIA_ROOT
                  file_path = os.path.join(settings.MEDIA_ROOT, 'property_image.jpg')

                  # Open the file using the constructed file path
                  with open(file_path, 'wb+') as destination:
                        for chunk in property_image.chunks():
                              destination.write(chunk)
        
        
            myproperty=ParentProperty(name = name, property_image=property_image, address=address, property_type=property_type, total_units=totalunits, property_size =property_size, building_age=building_age, management_company=management_company, amenities=amenities, utilities=utilities, maintenance_services=maintenance, parking=parking, security_features=security, rules_regulations=rules, accessibility=accessibility, lease_terms=lease_terms,description=description)                                
            myproperty.save()

    return render(request, "landlord/landlordApartment.html")

def unitManagement(request):
    if request.method =="POST":
            unit_image = request.POST['unit_image']
            floornumber = request.POST['floornumber'] 
            bedrooms = request.POST['bedrooms']       
            bathrooms = request.POST['bathrooms']
            unit_size = request.POST['unit_size'] 
            rent = request.POST['rent'] 
            deposit = request.POST['deposit'] 
            description = request.POST['description'] 
            availability = request.POST['availability'] 

            if unit_image:
                  # Construct the file path using MEDIA_ROOT
                  file_path = os.path.join(settings.MEDIA_ROOT, 'unit_image.jpg')

                  # Open the file using the constructed file path
                  with open(file_path, 'wb+') as destination:
                        for chunk in unit_image.chunks():
                              destination.write(chunk)


            myunit=Units(unit_image=unit_image, floor_number = floornumber, bedrooms=bedrooms, bathrooms=bathrooms, unit_size=unit_size, rent_amount=rent, security_deposit=deposit, availability=availability, description=description)                                
            myunit.save()

    return render(request, "landlord/unitDetails.html")


def activate(request, uidb64, token):
      try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user= User.objects.get(pk=uid)
      except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

      if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
      else:
           return render(request, 'activation_failed.html')
