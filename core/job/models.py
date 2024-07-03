from typing import Any
from django.db import models, transaction
from core.abstract.model import AbstractManager, AbstractModel
from core.role.models import Role

# Create your models here.

class JobManager(AbstractManager):

    @transaction.atomic
    def create(self, **kwargs: Any) -> Any:
        job = super().create(**kwargs)
        role = Role.objects.create(Job=job, Employee=job.CurrentEmployee)
        return job
    pass

class Job(AbstractModel):
    JobName = models.CharField(max_length=50)
    Department = models.ForeignKey(to='department.Department', on_delete=models.CASCADE)
    CurrentEmployee = models.ForeignKey(to='employee.Employee', on_delete=models.PROTECT, null=True, default=None)
    
    objects = JobManager()


