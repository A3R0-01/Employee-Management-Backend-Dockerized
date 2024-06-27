from .models import Company
from core.abstract.serializer import AbstractSerializer

class CompanySerializer(AbstractSerializer):
    class Meta:
        model = Company
        fields = ['id', 'CompanyName', 'DateOfRegistration','Address','NumberOfEmployees','ContactPhone','Email','Registration', 'Registered', 'Created', 'Updated']
        read_only_fields = ['id','Registered', 'Created', 'Updated']

    