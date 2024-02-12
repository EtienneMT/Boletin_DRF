# Boletín de ejercicios

Ejercicios sobre APIs de Django REST Framework

### Instalación

```bash
git clone https://github.com/EtienneMT/Boletin_DRF.git

cd Boletin_DRF

python -m venv venv-Boletin_DRF

# Windows

venv-Boletin_DRF\Scripts\activate

# MacOS y Linux

source nombre_del_entorno/bin/activate

pip install -r requirements.txt
```

Ahora tendrias que añadir tu fichero .envs/.local/.postgres, otro .env para que settings pueda coger las variables de entorno y por ultimo docker-compose.yml para que pueda levantar la base de datos.

```bash

python manage.py migrate

# crea tu superusuario
python manage.py createsuperuser 

python manage.py runserver

```


## [Ej 1: Gestion de vehiculos](gestion_vehiculos/readme.md)

### Uso de la API
#### Endpoints Principales

- vehiculos/vehiculos/: Endpoint para gestionar vehiculos.
- vehiculos/marcas/: Endpoint para gestionar marcas.


## [Ej 2: Gestion de alquiler de patinetes](alquiler_patinetes/readme.md)

### Uso de la API
#### Endpoints Principales

- patinetes/usuarios/: Endpoint para gestionar usuarios.
- patinetes/patinetes/: Endpoint para gestionar patinetes.
- patinetes/alquileres/: Endpoint para gestionar alquileres.
