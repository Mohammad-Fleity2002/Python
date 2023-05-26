from django.contrib import admin
from .models import Passwords


class PasswordAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password',
                    'description', 'create_Date')

admin.site.register(Passwords, PasswordAdmin)
