from django.db import models

# Create your models here.


class Technology(models.Model):
    COLOR_CHOICES = (
        ("success", "success"),
        ("danger", "danger"),
        ("warning", "warning"),
        ("info", "info"),
    )
    title = models.CharField(blank=False, null=False, max_length=256)
    percentage = models.IntegerField(blank=False, null=False)
    bar_color = models.CharField(blank=False, null=False, max_length=100, choices=COLOR_CHOICES)

    def __str__(self):
        return self.title
