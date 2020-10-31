from rest_framework import serializers
from work.models import Service, TechnologiesAndFramework


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'title')


class TechnologiesAndFrameworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologiesAndFramework
        fields = ('id', 'title')