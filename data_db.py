from app import app
from models import db, Category, Product, Supplier, Storage

# Configurar la ruta de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parcial.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def poblar_db():
    with app.app_context():
        # Crear categorías
        categoria1 = Category(name="Electrónica", description="Dispositivos electrónicos")
        categoria2 = Category(name="Ropa", description="Vestimenta y accesorios")
        db.session.add(categoria1)
        db.session.add(categoria2)

        # Crear proveedores
        proveedor1 = Supplier(name="Proveedor A", address="Calle 123", cellphone="555-1234")
        proveedor2 = Supplier(name="Proveedor B", address="Avenida 456", cellphone="555-5678")
        db.session.add(proveedor1)
        db.session.add(proveedor2)

        # Crear bodegas
        bodega1 = Storage(name="Bodega Central", location="Zona Industrial", max_capacity=1000)
        bodega2 = Storage(name="Bodega Secundaria", location="Parque Empresarial", max_capacity=500)
        db.session.add(bodega1)
        db.session.add(bodega2)

        # Crear productos
        producto1 = Product(
            name="Laptop",
            description="Laptop de alta gama",
            price=1200.00,
            stock=50,
            category=categoria1,
            supplier=proveedor1,
            storage=bodega1
        )
        producto2 = Product(
            name="Camiseta",
            description="Camiseta de algodón",
            price=20.00,
            stock=200,
            category=categoria2,
            supplier=proveedor2,
            storage=bodega2
        )
        db.session.add(producto1)
        db.session.add(producto2)

        # Guardar cambios en la base de datos
        db.session.commit()
        print("Base de datos poblada con éxito.")

if __name__ == '__main__':
    poblar_db()
