from django import forms

from . import models


class DepartmentAddForm(forms.ModelForm):
    def save(self, commit=True):
        # после нажатия на кнопку создания открыть модальной окно "вы уверены, ..., активистам будут выданы такие
        # права, руководителю - такие", также создать пользователя руководителю
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance

    class Meta:
        model = models.Department
        fields = 'name', 'descr', 'permissions', 'supervisor_instance', 'activists'
