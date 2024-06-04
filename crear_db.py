from app import app, db
from models import Categoria

def tablas_creadas():
    with app.app_context():
        inspector = db.inspect(db.engine)
        return (
            inspector.has_table('producto') and 
            inspector.has_table('categoria') and 
            inspector.has_table('proveedor') and
            inspector.has_table('bodega')
        )

def crear_tablas():
    with app.app_context():
        db.create_all()
        print("Tablas creadas en la base de datos.")

def crear_categoria_sin_categoria():
    with app.app_context():
        sin_categoria = Categoria.query.filter_by(nombre='Sin categoría').first()
        if not sin_categoria:
            sin_categoria = Categoria(nombre='Sin categoría', descripcion='Productos sin categoría asignada')
            db.session.add(sin_categoria)
            db.session.commit()
            print("Categoría 'Sin categoría' creada con éxito.")

if not tablas_creadas():
    crear_tablas()
    crear_categoria_sin_categoria()
    print("Base de datos creada con éxito y categoría 'Sin categoría' agregada.")
else:
    print("Las tablas ya están creadas en la base de datos.")
