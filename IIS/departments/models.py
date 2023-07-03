from django.db import models


class Department(models.Model):
    name = models.TextField(verbose_name='Название', blank=True, null=False)
    descr = models.TextField(verbose_name='Описание', blank=True, null=False)
    id_supervisor = models.ForeignKey('people.Person', verbose_name='Руководитель', on_delete=models.SET_NULL,
                                      blank=True, null=True)

    class Meta:
        ordering = ''
        verbose_name = 'Отедел'
        verbose_name_plural = 'Отеделы'
