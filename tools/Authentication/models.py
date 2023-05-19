from django.db import models
from django.utils import timezone

# Create your models here.


class Users(models.Model):
    user_name = models.CharField(max_length=255)
    user_password = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    user_join_date = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return f"Name: {self.user_name}, Email: {self.user_email}, Join Date: {self.user_join_date}."
