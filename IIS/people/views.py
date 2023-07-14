from django_tables2 import SingleTableView, RequestConfig
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, CreateView

from . import models, tables
from departments.tables import DepartmentsPersonTable
from events.tables import EventsPersonTable


class PersonViewFilterMixin:
    """

    """

    def get_queryset(self):
        return models.Person.objects.for_user(self.request.user, view_only=True)


class PersonChangeFilterMixin:
    """

    """

    def get_queryset(self):
        return models.Person.objects.for_user(self.request.user)


def redirect_from_start_page(request):
    return HttpResponseRedirect(reverse('people_list'))


class PeopleListView(PersonViewFilterMixin, SingleTableView):
    model = models.Person
    template_name = 'people/list.html'
    table_class = tables.PeopleTable
    paginate_by = 15

    def get_queryset(self):
        fields = [
            'surname',
            'name',
            'patronymic',
            'organisation',
        ]
        return super().get_queryset().only(*fields)


class PersonDetailView(PersonViewFilterMixin, DetailView):
    template_name = 'people/detail.html'
    model = models.Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pn = self.object
        departments_table = DepartmentsPersonTable(data=pn.get_departments_list(), person_id=pn.id)
        # RequestConfig(self.request).configure(departments_table)
        events_table = EventsPersonTable(pn.get_events_list(), person_id=pn.id)
        # RequestConfig(self.request).configure(events_table)
        context.update({
            'fields': self.object.get_fields().items(),
            'departments_table': departments_table,
            'events_table': events_table,
        })
        return context


class PersonAddView(CreateView):
    pass
