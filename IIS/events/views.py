from django.views.generic import DetailView, CreateView
from django_tables2 import SingleTableView

from . import models


class EventsListView(SingleTableView):
    template_name = ''
    # table_class = None
    # model = models.Person


class EventAddView(CreateView):
    pass


class EventDetailView(DetailView):
    pass
