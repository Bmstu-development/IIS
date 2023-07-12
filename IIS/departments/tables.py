import django_tables2 as tables

from . import models
from design.tables import TableStyleMeta


class DepartmentsTable(tables.Table):
    descr = tables.Column(verbose_name='Описание', orderable=False)
    actions = tables.TemplateColumn(template_name='departments/cell_action.html', verbose_name='')

    class Meta(TableStyleMeta):
        model = models.Department
        fields = 'name', 'descr',
