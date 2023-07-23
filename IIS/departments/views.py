from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from django_tables2 import SingleTableView
from django.contrib.auth.models import Group

from bootstrap_modal_forms.generic import BSModalDeleteView

from . import forms, models, tables
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
            is_supervisor = dp.supervisor_instance == Person.objects.get(user_instance=user)
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


def delete_department(request, pk):
    try:
        dp = models.Department.objects.get(id=pk)
    except models.Department.DoesNotExist:
        return HttpResponse(status=404)
    if request.user.is_superuser:
        for pn in dp.activists.all():
            if not pn.is_user:
                continue
            usr = pn.user_instance
            usr.groups.remove(Group.objects.get(name=models.Department.CRUD))
            usr.groups.remove(Group.objects.get(name=models.Department.READONLY))
            for dp in pn.get_departments_list():
                if dp.permissions == models.Department.NONE:
                    continue
                Group.objects.get(name=dp.permissions).user_set.add(usr)
        dp.delete()
        return HttpResponseRedirect(reverse_lazy('departments_list'))
    return HttpResponse(status=404)


class DepartmentAddView(CreateView):
    template_name = 'departments/create.html'
    model = models.Department
    form_class = forms.DepartmentAddForm

    def get_success_url(self):
        return reverse_lazy('department_detail', kwargs={'pk': self.object.id})
