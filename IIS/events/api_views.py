from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from . import models, serializers


class EventsViewSet(viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
    permission_classes = IsAdminUser,
