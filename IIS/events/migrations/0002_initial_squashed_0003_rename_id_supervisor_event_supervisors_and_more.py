# Generated by Django 4.2.2 on 2023-07-06 00:09

from django.db import migrations, models


class Migration(migrations.Migration):
    replaces = [('events', '0002_initial'), ('events', '0003_rename_id_supervisor_event_supervisors_and_more')]

    dependencies = [
        ('events', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='supervisors',
            field=models.ManyToManyField(blank=True, related_name='event_supervisor_match', to='people.person',
                                         verbose_name='Староста'),
        ),
        migrations.AddField(
            model_name='event',
            name='teachers',
            field=models.ManyToManyField(blank=True, related_name='event_teacher_match', to='people.person',
                                         verbose_name='Преподаватель'),
        ),
    ]
