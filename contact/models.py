from django.db import models


class Contact(models.Model):
    name = models.CharField(blank=False, null=False, max_length=256)
    email_id = models.CharField(blank=False, null=False, max_length=256)
    subject = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name
