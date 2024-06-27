from core.abstract.serializer import AbstractSerializer
from .models import Employee

class EmployeeSerializer(AbstractSerializer):

    class Meta:
        model = Employee
        fields = ['id', 'EmployeeName', 'Address', 'Email', 'Employed', 'Created', 'Updated']
        read_only_fields = ['id', 'Created', 'Updated']
