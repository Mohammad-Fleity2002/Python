from django.contrib import admin
from .models import Passwords


class PasswordAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password',
                    'description', 'create_Date')
# Register your models here.


admin.site.register(Passwords, PasswordAdmin)
