from django.db import models
from core.abstract.model import AbstractManager, AbstractModel

# Create your models here.
class DepartmentManager(AbstractManager):
    pass

class Department(AbstractModel):
    DepartmentName = models.CharField(max_length=256, unique=True)
    NumberOfEmployees = models.IntegerField(default=0)
    Company = models.ForeignKey(to="company.Company", on_delete=models.CASCADE)


    objects = DepartmentManager()

