from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework import routers
from .views import UsuarioViewSet, PatineteViewSet, AlquilerViewSet

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'patinetes', PatineteViewSet)
router.register(r'alquileres', AlquilerViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
