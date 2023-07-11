from simple_history.models import HistoricalRecords

from django.db import models

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
        for field in fields:
            dct[self._meta.get_field(field).verbose_name] = getattr(self, field)
        dct[self._meta.get_field('teachers').verbose_name] = ', '.join([str(p) for p in self.get_teachers_list()])
        dct[self._meta.get_field('supervisors').verbose_name] = ', '.join([str(p) for p in self.get_supervisors_list()])
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
