from rest_framework import filters
from rest_framework import viewsets

class AbstractViewset(viewsets.ModelViewSet):
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["Created", "Updated"]
    ordering = ["-Created"]