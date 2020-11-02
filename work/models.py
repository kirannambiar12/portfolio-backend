from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Service(models.Model):
    title = models.CharField(blank=False, null=False, max_length=256)
    description = RichTextUploadingField()

    def __str__(self):
        return self.title

class TechnologiesAndFramework(models.Model):
    title = models.CharField(blank=False, null=False, max_length=256)
    description = RichTextUploadingField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, related_name='technologies')

    def __str__(self):
        return self.title
