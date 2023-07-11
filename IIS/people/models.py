from simple_history.models import HistoricalRecords

from django.db import models
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.models import User

from departments.models import Department
from events.models import Event
from utils.converters import latinize
from utils.generators import generate_password


class PersonManager(models.Manager):
    """

    """
    def for_user(self, user, view_only=False):
        if view_only:
            return self.get_queryset()
        return self.get_queryset().filter()


class Person(models.Model):
    surname = models.CharField(verbose_name='Фамилия')
    name = models.CharField(verbose_name='Имя')
    patronymic = models.CharField(verbose_name='Отчество', blank=True, null=True)
    organisation = models.CharField(verbose_name='Организация')
    bmstu_group = models.CharField(verbose_name='Учебная группа (МГТУ)', blank=True, null=True)
    phone_number = models.CharField(verbose_name='Телефонный номер', blank=True, null=False)
    tg_username = models.CharField(verbose_name='Тег в телеграме', blank=True, null=False)
    is_user = models.BooleanField(verbose_name='Является ли пользователем', default=False)
    user_instance = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ID пользователя',
                                      on_delete=models.SET_NULL, blank=True, null=True)
    history = HistoricalRecords()  # Person.objects.get(id=1).history.all().first().history_date / ...history_user

    objects = PersonManager()

    class Meta:
        ordering = 'surname', 'name', 'patronymic',
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic if self.patronymic else ""}'

    def get_fields(self):
        dct = dict()

        fields = ['surname', 'name', 'patronymic', 'organisation', 'bmstu_group', 'phone_number', 'tg_username',
                  'is_user']
        for field in fields:
            dct[self._meta.get_field(field).verbose_name] = getattr(self, field)
        return dct

    def get_departments_pk_list(self):
        """
        Возвращает список всех отделов, куда человек входит
        :return:
        """
        return list(set([dp.id for dp in Department.objects.filter(Q(activists__id=self.id) | Q(supervisor_instance=self))]))

    def get_events_pk_list(self):
        """
        Возвращает список всех курсов, студентом которых человек является
        :return:
        """
        return list(set([ev.id for ev in Event.objects.filter(Q(listeners__id=self.id) | Q(supervisors__id=self.id))]))

    def make_user(self):
        """
        Создает из персоны self пользователя. Автоматически генерирует логин и пароль, выполняет объекта пользователя
        к модели персоны self через внешний ключ
        :return:
        Пароль нового пользователя
        """
        if self.is_user:
            raise ValueError(f'Person pk={self.id} is already user')

        username = latinize(f'{self.surname}_{self.name}')
        password = generate_password(15)
        i = 0
        try:
            while True:
                User.objects.get(username=username + (f'_{str(i)}' if i else ''))
                i += 1
        except User.DoesNotExist:
            new_user = User.objects.create_user(username=username + (f'_{str(i)}' if i else str()), password=password)
            new_user.first_name = self.name
            new_user.last_name = self.surname
            new_user.save()
        self.user_instance = new_user
        self.is_user = True
        self.save()
        return password

    def delete_user(self):
        """
        Удаляет пользователя, связанного с персоной self
        :return:
        """
        if not self.is_user:
            raise ValueError(f'Person pk={self.id} is not user')

        self.user_instance.delete()
        self.user_instance = None
        self.is_user = False
        self.save()
