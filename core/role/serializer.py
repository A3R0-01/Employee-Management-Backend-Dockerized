from rest_framework.serializers import SlugRelatedField
from core.job.models import Job
from core.employee.models import Employee
from core.abstract.serializer import AbstractSerializer
from .models import Role

class RoleSerializer(AbstractSerializer):
    Job = SlugRelatedField(queryset=Job.objects.all(), slug_field="PublicId")
    Employee = SlugRelatedField(queryset=Employee.objects.all(), slug_field="PublicId")
    
    class Meta:
        model = Role
        fields = ['id', 'Job', 'Employee', 'DateLeft', 'Updated', 'Created']
        read_only_fields = ['id', 'Updated', 'Created']
