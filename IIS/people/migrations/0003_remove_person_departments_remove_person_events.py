# Generated by Django 4.2.2 on 2023-07-10 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_alter_person_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='departments',
        ),
        migrations.RemoveField(
            model_name='person',
            name='events',
        ),
    ]