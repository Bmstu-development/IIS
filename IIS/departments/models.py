from simple_history.models import HistoricalRecords

from django.db import models


class DepartmentManager(models.Manager):
    """

    """

    def for_user(self, user, view_only=False):
        """

        :param user:
        :param view_only:
        :return:
        """
        if view_only or user.is_superuser:
            # для просмотра доступны все
            # администратору доступны все
            return self.get_queryset()
        # руководителю отдела доступно редактирование
        return self.get_queryset().filter(supervisor_instance=user)


class Department(models.Model):
    CRUD = 'crud'
    READONLY = 'readonly'
    NONE = 'none'
    PERMISSION_CHOICES = (
        (CRUD, 'Чтение, изменение, добавление'),
        (READONLY, 'Только чтение'),
        (NONE, 'Нет прав'),
    )

    name = models.CharField(verbose_name='Название')
    descr = models.TextField(verbose_name='Описание')
    supervisor_instance = models.ForeignKey('people.Person', verbose_name='Руководитель', on_delete=models.SET_NULL,
                                            blank=True, null=True)
    activists = models.ManyToManyField('people.Person', verbose_name='Активисты',
                                       related_name='department_activists_match', blank=True)
    permissions = models.CharField(verbose_name='Уровень доступа', choices=PERMISSION_CHOICES, default=NONE)
    history = HistoricalRecords()

    objects = DepartmentManager()

    class Meta:
        ordering = 'name',
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.name

    def get_fields(self):
        """

        :return:
        """
        dct = dict()

        fields = ['name', 'descr']
        for field in fields:
            dct[self._meta.get_field(field).verbose_name] = getattr(self, field)
        dct[self._meta.get_field('supervisor_instance').verbose_name] = str(
            self.supervisor_instance) if self.supervisor_instance else 'Не указан'
        return dct

    def get_activists_list(self):
        """
        Возвращает список активистов отдела
        :return:
        """
        return self.activists.all()
