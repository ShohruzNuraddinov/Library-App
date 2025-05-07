from django.urls import path
from rest_framework import permissions

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

swagger_urlpatterns = [
    path('swagger-file/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('swagger/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
