from simple_history.admin import SimpleHistoryAdmin

from django.contrib import admin

from .models import Event

admin.site.register(Event, SimpleHistoryAdmin)
