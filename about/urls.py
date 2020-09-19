from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from .views import AboutViewSet, DeveloperViewSet

router = routers.DefaultRouter()
router.register('about', DeveloperViewSet)
router.register('about', AboutViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
