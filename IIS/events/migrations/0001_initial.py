# Generated by Django 4.2.2 on 2023-07-03 09:00

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Название')),
                ('descr', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('dt_start', models.DateField(blank=True, null=True, verbose_name='Дата начала')),
                ('dt_finish', models.DateField(blank=True, null=True, verbose_name='Дата конца')),
                ('t_start', models.TimeField(blank=True, null=True, verbose_name='Время начала')),
                ('t_finish', models.TimeField(blank=True, null=True, verbose_name='Время конца')),
                ('frequently', models.IntegerField(blank=True, null=True, verbose_name='Частота занятий')),
                ('audience_num', models.CharField(blank=True, null=True, verbose_name='Номер аудитории')),
                ('status', models.IntegerField(default=0, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
                'ordering': ('-dt_start', '-name'),
            },
        ),
    ]
