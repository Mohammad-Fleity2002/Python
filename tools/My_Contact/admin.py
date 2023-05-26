from django.contrib import admin
from .models import Contacts


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number',
                    'description', 'create_date')
admin.site.register(Contacts, ContactAdmin)
