from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from .views import ServiceViewSet, TechnologiesAndFrameworkViewSet

router = routers.DefaultRouter()
router.register('work/service', ServiceViewSet)
router.register('work/t&f', TechnologiesAndFrameworkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
