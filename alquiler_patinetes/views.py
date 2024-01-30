from rest_framework import viewsets

from .models import Usuario, Alquiler, Patinete
from .serializers import UsuarioSerializer, AlquilerSerializer, PatineteSerializer


# Create your views here.
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class AlquilerViewSet(viewsets.ModelViewSet):
    queryset = Alquiler.objects.all()
    serializer_class = AlquilerSerializer


class PatineteViewSet(viewsets.ModelViewSet):
    queryset = Patinete.objects.all()
    serializer_class = PatineteSerializer
