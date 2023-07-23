from django.forms.widgets import Widget, CheckboxSelectMultiple
from django.template import loader
from django.utils.safestring import mark_safe


class DepartmentActivistsChoiceWidget(Widget):
    template_name = 'departments/activists_widget.html'

    # def __init__(self, attrs=None, queryset=None):
    #     super().__init__(attrs)
    #     self.queryset = queryset

    def get_context(self, name, value, attrs=None):
        context = super().get_context(name, value, attrs)
        return context

    def render(self, name, value, attrs=None, renderer=None):
        print(self)
        print(name)
        print(value)
        print(attrs)
        print(renderer)
        context = self.get_context(name, value, attrs)
        template = loader.get_template(self.template_name).render(context)
        return mark_safe(template)

    # def value_from_datadict(self, data, files, name):
    #     print(data)
    #     print(files)
    #     print(name)
    #     return []
