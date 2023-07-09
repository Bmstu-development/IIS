from rest_framework import serializers

from . import models


class PersonSerializer(serializers.ModelSerializer):
    fields_descr = {
        'id': 'ID человека',
        'surname': 'Фамилия (строка)',
        'name': 'Имя (строка)',
        'patronymic': 'Отчество (если есть) (строка)',
        'organisation': 'Организация (строка',
        'bmstu_group': 'Учебная группа (если студент МГТУ) (строка)',
        'phone_number': 'Телефонный номер (строка)',
        'tg_username': 'Тег в телеграме (строка)',
        'departments': 'Список ID отделов Искры, в которые человек входит (список)',
        'events': 'Список мероприятий Искры, слушателем который человек является (список)',
    }

    class Meta:
        model = models.Person
        fields = '__all__'
