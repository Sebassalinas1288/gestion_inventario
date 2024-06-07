from app import app, db
from models import Category, Supplier, Storage

def tableCreated():
    with app.app_context():
        inspector = db.inspect(db.engine)
        return (
            inspector.has_table('product') and 
            inspector.has_table('category') and 
            inspector.has_table('supplier') and
            inspector.has_table('storage')
        )

def createTables():
    with app.app_context():
        db.create_all()
        print("Tablas creadas en la base de datos.")

def createCategory():
    with app.app_context():
        sin_categoria = Category.query.filter_by(name='Sin categoría').first()
        if not sin_categoria:
            sin_categoria = Category(name='Sin categoría', description='Productos sin categoría asignada')
            db.session.add(sin_categoria)
            db.session.commit()
            print("Categoría 'Sin categoría' creada con éxito.")

def createSupplier():
    with app.app_context():
        sin_proveedor = Supplier.query.filter_by(name='Sin proveedor').first()
        if not sin_proveedor:
            sin_proveedor = Supplier(name='Sin proveedor', address='', cellphone='')
            db.session.add(sin_proveedor)
            db.session.commit()
            print("Proveedor 'Sin proveedor' creado con éxito.")

def createStorage():
    with app.app_context():
        sin_bodega = Storage.query.filter_by(name='Sin bodega').first()
        if not sin_bodega:
            sin_bodega = Storage(name='Sin bodega', location='none', max_capacity='')
            db.session.add(sin_bodega)
            db.session.commit()
            print("Bodega 'Sin bodega' creada con éxito.")

if not tableCreated():
    createTables()
    createCategory()
    createSupplier()
    createStorage()
    print("Base de datos creada con éxito y categoría 'Sin categoría' agregada.")
else:
    print("Las tablas ya están creadas en la base de datos.")
