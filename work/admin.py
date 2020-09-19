from django.contrib import admin

# Register your models here.
from work.models import Technology


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'percentage', 'bar_color')


admin.site.register(Technology, TechnologyAdmin)
