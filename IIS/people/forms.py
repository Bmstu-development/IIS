from django import forms

from . import models
from events.models import Event
from departments.models import Department


class PersonAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.events = Event.objects.all()
        self.departments = Department.objects.all()

    surname = forms.CharField(
        label='Фамилия',
        help_text='Фамилия в соответствии с указанной в паспорте',
        strip=True,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': ''
        }),
    )

    name = forms.CharField(
        label='Имя',
        help_text='Фамилия в соответствии с указанной в паспорте',
        strip=True,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': ''
        }),
    )

    patronymic = forms.CharField(
        label='Отчество',
        help_text='Отчество в соответствии с указанным в паспорте',
        strip=True,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': ''
        }),
    )

    no_patronymic = forms.BooleanField(
        label='Без отчества',
        initial=False,
        required=False,
    )

    organisation = forms.CharField(
        label='Организация',
        help_text='Организация, учеником или сотрудником которой человек является',
        strip=True,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': ''
        }),
    )

    bmstu_group = forms.CharField(
        label='Учебная группа',
        help_text='Учебная группа студента МГТУ',
        strip=True,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': ''
        }),
    )

    phone_number = forms.CharField(
        label='Телефонный номер',
        help_text='Формат: +7 (ххх) ххх-хх-хх',
        strip=True,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': ''
        }),
    )

    no_phone_number = forms.BooleanField(
        label='Номер телефона не указан',
        initial=False,
        required=False,
    )

    tg_username = forms.CharField(
        label='Тег в телеграме',
        help_text='Формат: @username',
        strip=True,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': ''
        }),
    )

    no_tg_username = forms.BooleanField(
        label='Тег в телеграме не указан',
        initial=False,
        required=False,
    )

    is_user = forms.BooleanField(
        label='Сделать пользователем',
        initial=False,
        required=False,
    )

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance

    class Meta:
        model = models.Person
        fields = 'surname', 'name', 'patronymic', 'organisation', 'bmstu_group', 'phone_number', 'tg_username', \
            'is_user'
