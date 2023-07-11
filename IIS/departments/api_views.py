from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from . import models, serializers


class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    permission_classes = IsAdminUser,
