from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(blank=False, null=False, max_length=256)
    about_text = models.TextField(blank=False, null=False)
    about_img = models.ImageField(blank=False, null=False)

    def __str__(self):
        return self.title


class Developer(models.Model):
    title = models.CharField(blank=False, null=False, max_length=256)
    about_developer_text = models.TextField(blank=False, null=False)
    developer_background_img = models.ImageField(blank=True, null=False)

    def __str__(self):
        return self.title

