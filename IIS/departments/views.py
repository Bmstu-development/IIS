from django.views.generic import DetailView, CreateView
from django_tables2 import SingleTableView

from . import models, tables
from people.models import Person
from people.tables import PeopleTable


class DepartmentsListView(SingleTableView):
    template_name = 'departments/list.html'
    table_class = tables.DepartmentsTable
    model = models.Department


class DepartmentDetailView(DetailView):
    template_name = 'departments/detail.html'
    model = models.Department

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dp = self.object
        user = self.request.user
        try:
            is_supervisor = dp.supervisor_instance == Person.objects.get(user_instance=self)
        except Person.DoesNotExist:
            is_supervisor = False
        context.update({
            'fields': dp.get_fields().items(),
            'supervisor': (dp.supervisor_instance.id,
                           dp.supervisor_instance) if dp.supervisor_instance else (None, None),
            'activists_list': PeopleTable(dp.get_activists_list()),
            'is_allowed_edit': user.is_superuser or is_supervisor,
            'is_allowed_delete': user.is_superuser,
        })
        return context


class DepartmentAddView(CreateView):
    pass
