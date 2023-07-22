from django import forms
from django.contrib.auth.models import Group

from . import models


class DepartmentAddForm(forms.ModelForm):
    name = forms.CharField(
        label='Название',
        help_text='Введенное название будет считаться официальным названием отдела',
        strip=True,
        widget=forms.TextInput(attrs={
            'placeholder': ''
        })
    )

    descr = forms.CharField(
        label='Описание',
        help_text='Введенное описание будет считаться официальным описанием отдела',
        strip=True,
        widget=forms.Textarea(attrs={
            'placeholder': ''
        })
    )

    # activists = forms.ModelForm(
    # )

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            self.save_m2m()
            for pn in instance.activists.all():
                if pn.user_instance is None:
                    continue
                Group.objects.get(name=instance.permissions).user_set.add(pn.user_instance)
            # TODO: call modal form to offer create new users
        return instance

    class Meta:
        model = models.Department
        fields = 'name', 'descr', 'permissions', 'supervisor_instance', 'activists'
        widgets = {
            'descr': forms.Textarea(attrs={
                'placeholder': '',
            }),
        }
