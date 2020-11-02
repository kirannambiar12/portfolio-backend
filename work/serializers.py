from rest_framework import serializers
from work.models import Service, TechnologiesAndFramework


class TechnologiesAndFrameworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologiesAndFramework
        fields = ('id', 'title', 'description')

class ServiceSerializer(serializers.ModelSerializer):

    technologies = TechnologiesAndFrameworkSerializer(read_only=True, many=True)
    class Meta:
        model = Service
        fields = ('id', 'title', 'description', 'technologies')
