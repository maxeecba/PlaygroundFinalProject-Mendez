# PlaygroundFinalProject-Mendez
-----------------------Proyecto Final----------------------------
Alumno:Maximiliano Mendez
Comision: 56060
---------------------------------------------------------------
Pasos para ejecutar el proyecto:

Descargar el repositorio usando el siguiente comando en la terminal:
git clone https://github.com/maxeecba/PlaygroundFinalProject-Mendez.git


---------------------------------------------------------------
CD comando para moverse de carpetas:

Moverse a la carpeta TRABAJO FINAL:
cd TRABAJO FINAL
----------------------------------------------------------------
Entorno Virtual:

instalar el entorno virtual dentro de la carpeta TRABAJO FINAL(donde se encuentra el archivo .gitignore para que no haya errores):
py -m venv .venv

activar el entorno virtual con el siguiente comando:
.\.venv\Scripts\activate

instalar django
pip install django
--------------------------------------------------------------
moverse a la carpeta donde se encuentre el archivo manage.py:


ejecutar el servidor:
py manage.py runserver

mantener apretado el ctrl+ clic en la direccion http://127.0.0.1:8000/






python manage.py startapp usuarios
python manage.py startapp animales
python manage.py startapp comentarios