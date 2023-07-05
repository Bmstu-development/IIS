import django_tables2 as tables

from . import models


class DepartmentsTable(tables.Table):
    actions = tables.TemplateColumn(template_name='departments/cell_action.html', verbose_name='')

    class Meta:
        model = models.Department
        fields = 'name',
