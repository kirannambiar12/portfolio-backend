from django.db import models

# Create your models here.


class Service(models.Model):
    title = models.CharField(blank=False, null=False, max_length=256)
    description = models.CharField(blank=False, null=False, max_length=256)

    def __str__(self):
        return self.title

class TechnologiesAndFramework(models.Model):
    title = models.CharField(blank=False, null=False, max_length=256)
    description = models.CharField(blank=False, null=False, max_length=256)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, related_name='technologies')

    def __str__(self):
        return self.title
