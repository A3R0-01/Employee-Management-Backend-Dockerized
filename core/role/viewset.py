from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED
from core.abstract.viewset import AbstractViewset, AbstractBulkViewset
from .models import Role
from .serializer import RoleSerializer
# Create your views here.

class RoleViewset(AbstractViewset):
    permission_classes = (AllowAny,)
    http_method_names = ('post', 'get', 'patch', 'delete')
    serializer_class = RoleSerializer

    def get_queryset(self):
        return Role.objects.all()
    
    def get_object(self):
        obj = Role.objects.get_by_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, HTTP_201_CREATED)

class RoleTerminateViewset(AbstractViewset):
    permission_classes = (AllowAny,)
    http_method_names = ('get',)
    serializer_class = RoleSerializer

    def get_queryset(self):
        return Response("method not allowed", HTTP_401_UNAUTHORIZED)
    
    def get_object(self):
        terminatedRole = Role.objects.terminate_role(self.kwargs['pk'])
        if terminatedRole == Http404:
            return Response("object not found", HTTP_404_NOT_FOUND)
        self.check_object_permissions(self.request, terminatedRole)
        return terminatedRole

class RoleBulkViewset(AbstractBulkViewset):
    model_serializer = RoleSerializer