from flask import Flask, render_template, request, redirect, url_for
from models import db,  Product, Category, Supplier, Storage

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parcial.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

## -------- PRODUCT --------

@app.route('/add-product', methods=['GET', 'POST'])
def addProduct():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        stock = request.form['stock']
        category_id = request.form['category_id']
        supplier_id = request.form['supplier_id']
        storage_id = request.form['storage_id']

        newProduct = Product(
            name=name,
            description=description,
            price=float(price),
            stock=int(stock),
            category_id=int(category_id),
            supplier_id=int(supplier_id),
            storage_id=int(storage_id)
        )

        db.session.add(newProduct)
        db.session.commit()

        return redirect(url_for('index'))

    categories = Category.query.all()
    suppliers = Supplier.query.all()
    storages = Storage.query.all()
    return render_template('product/addProduct.html', categories=categories, suppliers=suppliers, storages=storages)

@app.route('/consultar-productos')
def readProducts():
    products = Product.query.all()
    return render_template('product/readProducts.html', products=products)

@app.route('/consultar-producto/<int:product_id>')
def readProduct(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product/readProduct.html', product=product)

@app.route('/eliminar-producto-categoria/<int:product_id>', methods=['POST'])
def removeProductCategory(product_id):
    producto = Product.query.get_or_404(product_id)
    producto.category_id = 1  # Asignar la categoría "Sin categoría"
    db.session.commit()
    return redirect(url_for('readProducts'))


## -------- CATEGORY --------

@app.route('/add-categoria', methods=['GET', 'POST'])
def addCategory():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        newCategory = Category(name=name, description=description)
        db.session.add(newCategory)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('category/addCategory.html')

@app.route('/consultar-categorias')
def readCategories():
    categories = Category.query.all()
    return render_template('category/readCategories.html', categories=categories)

@app.route('/consultar-categoria/<int:category_id>')
def consultarCategoria(category_id):
    category = Category.query.get_or_404(category_id)
    return render_template('category/readCategory.html', category=category)

@app.route('/asignar-producto-categoria/<int:product_id>', methods=['GET', 'POST'])
def assignProductCategory(product_id):
    product = Product.query.get_or_404(product_id)
    
    if request.method == 'POST':
        category_id = request.form['category_id']
        product.category_id = category_id
        db.session.commit()
        return redirect(url_for('readProducts'))

    categories = Category.query.all()
    return render_template('category/assignProductCategory.html', product=product, categories=categories)



## SUPPLIER

@app.route('/add-proveedor', methods=['GET', 'POST'])
def addSupplier():
    if request.method == 'POST':
        name = request.form['name']
        direccion = request.form['direccion']
        telefono = request.form['telefono']

        nuevo_proveedor = Supplier(name=name, direccion=direccion, telefono=telefono)
        db.session.add(nuevo_proveedor)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('supplier/addSupplier.html')

@app.route('/consultar-proveedores')
def readSuppliers():
    proveedores = Supplier.query.all()
    return render_template('supplier/readSuppliers.html', proveedores=proveedores)

@app.route('/consultar-proveedor/<int:proveedor_id>')
def consultarProveedor(proveedor_id):
    proveedor = Supplier.query.get_or_404(proveedor_id)
    return render_template('supplier/readSupplier.html', proveedor=proveedor)


## -------- STORAGE ---------
@app.route('/add-bodega', methods=['GET', 'POST'])
def addStorage():
    if request.method == 'POST':
        name = request.form['name']
        ubicacion = request.form['ubicacion']
        capacidad_maxima = request.form['capacidad_maxima']

        nueva_bodega = Storage(name=name, ubicacion=ubicacion, capacidad_maxima=int(capacidad_maxima))
        db.session.add(nueva_bodega)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('storage/addStorage.html')

@app.route('/consultar-bodegas')
def readStorages():
    bodegas = Storage.query.all()
    return render_template('storage/readStorages.html', bodegas=bodegas)

@app.route('/consultar-bodega/<int:bodega_id>')
def consultarBodega(bodega_id):
    bodega = Storage.query.get_or_404(bodega_id)
    productos = bodega.productos
    total_stock = sum(producto.stock for producto in productos)
    return render_template('storage/readStorage.html', bodega=bodega, productos=productos, total_stock=total_stock)

## STOCK

@app.route('/add-stock/<int:product_id>', methods=['GET', 'POST'])
def addStock(product_id):
    producto = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        cantidad = int(request.form['cantidad'])
        producto.stock += cantidad
        db.session.commit()
        return redirect(url_for('readProducts'))

    return render_template('stock/addStock.html', producto=producto)

@app.route('/remove-stock/<int:product_id>', methods=['GET', 'POST'])
def removeStock(product_id):
    producto = Product.query.get_or_404(product_id)
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
    productos = Product.query.all()
    valor_total = sum(producto.precio * producto.stock for producto in productos)
    return render_template('stock/calculateStockValue.html', valor_total=valor_total)

@app.route('/informe-stock')
def informeStock():
    productos = Product.query.all()
    categorias = Category.query.all()
    proveedores = Supplier.query.all()
    bodegas = Storage.query.all()
    
    # Función para calcular el stock total por categoría
    def categoria_stock(categoria):
        return sum(producto.stock for producto in productos if producto.categoria_id == categoria.id)

    # Función para calcular el stock total por proveedor
    def proveedor_stock(proveedor):
        return sum(producto.stock for producto in productos if producto.proveedor_id == proveedor.id)

    # Función para calcular el stock total por bodega
    def bodega_stock(bodega):
        return sum(producto.stock for producto in productos if producto.bodega_id == bodega.id)

    stock_total = sum(producto.stock for producto in productos)

    return render_template(
        'stock/reportStock.html',
        valor_total=stock_total,
        categorias=categorias,
        proveedores=proveedores,
        bodegas=bodegas,
        categoria_stock=categoria_stock,
        proveedor_stock=proveedor_stock,
        bodega_stock=bodega_stock
    )







# Relación entre Product y Supplier
@app.route('/asignar-producto-proveedor', methods=['GET', 'POST'])
def assignProductSupplier():
    if request.method == 'POST':
        producto_id = request.form['producto_id']
        proveedor_id = request.form['proveedor_id']
        producto = Product.query.get(producto_id)
        producto.proveedor_id = proveedor_id
        db.session.commit()
        return redirect(url_for('readProducts'))

    productos = Product.query.all()
    proveedores = Supplier.query.all()
    return render_template('supplier/assignProductSupplier.html', productos=productos, proveedores=proveedores)

@app.route('/eliminar-producto-proveedor/<int:producto_id>', methods=['POST'])
def removeProductSupplier(producto_id):
    producto = Product.query.get_or_404(producto_id)
    producto.proveedor_id = None
    db.session.commit()
    return redirect(url_for('readProducts'))

# Relación entre Product y Storage
@app.route('/agregar-producto-bodega/<int:producto_id>', methods=['GET', 'POST'])
def addProductToStorage(producto_id):
    producto = Product.query.get_or_404(producto_id)
    if request.method == 'POST':
        bodega_id = request.form['bodega_id']
        bodega = Storage.query.get(bodega_id)
        if producto.stock <= bodega.capacidad_maxima:
            producto.bodega_id = bodega_id
            bodega.productos.append(producto)
            db.session.commit()
            return redirect(url_for('readProducts'))
        else:
            return "Error: No hay suficiente espacio en la bodega para almacenar el producto."

    bodegas = Storage.query.all()
    return render_template('storage/addProductToStorage.html', producto=producto, bodegas=bodegas)

@app.route('/remover-producto-bodega/<int:producto_id>', methods=['GET', 'POST'])
def removeProductFromStorage(producto_id):
    producto = Product.query.get_or_404(producto_id)
    if request.method == 'POST':
        producto.bodega_id = None
        db.session.commit()
        return redirect(url_for('readProducts'))

    return render_template('storage/removeProductFromStorage.html', producto=producto)

@app.route('/consultar-disponibilidad', methods=['GET', 'POST'])
def checkProductAvailability():
    if request.method == 'POST':
        producto_id = request.form['producto_id']
        bodega_id = request.form['bodega_id']
        producto = Product.query.get_or_404(producto_id)
        bodega = Storage.query.get_or_404(bodega_id)
        
        # Obtener la cantidad del producto en la bodega específica
        cantidad = None
        for prod in bodega.productos:
            if prod.id == producto.id:
                cantidad = prod.stock
                break
                
        return render_template('storage/checkProductAvailability.html', producto=producto, bodega=bodega, cantidad=cantidad)

    productos = Product.query.all()
    bodegas = Storage.query.all()
    return render_template('storage/checkAvailabilityForm.html', productos=productos, bodegas=bodegas)



if __name__ == '__main__':
    app.run(debug=True)