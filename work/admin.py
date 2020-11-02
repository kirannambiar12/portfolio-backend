from django.contrib import admin

# Register your models here.
from work.models import Service, TechnologiesAndFramework


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Service, ServiceAdmin)
admin.site.register(TechnologiesAndFramework)
