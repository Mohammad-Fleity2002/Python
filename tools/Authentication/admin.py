from django.contrib import admin

from .models import Users


class UsersAdmin(admin.ModelAdmin):
    exclude = ('user_join_date',)
    list_display = ('id', 'user_name', 'user_email',
                    'user_join_date')


admin.site.register(Users, UsersAdmin)
