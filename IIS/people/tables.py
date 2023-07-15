import django_tables2 as tables

from . import models
from design.tables import TableStyleMeta


class PeopleTable(tables.Table):
    patronymic = tables.Column(verbose_name='Отчество', orderable=False)
    actions = tables.TemplateColumn(template_name='people/cell_action.html', verbose_name='', orderable=False)

    class Meta(TableStyleMeta):
        model = models.Person
        fields = 'surname', 'name', 'patronymic', 'organisation',
        row_attrs = {
            'person-id': lambda record: record.pk
        }


# class PeopleEventTable(tables.Table):
#     actions = tables.TemplateColumn(template_name='people/cell_action.html', verbose_name='', orderable=False)
#
#     class Meta(TableStyleMeta):
#         model = models.Person
#         fields = 'surname', 'name', 'patronymic',
#         row_attrs = {
#             'person-id': lambda record: record.pk
#         }
