from django.db import models

from people.models import Person


class Department(models.Model):
    name = models.CharField(verbose_name='Название')
    descr = models.TextField(verbose_name='Описание')
    id_supervisor = models.ForeignKey('people.Person', verbose_name='Руководитель', on_delete=models.SET_NULL,
                                      blank=True, null=True)

    class Meta:
        ordering = '-name',
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.name

    def get_fields(self):
        dct = dict()

        fields = ['name', 'descr']
        for field in fields:
            dct[self._meta.get_field(field).verbose_name] = getattr(self, field)
        return dct

    def get_activists_list(self):
        """
        Возвращает список активистов отдела
        :return:
        """
        # result = list()
        # for pn in Person.objects.all():
        #     if self in pn.get_departments_list():
        #         result.append(pn)
        # return result
        return Person.objects.filter(departments__name=self.name)
