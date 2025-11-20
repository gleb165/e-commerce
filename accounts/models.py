from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        return self.username
    
    


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100, blank=True)
    # delivery to home customer 
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=20, blank=True)
    apartment = models.CharField(max_length=20, blank=True)
    # delivery to post office
    post_office_ref = models.CharField(max_length=100, blank=True)
    post_office_address = models.CharField(max_length=100, blank=True)
    
    delivery_type = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        customer_address = f"{self.city}, {self.region}, {self.street}, {self.building} - {self.apartment} "
        return f"{customer_address or self.post_office_address}"