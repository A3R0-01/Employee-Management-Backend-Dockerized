from django.db import models
from core.abstract.model import AbstractManager, AbstractModel

# Create your models here.

class JobManager(AbstractManager):
    pass

class Job(AbstractModel):
    JobName = models.CharField(max_length=50)
    Department = models.ForeignKey(to='department.Department', on_delete=models.CASCADE)
    CurrentEmployee = models.ForeignKey(to='employee.Employee', on_delete=models.PROTECT, null=True, default=None)
    
    objects = JobManager()


