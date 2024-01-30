from rest_framework import viewsets
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


class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [ReadOnlyPermission]

    @action(detail=False, methods=['GET'])
    def listar_por_marca(self, request):
        nombre_marca = request.query_params.get('marca', None)
        if nombre_marca:
            try:
                marca = Marca.objects.get(nombre=nombre_marca)
                vehiculos = self.queryset.filter(marca=marca)
                serializer = self.get_serializer(vehiculos, many=True)
                return Response(serializer.data)
            except Marca.DoesNotExist:
                return Response({'error': 'La marca especificada no existe'}, status=400)
        else:
            return Response({'error': 'Parámetro de marca requerido'}, status=400)
