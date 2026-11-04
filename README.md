# Módulo de Login - Casilleros Inteligentes IoT
Módulo básico de autenticación con Django para el proyecto TFA de Procesos de Software.

## Estructura
```
modulo_login_django/
├── venv/                         # Entorno virtual (no instalar dependencias localmente)
├── config/                       # Configuración del proyecto Django
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── accounts/                     # App de autenticación
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   ├── admin.py
│   ├── migrations/
│   └── templates/
│       └── accounts/
├── templates/                    # Plantillas globales
│   └── base.html
├── manage.py
├── requirements.txt              # Dependencias del proyecto
├── .gitignore
└── README.md
```

## Requisitos
- Python 3.x
- Django 6.1.3 (instalado en el entorno virtual)

## Instalación y ejecución

1. Crear y activar el entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Aplicar migraciones:
   ```bash
   python manage.py migrate
   ```

4. Crear un superusuario (para acceder al admin de Django):
   ```bash
   python manage.py createsuperuser
   ```

5. Ejecutar el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

6. Acceder a: http://127.0.0.1:8000/

## Normativa y buenas prácticas

Este módulo sigue los principios de ISO/IEC/IEEE 12207:2017 adaptados al proyecto:

- **Separación de responsabilidades**: la app `accounts` encapsula la autenticación.
- **Configuración centralizada**: `config/settings.py` define los parámetros del proyecto.
- **Entorno virtual**: las dependencias se instalan en `venv/`, no en el sistema.
- **Versionado**: `requirements.txt` registra las versiones de las dependencias.
- **Plantillas reutilizables**: `base.html` define la estructura común.

## Metodología
Proyecto desarrollado bajo FDD + Kanban con rotación de roles (PM, CA, DM, CP, CO) según la planificación del TFA.
