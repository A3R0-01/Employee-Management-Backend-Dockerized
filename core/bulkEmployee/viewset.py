from django.shortcuts import render
from django.db import transaction
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from core.abstract.viewset import AbstractViewset
from core.abstract.serializer import AbstractFileSerializer
from django.core.files import uploadedfile
from core.employee.models import Employee
from core.employee.serializer import EmployeeSerializer
import pandas as pd

# Create your views here.
class EmployeeBulk(AbstractViewset):
    permission_classes = (AllowAny,)
    http_method_names = ('post', 'patch')
    serializer_class = AbstractFileSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        file_serializer = self.serializer_class(data=request.data)
        file_serializer.is_valid(raise_exception=True)
        file = file_serializer.validated_data['file']
        try:
            if uploadedfile.UploadedFile(file).name.endswith('.csv'):
                data_frame = pd.read_csv(file)
                print(data_frame.head())
                serializer = EmployeeSerializer(data=data_frame.to_dict(orient='records'), many=True)
                serializer.is_valid(raise_exception=True)
                print("passed")
                serializer.save()
                return Response(serializer.data, HTTP_201_CREATED)

            return Response("incorrect file format", HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(e.__dict__, HTTP_400_BAD_REQUEST)
