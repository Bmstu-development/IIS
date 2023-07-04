from django.views.generic import DetailView, CreateView
from django_tables2 import SingleTableView

from . import models


class PeopleListView(SingleTableView):
    template_name = 'people/list.html'
    # table_class = None
    model = models.Person


class PersonAddView(CreateView):
    pass


class PersonDetailView(DetailView):
    pass
