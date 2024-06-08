from app import app
from models import db, Category, Product, Supplier, Storage

# Configurar la ruta de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parcial.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def poblar_db():
    with app.app_context():
        # Crear categorías
        category1 = Category(name="Electrónica", description="Dispositivos electrónicos")
        category2 = Category(name="Ropa", description="Vestimenta y accesorios")
        db.session.add(category1)
        db.session.add(category2)

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
        products = [
            Product(
                name="Laptop",
                description="Laptop de alta gama",
                price=1200.00,
                stock=50,
                category=category1,
                supplier=proveedor1,
                storage=bodega1
            ),
            Product(
                name="Camiseta",
                description="Camiseta de algodón",
                price=20.00,
                stock=200,
                category=category2,
                supplier=proveedor2,
                storage=bodega2
            ),
            Product(
                name="Smartphone",
                description="Teléfono inteligente",
                price=800.00,
                stock=100,
                category=category1,
                supplier=proveedor1,
                storage=bodega1
            ),
            Product(
                name="Pantalones",
                description="Pantalones de mezclilla",
                price=40.00,
                stock=100,
                category=category2,
                supplier=proveedor2,
                storage=bodega2
            ),
            Product(
                name="Tablet",
                description="Tablet de 10 pulgadas",
                price=300.00,
                stock=70,
                category=category1,
                supplier=proveedor1,
                storage=bodega1
            ),
            Product(
                name="Chaqueta",
                description="Chaqueta de cuero",
                price=150.00,
                stock=80,
                category=category2,
                supplier=proveedor2,
                storage=bodega2
            ),
            Product(
                name="Monitor",
                description="Monitor 4K",
                price=400.00,
                stock=60,
                category=category1,
                supplier=proveedor1,
                storage=bodega1
            ),
            Product(
                name="Zapatos",
                description="Zapatos deportivos",
                price=60.00,
                stock=120,
                category=category2,
                supplier=proveedor2,
                storage=bodega2
            ),
            Product(
                name="Auriculares",
                description="Auriculares inalámbricos",
                price=100.00,
                stock=90,
                category=category1,
                supplier=proveedor1,
                storage=bodega1
            ),
            Product(
                name="Reloj",
                description="Reloj de pulsera",
                price=200.00,
                stock=75,
                category=category1,
                supplier=proveedor1,
                storage=bodega1
            )
        ]
        for product in products:
            db.session.add(product)

        # Guardar cambios en la base de datos
        db.session.commit()
        print("Base de datos poblada con éxito.")

if __name__ == '__main__':
    poblar_db()
