from rest_framework import serializers
from work.models import Service, TechnologiesAndFramework


class ServiceSerializer(serializers.ModelSerializer):
    
    technologies = serializers.SlugRelatedField(read_only=True, many=True, slug_field="title")
    class Meta:
        model = Service
        fields = ('id', 'title', 'description', 'technologies')


class TechnologiesAndFrameworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologiesAndFramework
        fields = ('id', 'title', 'description')