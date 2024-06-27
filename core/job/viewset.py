from django.shortcuts import render
from django.http import Http404
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from rest_framework.response import Response
from core.abstract.viewset import AbstractViewset
from .models import Job
from .serializer import JobSerializer

# Create your views here.
class JobViewset(AbstractViewset):
    permission_classes = (AllowAny,)
    http_method_names = ('post', 'get', 'patch', 'delete')
    serializer_class = JobSerializer

    def get_queryset(self):
        return Job.objects.all()

    def get_object(self):
        job = Job.objects.get_by_id(self.kwargs['pk'])
        if job == Http404:
            return Response("job not found", HTTP_404_NOT_FOUND)
        self.check_object_permissions(self.request, obj=job)
        return job

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, HTTP_201_CREATED)