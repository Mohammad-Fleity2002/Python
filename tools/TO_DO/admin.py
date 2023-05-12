from django.contrib import admin
from .models import task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'add_date', 'cheked')
# Register your models here.


admin.site.register(task, TaskAdmin)
