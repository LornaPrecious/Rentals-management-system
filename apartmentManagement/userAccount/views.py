from django.http import HttpResponse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from main.models import Customer
from django.contrib.sites.shortcuts import get_current_site 
from apartmentManagement import settings
from django.utils.encoding import force_bytes, force_str, force_text
from .tokens import generate_token

# Create your views here.

def register (request):
      if request.method =="POST":
            username = request.POST['username'] 
            fname = request.POST['fname']
            lname = request.POST['lname'] 
            email = request.POST['email']       
            password = request.POST['password']
            pass2 = request.POST['pass2']
            phonenumber = request.POST['phonenumber']
            gender = request.POST['gender'] 
            classify = request.POST['classify'] 
          
            if User.objects.filter(username=username):
                  messages.error(request, "Username already exist! Please try again")
                  return redirect('register')
            
            if User.objects.filter(email=email):
                  messages.error(request,"Email address is already registered!")
                  return redirect('register')
            
            if password != pass2:
                  messages.error(request, "Passwords did not match!")        


            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname
            user.is_active = False
            user.save()
            
            mycustomer=Customer(user = user, first_name = fname, last_name = lname, email=email, password=password, phone_number=phonenumber, gender=gender, classification = classify)                                
            mycustomer.save()

            messages.success(request, "Your account has been created successfully. Please check your email for email verification.")

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

            return redirect('login')

      return render(request, "registration/register.html")

def custom_login(request):
      if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                  login(request, user)
                  username = user.username
                  return render(request, "main/home.html", {'username': username})

            else:
                  messages.error(request, "Wrong credentials")
                  return redirect('register')

      return render(request, "registration/login.html")

def signout(request):
      logout(request)
      messages.success(request, 'Logout successfully')
      return redirect('home')

def activate(request, uidb64, token):
      try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user= User.objects.get(pk=uid)
      except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

      if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('home')
      else:
           return render(request, 'activation_failed.html')

