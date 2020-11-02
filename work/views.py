from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from work.models import Service, TechnologiesAndFramework
from work.serializers import ServiceSerializer, TechnologiesAndFrameworkSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    permission_classes = [permissions.AllowAny]


class TechnologiesAndFrameworkViewSet(viewsets.ModelViewSet):
    serializer_class = TechnologiesAndFrameworkSerializer
    queryset = TechnologiesAndFramework.objects.all()
    permission_classes = [permissions.AllowAny]