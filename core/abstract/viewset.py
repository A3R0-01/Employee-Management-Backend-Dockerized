from django.shortcuts import render
from django.db import transaction
from django.core.files import uploadedfile
from collections.abc import Callable
from typing import Type
import pandas as pd
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_429_TOO_MANY_REQUESTS, HTTP_200_OK
from .serializer import AbstractFileSerializer, AbstractSerializer


class AbstractViewset(viewsets.ModelViewSet):
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["Created", "Updated"]
    ordering = ["-Created"]

class AbstractBulkViewset(AbstractViewset):
    permission_classes = (AllowAny,)
    http_method_names = ('post', 'patch')
    serializer_class = AbstractFileSerializer
    model_serializer: Type[AbstractSerializer]


    def get_file(self, request):
        file_serializer = self.serializer_class(data=request.data)
        file_serializer.is_valid(raise_exception=True)
        return file_serializer.validated_data['file']


    def bulk_operation(self, request, function: Callable[[any, any], Response]):
        file = self.get_file(request)
        try:
            if uploadedfile.UploadedFile(file).name.endswith('.csv'):
                return function(request, file)
            return Response("incorrect file format", HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(e.__dict__, HTTP_400_BAD_REQUEST)


    def to_records(self, file):
        return pd.read_csv(file).to_dict(orient='records')


    def bulk_create_operations(self, request, file) -> Response:
        serializer = self.model_serializer(data=self.to_records(file), many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, HTTP_201_CREATED)

    def bulk_update_operations(self, request, file) -> Response:
        updates = []
        for r in self.to_records(file):
            id = r.pop("id")
            for key in r.keys():
                request.data[key] = r[key]
            instance = self.model_serializer.Meta.model.objects.get_by_id(id)
            serializer = self.model_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            updates.append(serializer.data)
        return Response(updates, HTTP_200_OK)


    # def bulk_create(self, request):
    #     return self.bulk_operation(request, self.bulk_create_operations)


    # def bulk_update(self, request):
    #     return self.bulk_operation(request, self.bulk_update_operations)


    @transaction.atomic
    def update(self, request, *args, **kwargs):
        return self.bulk_operation(request, self.bulk_update_operations)


    @transaction.atomic
    def create(self, request, *args, **kwargs):
        return self.bulk_operation(request, self.bulk_create_operations)


