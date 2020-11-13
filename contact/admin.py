from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email_id', 'subject', 'date')
    list_display = ('name', 'email_id',)


admin.site.register(Contact, ContactAdmin)
