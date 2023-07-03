from django.db import models


class Person(models.Model):
    name = models.TextField(verbose_name='Имя', blank=True, null=False)
    surname = models.TextField(verbose_name='Фамилия', blank=True, null=False)
    patronymic = models.TextField(verbose_name='Отчество', blank=True, null=True)
    organisation = models.TextField(verbose_name='Организация', blank=True, null=False)
    bmstu_group = models.TextField(verbose_name='Учебная группа (МГТУ)', blank=True, null=True)
    phone_number = models.TextField(verbose_name='Телефонный номер', blank=True, null=False)
    tg_username = models.TextField(verbose_name='Тег в телеграме', blank=True, null=False)
    departments = models.ManyToManyField('departments.Department', related_name='person_department_match', blank=True,
                                         default=list())
    events = models.ManyToManyField('events.Event', related_name='person_event_match', blank=True, default=list())

    class Meta:
        ordering = '-surname', '-name', '-patronymic',
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
