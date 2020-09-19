from rest_framework import serializers
from .models import About, Developer


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ('id', 'title', 'about_developer_text', 'developer_background_img')


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'title', 'about_text', 'about_img')




