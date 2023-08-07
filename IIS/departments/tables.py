import django_tables2 as tables

from . import models
from design.tables import TableStyleMeta


class DepartmentsTable(tables.Table):
    descr = tables.Column(verbose_name='Описание', orderable=False)
    actions = tables.TemplateColumn(template_name='departments/cell_action.html', verbose_name='', orderable=False)

    class Meta(TableStyleMeta):
        model = models.Department
        fields = 'name', 'descr',
        row_attrs = {
            'department-id': lambda record: record.pk
        }


class DepartmentsActivistsTable(tables.Table):
    person_status = tables.Column(verbose_name='Статус', empty_values=())
    descr = tables.Column(verbose_name='Описание', orderable=False)
    actions = tables.TemplateColumn(template_name='departments/cell_action.html', verbose_name='', orderable=False)

    def __init__(self, *args, **kwargs):
        self.__person_id = kwargs.pop('person_id')
        super().__init__(*args, **kwargs)

    def render_person_status(self, record):
        """

        :param record:
        :return:
        """
        department = models.Department.objects.get(id=record.pk)
        if department.supervisor_instance is None:
            return 'Активист'
        if department.supervisor_instance.id == self.__person_id:
            return 'Руководитель'
        return 'Активист'

    class Meta(TableStyleMeta):
        model = models.Department
        fields = 'name', 'descr',
        sequence = 'person_status', 'name', 'descr', 'actions',
        row_attrs = {
            'department-id': lambda record: record.pk
        }
