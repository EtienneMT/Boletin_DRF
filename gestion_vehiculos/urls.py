from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework import routers
from .views import VehiculoViewSet, MarcaViewSet

router = routers.DefaultRouter()
router.register(r'vehiculos', VehiculoViewSet)
router.register(r'marcas', MarcaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('listado_marca/', VehiculoViewSet.as_view({'get': 'listar_por_marca'}), name='listar-marca'),
]
