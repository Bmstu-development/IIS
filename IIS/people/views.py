from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django_tables2 import SingleTableView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, CreateView

from . import models, tables, serializers


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


def redirect_from_start_page(request):
    return HttpResponseRedirect(reverse('people_list'))


class PeopleListView(SingleTableView):
    template_name = 'people/list.html'
    table_class = tables.PeopleTable
    model = models.Person

    def get_queryset(self):
        fields = [
            'surname',
            'name',
            'patronymic',
            'organisation',
        ]
        return super().get_queryset().only(*fields)


class PersonDetailView(DetailView):
    template_name = 'people/detail.html'
    model = models.Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'fields': self.object.get_fields().items(),
            # 'departments': self.object.get_departments_list(),
            # 'events': self.object.get_events_list(),
        })
        return context


class PersonAddView(CreateView):
    pass
