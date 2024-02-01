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

#### Endpoints Secundarios

- Alquilar un Patinete
URL: /alquileres/alquilar/
Método: POST
Datos requeridos:
patinete_id: ID del patinete que deseas alquilar.


- Liberar un Patinete
URL: /alquileres/liberar/
Método: POST
Datos requeridos:
patinete_id: ID del patinete que deseas liberar.


- Listar Alquileres (Solo Administradores)
URL: /alquileres/alquileres_admin/
Método: GET


- Listar Alquileres del Usuario Actual
URL: /alquileres/alquileres_usuario/
Método: GET


- Listar Patinetes Libres
URL: /patinetes/patinetes_libres/
Método: GET


- Listar Patinetes Ocupados
URL: /patinetes/patinetes_ocupados/
Método: GET


- Listar Usuarios por Débito
URL: /usuarios/usuarios_por_debito/
Método: GET


- Top Ten de Patinetes Alquilados
URL: /patinetes/top_ten_patinetes_alquilados/
Método: GET


- Top 3 de Usuarios en Número de Alquileres
URL: /usuarios/top_tres_usuarios_alquileres/
Método: GET


- Top 3 de Usuarios en Número de Débito
URL: /usuarios/top_tres_usuarios_debito/
Método: GET
