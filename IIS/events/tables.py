import django_tables2 as tables

from . import models


class EventsTable(tables.Table):
    actions = tables.TemplateColumn(template_name='events/cell_action.html', verbose_name='')

    class Meta:
        model = models.Event
        fields = 'name', 'dt_start', 'dt_finish', 'status',
