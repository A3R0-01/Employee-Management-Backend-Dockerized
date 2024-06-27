from typing import Any
from django.db import models, transaction
from core.abstract.model import AbstractManager, AbstractModel
from core.company.models import Company
# Create your models here.

class RegistrationManager(AbstractManager):
    @transaction.atomic
    def create(self, **kwargs: Any) -> Any:
        registration = super().create(**kwargs)
        company = Company.objects.get_by_id(registration.Company.PublicId)
        company.Registration = registration.PublicId
        company.Registered = True
        company.DateOfRegistration = registration.Created
        company.save()
        return registration
    pass


class Registration(AbstractModel):
    Company = models.ForeignKey(to="company.Company", on_delete=models.CASCADE)
    
    objects = RegistrationManager()


