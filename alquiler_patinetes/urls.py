from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework import routers
from .views import UsuarioViewSet, PatineteViewSet, AlquilerViewSet

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'patinetes', PatineteViewSet)
router.register(r'alquileres', AlquilerViewSet)

router.register(r'alquilar', AlquilerViewSet, basename='alquilar')
router.register(r'liberar', AlquilerViewSet, basename='liberar')

router.register(r'alquileres_admin', AlquilerViewSet, basename='alquileres_admin')
router.register(r'alquileres_usuario', AlquilerViewSet, basename='alquileres_usuario')

router.register(r'patinetes_libres', PatineteViewSet, basename='patinetes_libres')
router.register(r'patinetes_ocupados', PatineteViewSet, basename='patinetes_ocupados')

router.register(r'usuarios_por_debito', UsuarioViewSet, basename='usuarios_por_debito')

router.register(r'top_ten_patinetes_alquilados', PatineteViewSet, basename='top_ten_patinetes_alquilados')
router.register(r'top_tres_usuarios_alquileres', UsuarioViewSet, basename='top_tres_usuarios_alquileres')


urlpatterns = [
    path('', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
