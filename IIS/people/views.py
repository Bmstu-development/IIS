from django_tables2 import SingleTableView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, CreateView

from . import models, tables


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
        context.update({
            'fields': self.object.get_fields().items(),
            # 'departments': self.object.get_departments_list(),
            # 'events': self.object.get_events_list(),
        })
        return context


class PersonAddView(CreateView):
    pass
