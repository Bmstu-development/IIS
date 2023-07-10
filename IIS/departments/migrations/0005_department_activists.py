# Generated by Django 4.2.2 on 2023-07-10 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_remove_person_departments_remove_person_events'),
        ('departments', '0004_alter_department_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='activists',
            field=models.ManyToManyField(blank=True, related_name='department_activists_match', to='people.person', verbose_name='Активисты'),
        ),
    ]