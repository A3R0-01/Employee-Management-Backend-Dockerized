from django.db import models
from core.abstract.model import AbstractManager, AbstractModel
# Create your models here.

class EmployeeManager(AbstractManager):pass


class Employee(AbstractModel):
    EmployeeName = models.CharField(max_length=50)
    Address = models.CharField(max_length=150)
    Email = models.EmailField(unique=True)
    Employed = models.BooleanField(default=False)


    objects = EmployeeManager()
