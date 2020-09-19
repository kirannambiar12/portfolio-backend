from rest_framework import viewsets, permissions
from .serializers import ContactSerializer
from .models import Contact


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [permissions.AllowAny]
