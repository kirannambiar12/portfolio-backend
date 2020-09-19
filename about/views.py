from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .serializers import AboutSerializer, DeveloperSerializer
from .models import About, Developer


class DeveloperViewSet(viewsets.ModelViewSet):
    serializer_class = DeveloperSerializer
    queryset = Developer.objects.all()
    permission_classes = [permissions.AllowAny]


class AboutViewSet(viewsets.ModelViewSet):
    serializer_class = AboutSerializer
    queryset = About.objects.all()
    permission_classes = [permissions.AllowAny]




