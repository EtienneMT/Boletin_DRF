from django.urls import path, include
from rest_framework import routers
from .views import VehiculoViewSet, MarcaViewSet

router = routers.DefaultRouter()
router.register(r'vehiculos', VehiculoViewSet)
router.register(r'marcas', MarcaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
