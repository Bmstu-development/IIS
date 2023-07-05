from django.views.generic import DetailView, CreateView
from django_tables2 import SingleTableView

from . import models, tables


class DepartmentsListView(SingleTableView):
    template_name = 'departments/list.html'
    table_class = tables.DepartmentsTable
    model = models.Department


class DepartmentDetailView(DetailView):
    template_name = 'departments/detail.html'
    model = models.Department

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'fields': self.object.get_fields().items(),
        })
        return context


class DepartmentAddView(CreateView):
    pass
