from simple_history.models import HistoricalRecords

from django.db import models
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.models import User, Group

from datetime import timezone

from departments.models import Department
from events.models import Event
from utils.converters import latinize
from utils.generators import generate_password


class PersonManager(models.Manager):
    """
    Класс-менеджер класса Person
    """

    def for_user(self, user, view_only=False):
        """
        Метод определения query_set в зависимости от намерений и прав пользователя user
        :param user: инициатор вызова query_set
        :param view_only: флаг - только чтение или изменение
        :return: query_set объектов класса Person доступных user
        """
        if view_only or user.is_superuser:
            # для просмотра доступны все
            # администратору доступны все
            return self.get_queryset()
        is_crud = Department.CRUD in user.groups.all().values_list('name', flat=True)
        subordinates_pk_list = user.get_subordinates_pk_list()
        if is_crud and subordinates_pk_list:
            # пользователям с CRUD правом, которые руководители, доступны все, кроме пользователей из других отделов
            return self.get_queryset().exclude(Q(is_user=True) & ~Q(id__in=subordinates_pk_list))
        if is_crud:
            # пользователям с CRUD правом, которые НЕруководители, доступны все НЕпользователи
            return self.get_queryset().filter(is_user=False)
        if subordinates_pk_list:
            # пользователям без CRUD права, которые руководители, доступны свои активисты
            return self.get_queryset().filter(id__in=subordinates_pk_list)
        # пользователям без CRUD права, которые НЕруководители, недоступно ничего
        return Person.objects.none()


class Person(models.Model):
    surname = models.CharField(verbose_name='Фамилия')
    name = models.CharField(verbose_name='Имя')
    patronymic = models.CharField(verbose_name='Отчество', blank=True, null=True)
    organisation = models.CharField(verbose_name='Организация')
    bmstu_group = models.CharField(verbose_name='Учебная группа (МГТУ)', blank=True, null=False)
    phone_number = models.CharField(verbose_name='Телефонный номер', blank=True, null=False)
    tg_username = models.CharField(verbose_name='Тег в телеграме', blank=True, null=False)
    is_user = models.BooleanField(verbose_name='Является ли пользователем', default=False)
    user_instance = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ID пользователя',
                                      on_delete=models.SET_NULL, blank=True, null=True)
    history = HistoricalRecords()

    objects = PersonManager()

    class Meta:
        ordering = 'surname', 'name', 'patronymic',
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic if self.patronymic else ""}'

    def get_fields(self):
        """

        :return:
        """
        dct = dict()

        fields = ['surname', 'name', 'patronymic', 'organisation', 'bmstu_group', 'phone_number', 'tg_username',
                  'is_user']
        fields_to_hide_if_none = ['bmstu_group']
        fields_to_replace_if_none = {
            'patronymic': 'Без отчества',
            'phone_number': 'Не указан',
            'tg_username': 'Не указан',
        }
        fields_boolean = ['is_user']
        for field in fields:
            field_value = getattr(self, field)
            if field in fields_to_hide_if_none and not field_value:
                continue
            if field in fields_to_replace_if_none and not field_value:
                field_value = fields_to_replace_if_none[field]
            if field in fields_boolean:
                field_value = 'Да' if field_value else 'Нет'
            dct[self._meta.get_field(field).verbose_name] = field_value
        return dct

    def get_departments_list(self):
        """
        Возвращает список отделов, в которые активистом или руководителем входит self
        :return: List объектов класса Department
        """
        result = list()
        for dp in Department.objects.all():
            if dp.supervisor_instance == self or self in dp.activists.all():
                result.append(dp)
        return result

    def get_departments_pk_list(self):
        """
        Возвращает список pk отделов, в которые активистом или руководителем входит self
        :return: List pk объектов класса Department
        """
        return [dp.id for dp in self.get_departments_list()]

    def get_subordinate_departments_list(self):
        """
        Возвращает список отделов, в которые руководителем входит self
        :return: List объектов класса Department
        """
        return [dp for dp in self.get_departments_list() if dp.supervisor_instance == self]

    def get_events_list(self):
        """
        Возвращает список мероприятий, к которым старостой, преподавателем или слушателем относится self
        :return: List объектов класса Event
        """
        result = list()
        for ev in Event.objects.all():
            if self in ev.teachers.all() or self in ev.supervisors.all() or self in ev.listeners.all():
                result.append(ev)
        return result

    def get_events_pk_list(self):
        """
        Возвращает список pk мероприятий, к которым старостой, преподавателем или слушателем относится self
        :return: List pk объектов класса Event
        """
        return [ev.id for ev in self.get_events_list()]

    def get_subordinates_pk_list(self):
        """
        Возвращает список pk людей, которые входят в отдел(ы) под руководством self
        :return: List pk объектов класса Person
        """
        # TODO: OPTIMIZE
        result = set()
        for dp in self.get_subordinate_departments_list():
            result = result.union(set(dp.activists.all().values_list(flat=True)))
        return list(result)

    def is_supervisor(self):
        """
        Возвращает T/F в зависимости от того, является ли self руководителем какого-то отдела
        :return: T/F
        """
        for dp in Department.objects.all():
            if dp.supervisor_instance == self:
                return True
        return False

    def make_user(self):
        """
        Создает из персоны self пользователя. Автоматически генерирует логин и пароль, выполняет объекта пользователя
        к модели персоны self через внешний ключ
        :return: Пароль нового пользователя
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

        for dp in self.get_departments_list():
            if dp.permissions == Department.NONE:
                continue
            Group.objects.get(name=dp.permissions).user_set.add(new_user)

        self.user_instance = new_user
        self.is_user = True
        self.save()
        return password

    def delete_user(self):
        """
        Удаляет пользователя, связанного с персоной self
        :return: None
        """
        if not self.is_user:
            raise ValueError(f'Person pk={self.id} is not user')

        self.user_instance.delete()
        self.user_instance = None
        self.is_user = False
        self.save()

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
