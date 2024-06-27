from rest_framework import serializers
from .model import AbstractFileModel

class AbstractSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='PublicId', read_only=True, format="hex")
    Created = serializers.DateTimeField(read_only=True)
    Updated = serializers.DateTimeField(read_only=True)

class AbstractFileSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = AbstractFileModel
        fields = ['file']