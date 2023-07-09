from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models, serializers


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer

    def __check_pk(self, pk):
        if pk is None:
            return Response({'error': 'Method GET is not allowed'})
        try:
            return models.Person.objects.get(id=pk)
        except:
            return Response({'error': f'Person object with pk={pk} does not exist'})

    @action(methods=['get'], detail=True)
    def get_events(self, request, pk=None):
        res = self.__check_pk(pk)
        if isinstance(res, models.Person):
            return Response({'events': [ev.id for ev in res.get_events_list()]})
        return res

    @action(methods=['get'], detail=True)
    def get_departments(self, request, pk=None):
        res = self.__check_pk(pk)
        if isinstance(res, models.Person):
            return Response({'departments': [dp.id for dp in res.get_departments_list()]})
        return res
