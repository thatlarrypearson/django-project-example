# server/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    path('file_system_searcher/', include('django_fs_searcher.urls')),
    path('lightroom_loader/', include('django_lr_loader.urls')),
#     path('ios_sensor_pack/', include('ios_sensor_pack.urls')),
#     path('obd_sensor_pack/', include('obd_sensor_pack.urls')),
]
