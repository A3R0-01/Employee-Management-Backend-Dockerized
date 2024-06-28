from django.shortcuts import render
from django.db import transaction
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from core.abstract.viewset import AbstractViewset, AbstractBulkViewset
from .serializer import DepartmentSerializer
from .models import Department
# Create your views here.
class DepartmentViewset(AbstractViewset):
    permission_classes = (AllowAny,)
    http_method_names = ('post', 'patch', 'get', 'delete')
    serializer_class = DepartmentSerializer


    def get_queryset(self):
        return Department.objects.all()
    def get_object(self):
        obj = Department.objects.get_by_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        print(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED)

class DepartmentBulkViewset(AbstractBulkViewset):
    model_serializer = DepartmentSerializer