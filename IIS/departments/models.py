from simple_history.models import HistoricalRecords

from django.db import models


class Department(models.Model):
    name = models.CharField(verbose_name='Название')
    descr = models.TextField(verbose_name='Описание')
    id_supervisor = models.ForeignKey('people.Person', verbose_name='Руководитель', on_delete=models.SET_NULL,
                                      blank=True, null=True)
    activists = models.ManyToManyField('people.Person', verbose_name='Активисты',
                                       related_name='department_activists_match', blank=True)
    history = HistoricalRecords()

    class Meta:
        ordering = 'name',
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.name

    def get_fields(self):
        dct = dict()

        fields = ['name', 'descr']
        for field in fields:
            dct[self._meta.get_field(field).verbose_name] = getattr(self, field)
        dct[self._meta.get_field('id_supervisor').verbose_name] = str(
            self.id_supervisor) if self.id_supervisor else 'Не указан'
        return dct

    def get_activists_list(self):
        """
        Возвращает список активистов отдела
        :return:
        """
        return self.activists.all()
