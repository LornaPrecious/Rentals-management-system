import os
from django.shortcuts import get_object_or_404, render, redirect
from .models import ParentProperty, Review
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
from django.db.models import Q
#from .utils import property_details
# Create your views here.
def apartments(request):
    if request.method == 'POST':
        search_term = request.POST['search_term']
        query = Q()
        for field in ParentProperty._meta.fields:
            if field.get_internal_type() in ['CharField', 'TextField', 'IntegerField']:
                query |= Q(**{f"{field.name}__contains": search_term})
        properties = ParentProperty.objects.filter(query)

    #[field.name for field in User._meta.get_fields()]
    #my_model_fields = [field.name for field in MyModel._meta.get_fields()]
    else:    
        properties = ParentProperty.objects.all()

    context = {'properties': properties}
    return render(request, "landlord/apartments.html", context)

def apartmentDetails(request, property_code):
    property_detail = ParentProperty.objects.get(property_code = property_code)
    #unit_detail = Unit.objects.get(parent_property = property_code)

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']

        myreviews = Review(parent_property=property_detail, name=name, email=email, comment=comment)
        myreviews.save()

        
    reviews = Review.objects.filter(parent_property=property_code)
        
    return render(request, 'landlord/apartment-details.html', {
        'property_detail': property_detail,
        'reviews': reviews,
    
    })

    # context = {'items': property_details(request)['items']}
    # details = property_details(request)
    # items = details['items']
    # context = {'items': items}

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
        customer.username = username
        customer.first_name = fname
        customer.last_name = lname
        customer.email = email
        customer.phone_number = phonenumber
        customer.gender = gender
        customer.save()

        messages.success(request, "Profile updated successfully")
    #else:
        # If the request method is GET and the user is authenticated, fetch the customer associated with the user
        #if request.user.is_authenticated:
            #customer = Customer.objects.get(user=request.user)  # Assuming there's a OneToOneField linking Customer to User

    return render(request, "landlord/profile.html", {'customer': customer})

def propertyManagement(request):
    if request.user.is_authenticated:
        customer, created = Customer.objects.get_or_create(user=request.user)  

    if request.method =="POST":
            property_image = request.FILES.get('property_image')
            name = request.POST['name'] 
            location = request.POST['address']  
            average_rent = request.POST['average_rent']     
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


            unit_image = request.FILES.get('unit_image')
            floornumber = request.POST['floornumber'] 
            bedrooms = request.POST['bedrooms']       
            bathrooms = request.POST['bathrooms']
            unit_size = request.POST['unit_size'] 
            rent = request.POST['rent'] 
            deposit = request.POST['deposit'] 
            description = request.POST['description'] 
            availability = request.POST['availability'] 


            if property_image:
                  # Construct the file path using MEDIA_ROOT
                  file_path = os.path.join(settings.MEDIA_ROOT, 'property_image.jpg')

                  # Open the file using the constructed file path
                  with open(file_path, 'wb+') as destination:
                        for chunk in property_image.chunks():
                              destination.write(chunk)

            if unit_image:
                  # Construct the file path using MEDIA_ROOT
                  file_path = os.path.join(settings.MEDIA_ROOT, 'unit_image.jpg')

                  # Open the file using the constructed file path
                  with open(file_path, 'wb+') as destination:
                        for chunk in unit_image.chunks():
                              destination.write(chunk)
      
            
            if customer.role == 'landlord':
                myproperty=ParentProperty(customer=customer, name = name, property_image=property_image, location=location, property_type=property_type, average_rent=average_rent,
                                              total_units=totalunits, property_size =property_size, building_age=building_age,
                                              management_company=management_company, amenities=amenities, utilities=utilities, 
                                              maintenance_services=maintenance, parking=parking, security_features=security, 
                                              rules_regulations=rules, accessibility=accessibility, lease_terms=lease_terms,description=description,
                                              unit_image=unit_image, floor_number = floornumber, bedrooms=bedrooms, bathrooms=bathrooms, unit_size=unit_size, rent_amount=rent, 
                                              security_deposit=deposit, availability=availability, unit_description=description)                                
                myproperty.save()

                messages.success(request, "Your property has successfully been added")
             

            else:
                messages.error(request, "Please login")
                return redirect('login')
            
    return render(request, "landlord/landlordApartment.html", {'customer': customer})
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
      
# def apartment_search(request):
#     if request.method == 'GET':
#         search_term = request.GET.get('search_term', '')  # Get the search term from the request
#         query = Q()
#         for field in ParentProperty._meta.fields:  # Iterate over all fields in the Apartment model
#             if field.get_internal_type() in ['CharField', 'TextField']:  # Consider only text-like fields
#                 query |= Q(**{f"{field.name}__contains": search_term})  # Use __contains for each text-like field
#         apartments = ParentProperty.objects.filter(query)

#         return render(request, 'apartment_search.html', {'apartments': apartments})
#     else:
#         return render(request, 'apartment_search.html')