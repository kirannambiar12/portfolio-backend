from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from work.models import Technology
from work.serializers import TechnologySerializer


class TechnologyViewSet(viewsets.ModelViewSet):
    serializer_class = TechnologySerializer
    queryset = Technology.objects.all()
    permission_classes = [permissions.AllowAny]