from django_tables2 import SingleTableView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
# from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView

from . import forms, models, tables
from departments.models import Department
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            is_supervisor = models.Person.objects.get(user_instance=self.request.user).is_supervisor()
        except models.Person.DoesNotExist:
            is_supervisor = False
        context.update({
            'is_allowed_create': Department.CRUD in self.request.user.groups.all().values_list('name', flat=True) or
                                 is_supervisor or
                                 self.request.user.is_superuser,
        })
        return context


class PersonDetailView(PersonViewFilterMixin, DetailView):
    template_name = 'people/detail.html'
    model = models.Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pn = self.object
        user = self.request.user
        try:
            is_subordinate = pn.pk in models.Person.objects.get(user_instance=user).get_subordinates_pk_list()
        except models.Person.DoesNotExist:
            is_subordinate = False
        is_crud_allowed = Department.CRUD in user.groups.all().values_list('name', flat=True)
        context.update({
            'fields': pn.get_fields().items(),
            'departments_table': DepartmentsPersonTable(pn.get_departments_list(), person_id=pn.id),
            'events_table': EventsPersonTable(pn.get_events_list(), person_id=pn.id),
            'is_allowed_delete': user.is_superuser or (not pn.is_user and is_crud_allowed) or is_subordinate,
            'is_allowed_edit': pn.user_instance == user or user.is_superuser or is_subordinate or (
                    is_crud_allowed and not pn.is_user),
            'is_allowed_create_delete_user': (user.is_superuser or is_subordinate) and pn.user_instance != user,
        })
        return context


# @method_decorator(name='post')
class PersonAddView(CreateView):
    template_name = 'people/create.html'
    model = models.Person
    form_class = forms.PersonCreateForm

    def get_success_url(self):
        return reverse_lazy('person_detail', kwargs={'pk': self.object.id})
