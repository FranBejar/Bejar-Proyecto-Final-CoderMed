# Obra Social CoderMed

## Instalacion
+ Crear Carpeta Contenedora
+ Abrir terminal y mediante el comando cd ubicarse en la carpeta contenedora
+ Clone este proyecto e ingrese en la carpeta

## Instalar Requerimientos
+ Para instalar los requerimientos minimos ejecute el siguiente comando

```
pip install -r requirements.txt
```

## Funciones del Proyecto
+ Este proyecto simula una pagina de una Obra Social de prestaciones Medicas, con cartilla de Hospitales y Medicos Matriculados
+ Toda esta cartilla de profesionales se encuentra almacenada en una base de datos
+ A su vez la base de datos cuenta con un registro de los afiliados a la Obra Social con sus datos personales y de plan medico
+ El proyecto permite actualmente revisar la cartilla de hospitales con cobertura, medicos especializados en diferentes areas medicas y posee un formulario para afiliarse a la Obra Social completando una serie de datos
+ A su vez tiene una sección donde detalla los beneficios de cada plan

## Iniciar servidor
+ Al clonar el repositorio, para iniciar el servidor debe ejecutar el siguiente comando (siempre ubicado en la carpeta contenedora)
```
python manage.py runserver
```
+ Al ejecutar este comando se proporcionara una direccion IP la cual sera donde se esta ejecutando el proyecto

## Funciones de Administrador
+ Una vez ejecutado el proyecto puede acceder a las funciones de administrador agregando a la IP brindada /admin
+ Esto lo redirigira a una pagina de administrador que solicitara Usuario y Contraseña
+ Al ser un proyecto de prueba sin datos sensibles se proporciona el usuario administrador de pruebas

username: admin
password: coder

+ En caso de no tener este usuario puede crear uno con el siguiente comando
```
python manage.py createsuperuser
```
+ Este comando le pedira ciertos datos a modo de credenciales para crear un usuario administrador