from flask import Flask, render_template, request, redirect, url_for
from models import db,  Producto, Categoria, Proveedor, Bodega

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parcial.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    productos = Producto.query.all()
    return render_template('index.html', productos=productos)

## PRODUCT

@app.route('/add-product', methods=['GET', 'POST'])
def addProduct():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        stock = request.form['stock']
        categoria_id = request.form['categoria_id']
        proveedor_id = request.form['proveedor_id']
        bodega_id = request.form['bodega_id']

        nuevo_producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=float(precio),
            stock=int(stock),
            categoria_id=int(categoria_id),
            proveedor_id=int(proveedor_id),
            bodega_id=int(bodega_id)
        )

        db.session.add(nuevo_producto)
        db.session.commit()

        return redirect(url_for('index'))

    categorias = Categoria.query.all()
    proveedores = Proveedor.query.all()
    bodegas = Bodega.query.all()
    return render_template('product/addProduct.html', categorias=categorias, proveedores=proveedores, bodegas=bodegas)

@app.route('/consultar-productos')
def readProducts():
    productos = Producto.query.all()
    return render_template('product/readProduct.html', productos=productos)

## CATEGORY

@app.route('/add-categoria', methods=['GET', 'POST'])
def addCategory():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']

        nueva_categoria = Categoria(nombre=nombre, descripcion=descripcion)
        db.session.add(nueva_categoria)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('category/addCategory.html')

@app.route('/consultar-categorias')
def readCategories():
    categorias = Categoria.query.all()
    return render_template('category/readCategory.html', categorias=categorias)

## SUPPLIER

@app.route('/add-proveedor', methods=['GET', 'POST'])
def addSupplier():
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        telefono = request.form['telefono']

        nuevo_proveedor = Proveedor(nombre=nombre, direccion=direccion, telefono=telefono)
        db.session.add(nuevo_proveedor)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('supplier/addSupplier.html')

@app.route('/consultar-proveedores')
def readSuppliers():
    proveedores = Proveedor.query.all()
    return render_template('supplier/readSupplier.html', proveedores=proveedores)

## STORAGE

@app.route('/add-bodega', methods=['GET', 'POST'])
def addStorage():
    if request.method == 'POST':
        nombre = request.form['nombre']
        ubicacion = request.form['ubicacion']
        capacidad_maxima = request.form['capacidad_maxima']

        nueva_bodega = Bodega(nombre=nombre, ubicacion=ubicacion, capacidad_maxima=int(capacidad_maxima))
        db.session.add(nueva_bodega)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('storage/addStorage.html')

@app.route('/consultar-bodegas')
def readStorages():
    bodegas = Bodega.query.all()
    return render_template('storage/readStorage.html', bodegas=bodegas)

## STOCK

@app.route('/add-stock/<int:producto_id>', methods=['GET', 'POST'])
def addStock(producto_id):
    producto = Producto.query.get_or_404(producto_id)
    if request.method == 'POST':
        cantidad = int(request.form['cantidad'])
        producto.stock += cantidad
        db.session.commit()
        return redirect(url_for('readProducts'))

    return render_template('stock/addStock.html', producto=producto)

@app.route('/remove-stock/<int:producto_id>', methods=['GET', 'POST'])
def removeStock(producto_id):
    producto = Producto.query.get_or_404(producto_id)
    if request.method == 'POST':
        cantidad = int(request.form['cantidad'])
        if cantidad <= producto.stock:
            producto.stock -= cantidad
            db.session.commit()
        else:
            # Manejar el caso donde se intenta retirar más stock del disponible
            return "Error: No se puede retirar más stock del disponible."
        return redirect(url_for('readProducts'))

    return render_template('stock/removeStock.html', producto=producto)

@app.route('/calcular-valor-total-stock')
def calculateStockValue():
    productos = Producto.query.all()
    valor_total = sum(producto.precio * producto.stock for producto in productos)
    return render_template('stock/calculateStockValue.html', valor_total=valor_total)

@app.route('/asignar-producto-categoria', methods=['GET', 'POST'])
def assignProductCategory():
    if request.method == 'POST':
        producto_id = request.form['producto_id']
        categoria_id = request.form['categoria_id']
        producto = Producto.query.get(producto_id)
        producto.categoria_id = categoria_id
        db.session.commit()
        return redirect(url_for('readProducts'))

    productos = Producto.query.all()
    categorias = Categoria.query.all()
    return render_template('category/assignProductCategory.html', productos=productos, categorias=categorias)

@app.route('/eliminar-producto-categoria/<int:producto_id>', methods=['POST'])
def removeProductCategory(producto_id):
    producto = Producto.query.get_or_404(producto_id)
    producto.categoria_id = 1
    db.session.commit()
    return redirect(url_for('readProducts'))

if __name__ == '__main__':
    app.run(debug=True)