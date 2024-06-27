from typing import Any
from django.db import models, transaction
from django.http import Http404
from core.abstract.model import AbstractManager, AbstractModel
# from core.job.models import Job
import datetime
import pytz

# Create your models here.
class RoleManager(AbstractManager):

    @transaction.atomic
    def create(self, **kwargs: Any) -> Any:
        role = super().create(**kwargs)
        job = role.Job
        job.CurrentEmployee = role.Employee
        job.save()
        return role

    @transaction.atomic
    def terminate_role(self, public_id):
        role = self.get_by_id(public_id)
        if role == Http404:
            return Http404
        python_time = datetime.datetime.now() 
        utc_timezone = pytz.timezone('UTC')
        python_time_utc = python_time.astimezone(utc_timezone)
        django_time_format = "%Y-%m-%dT%H:%M:%S.%fZ"
        role.DateLeft = python_time_utc.strftime(django_time_format)
        role.save()
        job = role.Job
        job.CurrentEmployee = None
        job.save()
        return role




class Role(AbstractModel):
    Job = models.ForeignKey(to='job.Job', on_delete=models.CASCADE)
    Employee = models.ForeignKey(to='employee.Employee', on_delete=models.CASCADE)
    DateLeft = models.DateTimeField(null=True, default=None)


    objects = RoleManager()

