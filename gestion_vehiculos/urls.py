from django.urls import path, include
from rest_framework import routers
from .views import VehiculoViewSet, MarcaViewSet

router = routers.DefaultRouter()
router.register(r'vehiculos', VehiculoViewSet)
router.register(r'marcas', MarcaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('listado_marca/', VehiculoViewSet.as_view({'get': 'listar_por_marca'}), name='listar-marca'),
]
