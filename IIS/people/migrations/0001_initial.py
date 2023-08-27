# Generated by Django 4.2.2 on 2023-07-03 09:00

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('departments', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(verbose_name='Фамилия')),
                ('name', models.CharField(verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, null=True, verbose_name='Отчество')),
                ('organisation', models.CharField(verbose_name='Организация')),
                ('bmstu_group', models.CharField(blank=True, null=False, verbose_name='Учебная группа (МГТУ)')),
                ('phone_number', models.CharField(blank=True, verbose_name='Телефонный номер')),
                ('tg_username', models.CharField(blank=True, verbose_name='Тег в телеграме')),
                ('departments', models.ManyToManyField(blank=True, default=[], related_name='person_department_match',
                                                       to='departments.department', verbose_name='Отдел')),
                ('events',
                 models.ManyToManyField(blank=True, default=[], related_name='person_event_match', to='events.event',
                                        verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Человек',
                'verbose_name_plural': 'Люди',
                'ordering': ('-surname', '-name', '-patronymic'),
            },
        ),
    ]
