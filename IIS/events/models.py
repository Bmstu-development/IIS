from django.db import models

from people.models import Person


class Event(models.Model):
    # TODO на странице создания: в поле указывается число раз, столько создается рамок, в каждой из которых ввод
    #  времени, аудитории, препода
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
    status = models.IntegerField(verbose_name='Статус', default=0)

    def __str__(self):
        return self.name

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
        result = list()
        for pn in Person.objects.all():
            if self in pn.get_events_list():
                result.append(pn)
        return result

    class Meta:
        ordering = '-dt_start', '-name',
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
