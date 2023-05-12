from django.db import models
from django.utils import timezone

# Create your models here.


class task(models.Model):
    title = models.CharField(max_length=255)
    cheked = models.BooleanField(default=False)
    add_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
