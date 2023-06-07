from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Contacts(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = PhoneNumberField()
    description = models.CharField(max_length=610)
    create_date = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return f"username:  {self.full_name} pass: {self.phone_number} desc: {self.description}"
