from rest_framework import serializers

from . import models


class PersonSerializer(serializers.ModelSerializer):
    events = serializers.SerializerMethodField('get_events')
    departments = serializers.SerializerMethodField('get_departments')

    def get_events(self, instance):
        return instance.get_events_pk_list()

    def get_departments(self, instance):
        return instance.get_departments_pk_list()

    class Meta:
        model = models.Person
        fields = 'id', 'surname', 'name', 'patronymic', 'events', 'departments', \
            'organisation', 'bmstu_group', 'phone_number', 'tg_username', 'events', 'departments'
