# Gestión de Inventarios

Este es un sistema de gestión de inventarios desarrollado con Flask y SQLAlchemy. Permite registrar productos, categorías, proveedores y bodegas, también, permite realizar operaciones CRUD relacionado con estos elementos.

## Características

- Registrar y consultar productos, categorías, proveedores y bodegas.
- Asignar productos a categorías, proveedores y bodegas.
- Agregar y retirar stock de productos.
- Consultar la disponibilidad de productos en bodegas específicas.
- Calcular el valor total del stock y el total de productos en stock.
- Generar reporte stock, donde se encuentra el total y discriminado por categoría, proveedor y bodega.

## Requisitos

- Python 3.8+
- Flask
- Flask-SQLAlchemy

## Instalación

1. Clona el repositorio:
    - https://github.com/Sebassalinas1288/gestion_inventario.git
    - cd inventory-management

2. Crear un entorno virtual (opcional)
    - python -m venv venv
    - venv\Scripts\activate  # En Windows
    - source venv/bin/activate  # En macOS/Linux

3. Instala las dependencias:
    - pip install -r requirements.txt

4. Crea la base de datos:
    - python crear_db.py

5. Población inicial de la base de datos con datos de ejemplo:
    - python data_db.py

## Uso

1. Inicia la aplicación:
    - python app.py

2. Abre tu navegador web y navega a http://127.0.0.1:5000 para ver la aplicación en funcionamiento.

## Rutas Disponibles

### Productos

- /add-product: Añadir un nuevo producto.
- /consultar-productos: Consultar todos los productos.
- /consultar-producto/<product_id>: Consultar un producto específico.
- /eliminar-producto: Eliminar o desasociar un producto de una categoría, proveedor o bodega.

### Categorías

- /add-categoria: Añadir una nueva categoría.
- /consultar-categorias: Consultar todas las categorías.
- /consultar-categoria/<category_id>: Consultar una categoría específica.
- /asignar-producto-categoria/<product_id>: Asignar una categoría a un producto.

### Proveedores

- /add-proveedor: Añadir un nuevo proveedor.
- /consultar-proveedores: Consultar todos los proveedores.
- /consultar-proveedor/<supplier_id>: Consultar un proveedor específico.
- /asignar-producto-proveedor/<product_id>: Asignar un proveedor a un producto.

### Bodegas

- /add-bodega: Añadir una nueva bodega.
- /consultar-bodegas: Consultar todas las bodegas.
- /consultar-bodega/<storage_id>: Consultar una bodega específica.
- /agregar-producto-bodega/<product_id>: Asignar un producto a una bodega.
- /consultar-disponibilidad: Consultar la disponibilidad de un producto en una bodega específica.

### Stock

- /add-stock/<product_id>: Añadir stock a un producto.
- /remove-stock/<product_id>: Remover stock de un producto.
- /calcular-valor-total-stock: Calcular el valor total del stock.

### Informe
- /informe-stock: Generar un informe de stock.

