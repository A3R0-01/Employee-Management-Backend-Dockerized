from rest_framework.serializers import SlugRelatedField
from core.abstract.serializer import AbstractSerializer
from core.company.models import Company
from .models import Registration

class RegistrationSerializer(AbstractSerializer):
    Company = SlugRelatedField(queryset=Company.objects.all(), slug_field="PublicId")

    class Meta:
        model = Registration
        fields = ['id', 'Company', 'Created', 'Updated']
        read_only_fields = ['id', 'Created', 'Updated']

