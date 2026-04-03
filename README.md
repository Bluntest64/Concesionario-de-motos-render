# MotoGama — Sistema de Gestión para Concesionario

Aplicación web desarrollada con **Python + Flask** y **MySQL** para la gestión de un concesionario de motocicletas de alta gama.

## Estructura del proyecto

```
concesionario/
├── app.py                        # Punto de entrada y factory de la app
├── config.py                     # Variables de configuración
├── requirements.txt              # Dependencias Python
│
├── database/
│   └── schema.sql                # Script SQL: tablas + datos de ejemplo
│
├── models/                       # Capa de acceso a datos (M del MVC)
│   ├── __init__.py
│   ├── vehiculo.py
│   ├── cliente.py
│   └── venta.py
│
├── controllers/                  # Lógica de negocio y rutas (C del MVC)
│   ├── __init__.py
│   ├── vehiculo_controller.py
│   ├── cliente_controller.py
│   ├── venta_controller.py
│   └── reporte_controller.py
│
├── templates/                    # Vistas HTML con Jinja2 (V del MVC)
│   ├── base.html                 # Plantilla base (herencia)
│   ├── partials/
│   │   ├── navbar.html
│   │   └── flash.html
│   ├── vehiculos/
│   │   ├── lista.html
│   │   └── formulario.html
│   ├── clientes/
│   │   ├── lista.html
│   │   └── formulario.html
│   ├── ventas/
│   │   ├── lista.html
│   │   ├── formulario.html
│   │   └── detalle.html
│   └── reportes/
│       └── index.html
│
└── static/
    ├── css/
    │   ├── main.css              # Variables, reset, layout, tipografía
    │   ├── components.css        # Navbar, tabla, badges, botones
    │   └── forms.css             # Formularios y barra de filtros
    ├── js/
    │   ├── main.js               # Utilidades globales
    │   ├── vehiculos.js          # Lógica módulo vehículos
    │   ├── clientes.js           # Validaciones módulo clientes
    │   ├── ventas.js             # Lógica módulo ventas
    │   └── reportes.js           # Gráficos módulo reportes
    └── img/                      # Imágenes estáticas
```

## Instalación y ejecución

```bash
# 1. Clonar el repositorio
git clone <url-del-repo>
cd concesionario

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Crear la base de datos
mysql -u root -p < database/schema.sql

# 5. Ejecutar la aplicación
python app.py
```

La app estará disponible en `http://localhost:5000`

## Funcionalidades

| Módulo       | Operaciones                              |
|-------------|------------------------------------------|
| Vehículos   | CRUD completo + filtros por marca/precio |
| Clientes    | CRUD completo + búsqueda por documento   |
| Ventas      | Registro con validación de disponibilidad|
| Reportes    | Resumen estadístico + historial          |

## Tecnologías

- **Backend:** Python 3.x + Flask 3.0
- **Base de datos:** MySQL
- **Frontend:** HTML5 + CSS3 + JavaScript (vanilla)
- **Arquitectura:** MVC con Blueprints de Flask
