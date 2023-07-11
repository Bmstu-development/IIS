from simple_history.admin import SimpleHistoryAdmin

from django.contrib import admin

from .models import Person

admin.site.register(Person, SimpleHistoryAdmin)
