import os
from app import app
from models import db, Categoria, Proveedor, Bodega, Producto

# Configurar la ruta de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parcial.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def poblar_db():
    with app.app_context():
        # Crear categorías
        categoria1 = Categoria(nombre="Electrónica", descripcion="Dispositivos electrónicos")
        categoria2 = Categoria(nombre="Ropa", descripcion="Vestimenta y accesorios")
        db.session.add(categoria1)
        db.session.add(categoria2)

        # Crear proveedores
        proveedor1 = Proveedor(nombre="Proveedor A", direccion="Calle 123", telefono="555-1234")
        proveedor2 = Proveedor(nombre="Proveedor B", direccion="Avenida 456", telefono="555-5678")
        db.session.add(proveedor1)
        db.session.add(proveedor2)

        # Crear bodegas
        bodega1 = Bodega(nombre="Bodega Central", ubicacion="Zona Industrial", capacidad_maxima=1000)
        bodega2 = Bodega(nombre="Bodega Secundaria", ubicacion="Parque Empresarial", capacidad_maxima=500)
        db.session.add(bodega1)
        db.session.add(bodega2)

        # Crear productos
        producto1 = Producto(
            nombre="Laptop",
            descripcion="Laptop de alta gama",
            precio=1200.00,
            stock=50,
            categoria=categoria1,
            proveedor=proveedor1,
            bodega=bodega1
        )
        producto2 = Producto(
            nombre="Camiseta",
            descripcion="Camiseta de algodón",
            precio=20.00,
            stock=200,
            categoria=categoria2,
            proveedor=proveedor2,
            bodega=bodega2
        )
        db.session.add(producto1)
        db.session.add(producto2)

        # Guardar cambios en la base de datos
        db.session.commit()
        print("Base de datos poblada con éxito.")

if __name__ == '__main__':
    poblar_db()
