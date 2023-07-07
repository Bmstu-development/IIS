from django.views.generic import DetailView, CreateView
from django_tables2 import SingleTableView

from . import models, tables


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
        context.update({
            'fields': self.object.get_fields().items(),
        })
        return context


class EventAddView(CreateView):
    pass
