from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from rest_framework import routers
from contact import views as contact_views
from about import views as about_views
from django.conf.urls.static import static
from django.conf import settings
from work import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'contact', contact_views.ContactViewSet, 'contact')
router.register(r'about/developer', about_views.DeveloperViewSet, 'developer')
router.register(r'about', about_views.AboutViewSet, 'about')
router.register(r'work/f&t', views.TechnologiesAndFrameworkViewSet, 'f&t')
router.register(r'work/service', views.ServiceViewSet, 'service' )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', obtain_auth_token),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
