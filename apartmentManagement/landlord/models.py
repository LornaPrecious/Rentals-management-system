from django.db import models
from main.models import *

class ParentProperty(models.Model):
    if Customer.role == 'landlord':
        customer = models.ForeignKey(Customer, on_delete = models.CASCADE, null = True, blank=True)

    PROPERTY_TYPES = [
        ('apartment_building', 'Apartment Building'),
        ('single_family_home', 'Single Family Home'),
        ('condominium', 'Condominium'),
        ('duplex', 'Duplex')
        # Add more property types as needed
    ]

    property_code = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=100, null=True, blank = True) #name of apartment building
    property_image = models.ImageField(null=True, blank=True)
    address = models.CharField(max_length=255) #Where the apartment is located
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES, default='apartment_building')
    total_units = models.CharField(max_length=250, default = 1) #number of apartment, homes, etc. 
    property_size = models.CharField(max_length=250, help_text="Size of the property in square feet", blank=True, null=True)
    building_age = models.CharField(max_length=250, help_text="Age of the building in years", blank=True, null=True)
    management_company = models.CharField(max_length=100, blank=True, null=True) #If it is managed by a third party
    amenities = models.TextField(blank=True, null=True) #gym, swimming pool, parking etc
    utilities = models.TextField(blank=True, null=True) #water, electricity, gas)
    maintenance_services = models.TextField(blank=True, null=True) #if offered by property owner
    parking = models.TextField(blank=True, null=True) #none,  garage, open parking lot
    security_features = models.TextField(blank=True, null=True) #cctvs, watchmen, gated access, dogs, etc
    rules_regulations = models.TextField(blank=True, null=True) #noise policies, pet policies, smoking policies,
    accessibility = models.TextField(blank=True, null=True) # wheelchair ramps, elevators
    lease_terms = models.TextField(blank=True, null=True)
    description = models.TextField(null=True, blank=True)
  
    def __str__(self):
        return str(self.property_code)
    class Meta:
        db_table='property_information'


    @property #help us access this as an attribute rather than as a model
    def property_imageURL(self):
        try: 
            url = self.property_image.url
        except:
            url = ''
        return url

#Tenant Information: Information about current and past tenants occupying units within the property.
#insurance_info = models.TextField(blank=True, null=True)
#financial_info = models.TextField(blank=True, null=True)
#documentation = models.TextField(blank=True, null=True)


class Units(models.Model):
    parent_property = models.ForeignKey(ParentProperty, on_delete = models.CASCADE)

    unit_number = models.CharField(max_length = 100, primary_key = True)
    unit_image = models.ImageField(null=True, blank=True)
    floor_number = models.CharField(max_length=100, null=True, blank = True) #Which floor is the apartment located in
    bedrooms = models.CharField(max_length=100, null=True, blank = True) 
    bathrooms = models.CharField(max_length=100, null=True, blank = True) #na
    unit_size = models.CharField(max_length=100, null=True, blank = True) #square foot
    rent_amount = models.IntegerField(null=True, blank = True) #
    security_deposit = models.IntegerField(null=True, blank=True)
    availability = models.BooleanField(null=True, blank=True)
    description = models.TextField(null=True, blank = True)

    def __str__(self):
        return self.unit_number
    class Meta:
        db_table='unit_information'


    @property #help us access this as an attribute rather than as a model
    def unit_imageURL(self):
        try: 
            url = self.unit_image.url
        except:
            url = ''
        return url


class Tenants(models.Model):
    unit = models.ForeignKey(Units, on_delete = models.CASCADE)

    tenants_id = models.CharField(max_length = 25, primary_key = True)
    first_name = models.CharField(max_length= 100, null=True, blank=True)
    last_name = models.CharField(max_length= 100, null=True, blank=True)
    dob = models.DateField(max_length = 200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.IntegerField(help_text='0712345678 or +254712345678', null=True, blank=True) #look for a validator, ie. regex 
    gender = models.CharField(max_length=10)
    lease_start = models.DateField()
    lease_end = models.DateField(null=True, blank=True)
    lease_term = models.CharField(max_length = 200, null=True, blank=True)
    emergency_contact_name = models.CharField(max_length = 250, null=True, blank=True)
    emergency_contact_phone = models.CharField(max_length = 250, null=True, blank=True)
    
    def __str__(self):
        return self.tenants_id
    class Meta:
        db_table='tenants_information'

    