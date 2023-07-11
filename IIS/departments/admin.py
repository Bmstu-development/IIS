from simple_history.admin import SimpleHistoryAdmin

from django.contrib import admin

from .models import Department

admin.site.register(Department, SimpleHistoryAdmin)
