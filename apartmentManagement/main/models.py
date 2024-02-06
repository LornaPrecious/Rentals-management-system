from django.db import models
from django.contrib.auth.models import User



class Customer (models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    
    customer_id = models.IntegerField(primary_key= True,)
    first_name = models.CharField(max_length= 100, null=True, blank=True)
    last_name = models.CharField(max_length= 100, null=True, blank=True)
    password = models.CharField(max_length= 100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.IntegerField(help_text='0712345678 or +254712345678', null=True, blank=True) #look for a validator, ie. regex 
    gender = models.CharField(max_length=10)
         
    def __str__(self):
        return str(self.customer_id)
    class Meta:
        db_table='customer'


class Landlord(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    
    customer_id = models.IntegerField(primary_key= True,)
    first_name = models.CharField(max_length= 100, null=True, blank=True)
    last_name = models.CharField(max_length= 100, null=True, blank=True)
    password = models.CharField(max_length= 100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.IntegerField(help_text='0712345678 or +254712345678', null=True, blank=True) #look for a validator, ie. regex 
    gender = models.CharField(max_length=10)
         
    def __str__(self):
        return str(self.customer_id)
    class Meta:
        db_table='landlord'
    







