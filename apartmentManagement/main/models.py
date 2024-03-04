from django.db import models
from django.contrib.auth.models import AbstractUser, User, Group, Permission


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

    ROLE_CHOICES = (
        ('landlord', 'Landlord'),
        ('user', 'user'),
    )

    GENDER_CHOICES =(
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    )

    customer_id = models.IntegerField(primary_key= True,)
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)  #for authentication purposes
    first_name = models.CharField(max_length= 100, null=True, blank=True)
    last_name = models.CharField(max_length= 100, null=True, blank=True)
    customer_image = models.ImageField(null=True, blank=True)
    password = models.CharField(max_length= 100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.IntegerField(help_text='0712345678 or +254712345678', null=True, blank=True) #look for a validator, ie. regex 
    gender = models.CharField(max_length=10, null=True, blank=True, choices = GENDER_CHOICES)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, null=True, blank=True)
         
    def __str__(self):
        return str(self.customer_id)
    class Meta:
        db_table='customer'


    @property #help us access this as an attribute rather than as a model
    def customer_imageURL(self):
        try: 
            url = self.customer_image.url
        except:
            url = ''
        return url






    







