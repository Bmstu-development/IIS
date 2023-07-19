from django import forms

from . import models


class PersonAddForm(forms.ModelForm):
    no_patronymic = forms.BooleanField(label='Без отчества', initial=False, required=False)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance

    class Meta:
        model = models.Person
        fields = 'surname', 'name', 'patronymic', 'organisation', 'bmstu_group', 'phone_number', 'tg_username', \
            'is_user'
        # widgets = {
        #     'surname': forms.TextInput(attrs={
        #         'class': 'w-25',
        #         'placeholder': '',
        #     }),
        #     'name': forms.TextInput(attrs={
        #         'class': 'w-25',
        #         'placeholder': '',
        #     }),
        #     'patronymic': forms.TextInput(attrs={
        #         'class': 'w-25',
        #         'placeholder': '',
        #     }),
        #     'organisation': forms.TextInput(attrs={
        #         'class': 'w-25',
        #         'placeholder': '',
        #     }),
        #     'bmstu_group': forms.TextInput(attrs={
        #         'class': 'w-25',
        #         'placeholder': '',
        #     }),
        #     'phone_number': forms.TextInput(attrs={
        #         'class': 'w-25',
        #         'placeholder': '',
        #     }),
        #     'tg_username': forms.TextInput(attrs={
        #         'class': 'w-25',
        #         'placeholder': '',
        #     }),
        #     'is_user': forms.BooleanField(attrs={
        #
        #     })
        # }
