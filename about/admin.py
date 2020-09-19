from django.contrib import admin

# Register your models here.
from django.contrib import admin

from django.contrib import admin
from .models import About, Developer


class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(About, AboutAdmin)
