from rest_framework import serializers, permissions

from .models import Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('id', 'name', 'email_id', 'subject')
