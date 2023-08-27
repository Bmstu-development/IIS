from simple_history.models import HistoricalRecords

from django.db import models

from datetime import timezone

from departments.models import Department


class EventManager(models.Manager):
    """

    """

    def for_user(self, user, view_only=False):
        """

        :param user:
        :param view_only:
        :return:
        """
        if view_only or user.is_superuser or Department.CRUD in user.groups.all().values_list('name', flat=True):
            # для просмотра доступны все
            # администратору доступны все
            # пользователям с CRUD правом доступны все
            return self.get_queryset()
        return Event.objects.none()


class Event(models.Model):
    # TODO на странице создания: в поле указывается число раз, столько создается рамок, в каждой из которых ввод
    #  времени, аудитории, [преподавателя]
    name = models.CharField(verbose_name='Название')
    descr = models.TextField(verbose_name='Описание', blank=True, null=True)
    dt_start = models.DateField(verbose_name='Дата начала', blank=True, null=True)
    dt_finish = models.DateField(verbose_name='Дата конца', blank=True, null=True)
    t_start = models.TimeField(verbose_name='Время начала', blank=True, null=True)
    t_finish = models.TimeField(verbose_name='Время конца', blank=True, null=True)
    frequently = models.IntegerField(verbose_name='Частота занятий', blank=True, null=True)
    audience_num = models.CharField(verbose_name='Номер аудитории', blank=True, null=True)
    teachers = models.ManyToManyField('people.Person', verbose_name='Преподаватель',
                                      related_name='event_teacher_match', blank=True)
    supervisors = models.ManyToManyField('people.Person', verbose_name='Староста',
                                         related_name='event_supervisor_match', blank=True)
    listeners = models.ManyToManyField('people.Person', verbose_name='Слушатели', related_name='event_listeners_match',
                                       blank=True)
    status = models.IntegerField(verbose_name='Статус', default=0)
    history = HistoricalRecords()

    objects = EventManager()

    class Meta:
        ordering = 'dt_start', 'name',
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return self.name

    def get_fields(self):
        dct = dict()

        fields = ['name', 'descr', 'dt_start', 'dt_finish', 't_start', 't_finish', 'frequently', 'audience_num']
        fields_to_hide_if_none = ['descr']
        fields_to_replace_if_none = {
            'dt_start': 'Не выбрана',
            'dt_finish': 'Не выбрана',
            't_start': 'Не выбрано',
            't_finish': 'Не выбрано',
            'frequently': 'Не выбрана',
            'audience_num': 'Не выбрана',
        }
        fields_date = ['dt_start', 'dt_finish']
        fields_time = ['t_start', 't_finish']
        for field in fields:
            field_value = getattr(self, field)
            if field in fields_to_hide_if_none and not field_value:
                continue
            if field in fields_to_replace_if_none and not field_value:
                field_value = fields_to_replace_if_none[field]
            elif field in fields_date:
                field_value = field_value.strftime('%d.%m.%Y')
            elif field in fields_time:
                field_value = field_value.strftime('%H:%M')
            dct[self._meta.get_field(field).verbose_name] = field_value
        return dct

    def get_teachers_list(self):
        """
        Возвращает список всех преподавателей курса
        :return:
        """
        return self.teachers.all()

    def get_supervisors_list(self):
        """
        Возвращает список всех старост курса
        :return:
        """
        return self.supervisors.all()

    def get_students_list(self):
        """
        Возвращает список всех слушателей курса
        :return:
        """
        return self.listeners.all()

    def get_last_changes_data(self):
        """

        :return:
        """
        change_date = self.history.all().first().history_date.replace(tzinfo=timezone.utc).astimezone(tz=None)
        change_date = change_date.strftime('%d.%m.%Y %H:%M')
        change_person = self.history.all().first().history_user
        output = f'Последнее изменение: {change_date}'
        if not change_person:
            return output
        if change_person.get_full_name():
            return output + f', выполнено пользователем {change_person.get_full_name()}'
        return output + f', выполнено пользователем {change_person.username}'
