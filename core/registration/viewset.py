from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from rest_framework.exceptions import NotFound
from core.abstract.viewset import AbstractViewset, AbstractBulkViewset
from .serializer import RegistrationSerializer
from .models import Registration
# Create your views here.

class RegistrationViewset(AbstractViewset):
    permission_classes = (AllowAny,)
    http_method_names = ('post', 'patch', 'get', 'delete')
    serializer_class = RegistrationSerializer


    def get_queryset(self):
        return Registration.objects.all()
    def get_object(self):
        obj = Registration.objects.get_by_id(self.kwargs['pk'])
        if Http404 is obj: raise NotFound("registration not found", HTTP_404_NOT_FOUND)
        self.check_object_permissions(self.request, obj)
        return obj
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=HTTP_201_CREATED)

class RegistrationBulkViewset(AbstractBulkViewset):
    model_serializer = RegistrationSerializer
