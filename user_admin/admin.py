from django.contrib import admin

from .models import WorkDay, Projects, WorkOnProject

admin.site.register(WorkDay)
admin.site.register(Projects)
admin.site.register(WorkOnProject)
