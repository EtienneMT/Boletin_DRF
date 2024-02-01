from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Marca, Vehiculo
from .serializers import MarcaSerializer, VehiculoSerializer
from .permissions import ReadOnlyPermission

# Create your views here.


class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = [ReadOnlyPermission]
    filter_backends = [DjangoFilterBackend]


class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [ReadOnlyPermission]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['marca', 'modelo', 'color']
    ordering_fields = ['fecha_fabricacion']

