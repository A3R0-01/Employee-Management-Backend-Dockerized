from django.db import models
from core.abstract.model import AbstractModel, AbstractManager

# Create your models here.

class CompanyManager(AbstractManager):
    pass

class Company(AbstractModel):
    CompanyName = models.CharField(max_length=100, null=False, unique=True, db_index=True)
    DateOfRegistration = models.DateField(null=True)
    Address = models.CharField(max_length=100, null=False, unique=True)
    NumberOfEmployees = models.IntegerField(default=1)
    ContactPhone = models.CharField(max_length=20, null=False)
    Email = models.EmailField(unique=True, null=False)
    Registration = models.CharField(unique=True, default=None, null=True)
    Registered = models.BooleanField(default=False)
    
    objects = CompanyManager()

