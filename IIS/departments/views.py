from django.views.generic import DetailView, CreateView
from django_tables2 import SingleTableView

from . import models


class DepartmentsListView(SingleTableView):
    template_name = ''
    # table_class = None
    # model = models.Person


class DepartmentAddView(CreateView):
    pass


class DepartmentDetailView(DetailView):
    pass
