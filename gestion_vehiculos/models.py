from django.db import models

# Create your models here.
TIPO_CHOICES = [
    ('Coche', 'Coche'),
    ('Ciclomotor', 'Ciclomotor'),
    ('Motocicleta', 'Motocicleta'),
]

COLOR_CHOICES = [
    ('Rojo', 'Rojo'),
    ('Azul', 'Azul'),
    ('Verde', 'Verde'),
]


class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"


class Vehiculo(models.Model):
    tipo_vehiculo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    chasis = models.CharField(max_length=50, unique=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=50)
    matricula = models.CharField(max_length=20, unique=True)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    fecha_fabricacion = models.DateField()
    fecha_matriculacion = models.DateField()
    fecha_baja = models.DateField(null=True, blank=True)
    suspendido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.tipo_vehiculo} - {self.matricula}"
