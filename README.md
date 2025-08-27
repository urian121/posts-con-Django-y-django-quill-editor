
# Blog con Django y django-quill-editor

Este es un proyecto sencillo de blog hecho con **Django** y **django-quill-editor** para agregar y mostrar publicaciones con contenido enriquecido (negritas, imágenes, listas, etc.).

## Características
- Crear, listar y ver publicaciones.
- Editor de texto enriquecido con Quill.
- Interfaz simple y responsive usando Bootstrap.

## Requisitos
- Python 3.10+
- Django 5+
- django-quill-editor

## Instalación
```bash
# Clona el repositorio
git clone https://github.com/tuusuario/django-quill-blog.git
cd django-quill-blog

# Crea entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate

# Instala dependencias
pip install django django-quill-editor

# Ejecuta migraciones y corre el servidor
python manage.py migrate
python manage.py runserver
```

## Uso
1. Abre `http://127.0.0.1:8000/`
2. Crea nuevas publicaciones con el editor Quill.
3. Visualiza los posts creados.

---
¡Listo! Tienes un mini blog funcional con editor Quill sin necesidad de entrar al admin.
