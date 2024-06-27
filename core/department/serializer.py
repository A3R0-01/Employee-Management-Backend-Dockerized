from core.abstract.serializer import AbstractSerializer
from core.company.models import Company
from .models import Department
from rest_framework.serializers import SlugRelatedField

class DepartmentSerializer(AbstractSerializer):
    Company = SlugRelatedField(queryset=Company.objects.filter(Registered=True), slug_field="PublicId")

    class Meta:
        model = Department
        fields = ['id','DepartmentName','NumberOfEmployees','Company', 'Created', 'Updated']
        read_only_fields = ['id', 'Created', 'Updated']
