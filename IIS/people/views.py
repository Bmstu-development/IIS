from django.views.generic import DetailView, CreateView
from django_tables2 import SingleTableView

from . import models, tables


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


class PersonAddView(CreateView):
    pass


class PersonDetailView(DetailView):
    pass
