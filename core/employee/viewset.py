from django.shortcuts import render
from rest_framework.status import HTTP_201_CREATED
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from core.abstract.viewset import AbstractViewset, AbstractBulkViewset
from .serializer import EmployeeSerializer
from .models import Employee

# Create your views here.
class EmployeeViewset(AbstractViewset):
    permission_classes = (AllowAny,)
    http_method_names = ('post','patch', 'delete','get')
    serializer_class = EmployeeSerializer

    def get_object(self):
        obj = Employee.objects.get_by_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    
    def get_queryset(self):
        return Employee.objects.all()
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=HTTP_201_CREATED)

class EmployeeBulkViewset(AbstractBulkViewset):
    model_serializer = EmployeeSerializer