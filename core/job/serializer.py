from rest_framework.serializers import SlugRelatedField
from core.abstract.serializer import AbstractSerializer
from core.employee.models import Employee
from core.department.models import Department
from .models import Job

class JobSerializer(AbstractSerializer):
    CurrentEmployee = SlugRelatedField(queryset=Employee.objects.all(), slug_field='PublicId')
    Department = SlugRelatedField(queryset=Department.objects.all(), slug_field="PublicId")

    class Meta:
        model = Job
        fields = ['id', 'JobName', 'CurrentEmployee', 'Department', 'Created', 'Updated']
        read_only_fields = ['id', 'Created', 'Updated']