from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from .views import TechnologyViewSet

router = routers.DefaultRouter()
router.register('work', TechnologyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
