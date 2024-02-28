from django.contrib import admin
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/vi/shcema/', SpectacularAPIView.as_view(),name='schema'),
    path('api/vi/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'),name='swagger-ui'),
    path('api/vi/redoc/', SpectacularRedocView.as_view(url_name='schema'),name='redoc'),
    path('api/vi/videos/', SpectacularRedocView.as_view(url_name='schema'),name='redoc'),
]
