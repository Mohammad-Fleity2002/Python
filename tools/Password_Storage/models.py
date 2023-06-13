from django.db import models
from django.utils import timezone


class Passwords(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    description = models.CharField(max_length=610)
    create_Date = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return f"username:  {self.username} pass: {self.password} desc: {self.description}"
