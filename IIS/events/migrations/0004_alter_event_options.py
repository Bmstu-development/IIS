# Generated by Django 4.2.2 on 2023-07-09 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_initial_squashed_0003_rename_id_supervisor_event_supervisors_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('dt_start', 'name'), 'verbose_name': 'Событие', 'verbose_name_plural': 'События'},
        ),
    ]