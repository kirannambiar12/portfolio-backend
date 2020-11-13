from django.db import models
from django.utils import timezone, dateformat


class Contact(models.Model):
    name = models.CharField(blank=False, null=False, max_length=256)
    email_id = models.CharField(blank=False, null=False, max_length=256)
    subject = models.TextField(blank=False, null=False)
    date = dateformat.format(timezone.now(), 'Y-m-d H:i:s')

    def __str__(self):
        return self.name
