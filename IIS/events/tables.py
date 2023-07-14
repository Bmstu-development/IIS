import django_tables2 as tables

from . import models
from design.tables import TableStyleMeta


class EventsTable(tables.Table):
    actions = tables.TemplateColumn(template_name='events/cell_action.html', verbose_name='', orderable=False)

    class Meta(TableStyleMeta):
        model = models.Event
        fields = 'name', 'dt_start', 'dt_finish', 'status',
        row_attrs = {
            'event-id': lambda record: record.pk
        }


class EventsPersonTable(tables.Table):
    person_status = tables.Column(verbose_name='Статус', empty_values=())
    descr = tables.Column(verbose_name='Описание', orderable=False)
    actions = tables.TemplateColumn(template_name='events/cell_action.html', verbose_name='', orderable=False)

    def __init__(self, *args, **kwargs):
        self.__person_id = kwargs.pop('person_id')
        super().__init__(*args, **kwargs)

    def render_person_status(self, record):
        """

        :param record:
        :return:
        """
        event = models.Event.objects.get(id=record.pk)
        return ('староста' * (event.supervisors and self.__person_id in event.supervisors.values_list(
            flat=True)) + ' преподаватель' * (event.teachers and self.__person_id in event.teachers.values_list(
            flat=True)) + ' слушатель' * (event.listeners and self.__person_id in event.listeners.values_list(
            flat=True))).strip(' ').replace(' ', ', ').capitalize()

    class Meta(TableStyleMeta):
        model = models.Event
        fields = 'name',
        sequence = 'person_status', 'name', 'descr', 'actions',
        row_attrs = {
            'event-id': lambda record: record.pk
        }
