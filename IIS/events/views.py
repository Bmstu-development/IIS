from django.views.generic import DetailView, CreateView
from django_tables2 import SingleTableView

from . import models, tables
from people.tables import PeopleTable


class EventsListView(SingleTableView):
    template_name = 'events/list.html'
    table_class = tables.EventsTable
    model = models.Event

    def get_queryset(self):
        fields = [
            'name',
            'dt_start',
            'dt_finish',
            'status',
        ]
        return super().get_queryset().only(*fields)


class EventDetailView(DetailView):
    template_name = 'events/detail.html'
    model = models.Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ev = self.object
        context.update({
            'fields': ev.get_fields().items(),
            'supervisors': {sv.id: sv for sv in ev.supervisors.all()}.items(),
            'teachers': {tch.id: tch for tch in ev.teachers.all()}.items(),
            'listeners_table': PeopleTable(ev.get_students_list()),
        })
        return context


class EventAddView(CreateView):
    pass
