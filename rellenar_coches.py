import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "boletin_rest_EtienneMT.settings")
django.setup()

from gestion_vehiculos.models import Marca, Vehiculo
from datetime import date


def llenar_modelos():
    # Crear algunas marcas
    marcas = ['Toyota', 'Honda', 'Suzuki', 'Yamaha', 'Ford']
    for nombre_marca in marcas:
        marca = Marca.objects.get_or_create(nombre=nombre_marca)[0]
        marca.save()

    # Crear algunos vehículos
    vehiculos_data = [
        {'tipo_vehiculo': 'Coche', 'chasis': 'CHASIS123', 'marca': 'Toyota', 'modelo': 'Corolla', 'matricula': 'ABC123',
         'color': 'Rojo', 'fecha_fabricacion': date(2022, 1, 1), 'fecha_matriculacion': date(2022, 1, 1)},
        {'tipo_vehiculo': 'Ciclomotor', 'chasis': 'CHASIS456', 'marca': 'Yamaha', 'modelo': 'Jog',
         'matricula': 'DEF456',
         'color': 'Azul', 'fecha_fabricacion': date(2021, 5, 15), 'fecha_matriculacion': date(2021, 5, 15)},
        {'tipo_vehiculo': 'Motocicleta', 'chasis': 'CHASIS789', 'marca': 'Suzuki', 'modelo': 'GSX-R1000',
         'matricula': 'GHI789', 'color': 'Verde', 'fecha_fabricacion': date(2023, 8, 20),
         'fecha_matriculacion': date(2023, 8, 20)}
    ]

    for vehiculo_data in vehiculos_data:
        marca_obj = Marca.objects.get(nombre=vehiculo_data['marca'])
        vehiculo = Vehiculo(
            tipo_vehiculo=vehiculo_data['tipo_vehiculo'],
            chasis=vehiculo_data['chasis'],
            marca=marca_obj,
            modelo=vehiculo_data['modelo'],
            matricula=vehiculo_data['matricula'],
            color=vehiculo_data['color'],
            fecha_fabricacion=vehiculo_data['fecha_fabricacion'],
            fecha_matriculacion=vehiculo_data['fecha_matriculacion']
        )
        vehiculo.save()


if __name__ == '__main__':
    llenar_modelos()
