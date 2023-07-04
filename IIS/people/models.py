from django.db import models


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
    departments = models.ManyToManyField('departments.Department', verbose_name='Отдел',
                                         related_name='person_department_match', blank=True, default=list())
    events = models.ManyToManyField('events.Event', verbose_name='Курс', related_name='person_event_match', blank=True,
                                    default=list())

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    def get_departments_list(self):
        """
        Возвращает список всех отделов, куда человек входит
        :return:
        """
        return self.departments.all()

    def get_departments_supervisor_list(self):
        """
        Возвращает список всех отделов, руководителем которых человек является
        :return:
        """
        return [dp for dp in self.departments.all() if dp.id_supervisor == self]

    def get_events_teacher_list(self):
        """
        Возвращает список всех курсов, преподавателем которых человек является
        :return:
        """
        return [ev for ev in self.events.all() if ev.id_teacher == self]

    def get_events_list(self):
        """
        Возвращает список всех курсов, студентом которых человек является
        :return:
        """
        return self.events.all()

    class Meta:
        ordering = '-surname', '-name', '-patronymic',
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
