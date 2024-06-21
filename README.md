# Scott Database
Este proyecto es una interfaz básica para realizar operaciones CRUD en la base de datos scott.

## Ejecutar el proyecto 🚀
Este proyecto esta creado con Flask y MySQL.

### Pre-requisitos
    Instancia de MySQL
    Python 3.10
    Python venv

### Entorno virtual de Python
Para mantener las dependencias del proyecto controladas se utilizo el entorno virtual de Python (venv),
si quieres saber más sobre como utilizar venv puedes encontrar la documentación [aquí](https://docs.python.org/3/library/venv.html).

Las lista de las librerias utilizadas las puedes encontrar en ```requirements.txt```.

## Instalación 🔧
Una vez creado el entorno virtual se deben instalar las dependencias:

    pip install -r requirements.txt

Se debe tener una base de datos MySQL, para crear el esquema de la base de datos se puede utlizar el archivo ````create_db.sql```` que se encuentra dentro de la carpeta ````sql````.

Dentro del archivo ````main.py```` se especifica la cadena de conexión para la base de datos, no se olvide de cambiar el usuario y contraseña.

## Construido con 🛠️
- Flask
- WTForms
- SQLAlchemy

## Autor ✒️
Este es un proyecto final para la UACh creado por:
- [Erick Amezcua](https://gist.github.com/Orick08)