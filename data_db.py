from app import app
from models import db, Product, Category, Supplier, Storage

def crear_datos_ejemplo():
    with app.app_context():
        # Crear categorías
        cat1 = Category(name="Electrónica", description="Dispositivos y gadgets electrónicos")
        cat2 = Category(name="Muebles", description="Muebles para el hogar y la oficina")
        cat3 = Category(name="Ropa", description="Ropa y accesorios")

        db.session.add_all([cat1, cat2, cat3])
        db.session.commit()

        # Crear proveedores
        prov1 = Supplier(name="Proveedor Uno", address="Calle Proveedor 123", cellphone="1234567890")
        prov2 = Supplier(name="Proveedor Dos", address="Avenida Proveedor 456", cellphone="2345678901")
        prov3 = Supplier(name="Proveedor Tres", address="Boulevard Proveedor 789", cellphone="3456789012")

        db.session.add_all([prov1, prov2, prov3])
        db.session.commit()

        # Crear bodegas
        bod1 = Storage(name="Bodega Principal", location="Ciudad Central", max_capacity=1000)
        bod2 = Storage(name="Bodega Secundaria", location="Lado Este", max_capacity=800)
        bod3 = Storage(name="Bodega de Reserva", location="Lado Oeste", max_capacity=600)

        db.session.add_all([bod1, bod2, bod3])
        db.session.commit()

        # Crear productos
        products = [
            Product(
                name="Portátil", 
                description="Portátil de alto rendimiento", 
                price=1200.00, 
                stock=50, 
                category=cat1, 
                supplier=prov1, 
                storage=bod1),
            Product(
                name="Teléfono Inteligente", 
                description="Último modelo de teléfono inteligente",
                price=800.00, 
                stock=100, 
                category=cat1, 
                supplier=prov2, 
                storage=bod1),
            Product(
                name="Tableta", 
                description="Tableta de 10 pulgadas", 
                price=300.00, 
                stock=70, 
                category=cat1, 
                supplier=prov3, 
                storage=bod1),
            Product(
                name="Silla de Oficina", 
                description="Silla ergonómica de oficina", 
                price=150.00, 
                stock=20, 
                category=cat2, 
                supplier=prov1, 
                storage=bod2),
            Product(
                name="Escritorio", 
                description="Escritorio de madera para oficina", 
                price=200.00, 
                stock=15, 
                category=cat2, 
                supplier=prov2, 
                storage=bod2),
            Product(
                name="Estante", 
                description="Estante de 5 niveles", 
                price=100.00, stock=30, 
                category=cat2, 
                supplier=prov3, 
                storage=bod2),
            Product(
                name="Camiseta", 
                description="Camiseta de algodón", 
                price=20.00, 
                stock=200, 
                category=cat3, 
                supplier=prov1, 
                storage=bod3),
            Product(
                name="Jeans", 
                description="Jeans de mezclilla", 
                price=50.00, 
                stock=150, 
                category=cat3, 
                supplier=prov2, 
                storage=bod3),
            Product(
                name="Chaqueta", 
                description="Chaqueta de cuero", 
                price=120.00, 
                stock=80, 
                category=cat3, 
                supplier=prov3, 
                storage=bod3),
            Product(
                name="Auriculares", 
                description="Auriculares inalámbricos", 
                price=100.00, 
                stock=90, 
                category=cat1, 
                supplier=prov1, 
                storage=bod1),
            Product(
                name="Monitor", 
                description="Monitor de 24 pulgadas", 
                price=200.00, 
                stock=60, 
                category=cat1, 
                supplier=prov2, 
                storage=bod1),
            Product(
                name="Teclado", 
                description="Teclado mecánico", 
                price=80.00, 
                stock=110, 
                category=cat1, 
                supplier=prov3, 
                storage=bod1),
            Product(
                name="Mesa de Comedor", 
                description="Mesa de comedor para 6 personas", 
                price=400.00, 
                stock=10, 
                category=cat2, 
                supplier=prov1, 
                storage=bod2),
            Product(
                name="Sofá", 
                description="Sofá de 3 plazas", 
                price=500.00, 
                stock=8, 
                category=cat2, 
                supplier=prov2, 
                storage=bod2),
            Product(
                name="Cama", 
                description="Cama tamaño queen", 
                price=700.00, 
                stock=12, 
                category=cat2, 
                supplier=prov3, 
                storage=bod2)
        ]

        for product in products:
            db.session.add(product)
        db.session.commit()

        print("Datos de ejemplo creadas exitosamente.")

if __name__ == "__main__":
    crear_datos_ejemplo()
