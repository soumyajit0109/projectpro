from django.db import models
from phone_field import PhoneField

class Person(models.Model):
    name = models.CharField(max_length=30)
    phone =PhoneField(blank=True)
    email = models.EmailField(blank=True)
    joining_code = models.CharField(max_length=100, blank=True)
    designation = models.CharField(max_length=100, blank=True)
    employee_id=models.CharField(max_length=100, blank=True)
    
