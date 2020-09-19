from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from .views import ContactViewSet

router = routers.DefaultRouter()
router.register('contact', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
