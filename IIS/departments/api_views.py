from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models, serializers


class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
