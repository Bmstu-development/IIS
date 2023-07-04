import django_tables2 as tables

from . import models


class PeopleTable(tables.Table):
    actions = tables.TemplateColumn(template_name='people/cell_action.html', verbose_name='')

    class Meta:
        model = models.Person
        fields = 'surname', 'name', 'patronymic', 'organisation',
