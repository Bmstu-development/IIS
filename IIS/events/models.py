from django.db import models


class Event(models.Model):
    # TODO на странице создания: в поле указывается число раз, столько создается рамок, в каждой из которых ввод
    #  времени, аудитории, препода
    name = models.TextField(verbose_name='Название', blank=True, null=False)
    dt_start = models.DateField(verbose_name='Дата начала', blank=True, null=True)
    dt_finish = models.DateField(verbose_name='Дата конца', blank=True, null=True)
    t_start = models.TimeField(verbose_name='Время начала', blank=True, null=True)
    t_finish = models.TimeField(verbose_name='Время конца', blank=True, null=True)
    frequently = models.IntegerField(verbose_name='Частота занятий', blank=True, null=True)
    audience_num = models.TextField(verbose_name='Номер аудитории', blank=True, null=True)
    id_teacher = models.ManyToManyField('people.Person', verbose_name='Преподаватель',
                                        related_name='event_teacher_match')
    id_supervisor = models.ManyToManyField('people.Person', verbose_name='Староста',
                                           related_name='event_supervisor_match')
    status = models.IntegerField(verbose_name='Статус', blank=True, null=False, default=0)

    class Meta:
        ordering = '-dt_start', '-name',
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
