from django.db import models
from django.db.models import Q

from departments.models import Department
from events.models import Event


class Person(models.Model):
    # TODO все люди сначала появляются в этой таблице, при необходимсти сделать этого человека пользователем нужно
    #  нажать на какую-то кнопку, тогда запись будет перенесена в таблицу пользователей, будет сгенерирован логин,
    #  пароль
    surname = models.CharField(verbose_name='Фамилия')
    name = models.CharField(verbose_name='Имя')
    patronymic = models.CharField(verbose_name='Отчество', blank=True, null=True)
    organisation = models.CharField(verbose_name='Организация')
    bmstu_group = models.CharField(verbose_name='Учебная группа (МГТУ)', blank=True, null=True)
    phone_number = models.CharField(verbose_name='Телефонный номер', blank=True, null=False)
    tg_username = models.CharField(verbose_name='Тег в телеграме', blank=True, null=False)

    class Meta:
        ordering = 'surname', 'name', 'patronymic',
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic if self.patronymic else ""}'

    def get_fields(self):
        dct = dict()

        fields = ['surname', 'name', 'patronymic', 'organisation', 'bmstu_group', 'phone_number', 'tg_username']
        for field in fields:
            dct[self._meta.get_field(field).verbose_name] = getattr(self, field)
        return dct

    def get_departments_pk_list(self):
        """
        Возвращает список всех отделов, куда человек входит
        :return:
        """
        return list(set([dp.id for dp in Department.objects.filter(Q(activists__id=self.id) | Q(id_supervisor=self))]))

    def get_events_pk_list(self):
        """
        Возвращает список всех курсов, студентом которых человек является
        :return:
        """
        return list(set([ev.id for ev in Event.objects.filter(Q(listeners__id=self.id) | Q(supervisors__id=self.id))]))
