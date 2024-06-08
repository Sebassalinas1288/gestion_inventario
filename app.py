from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import db,  Product, Category, Supplier, Storage

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parcial.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    return redirect('/consultar-productos')

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

@app.route('/eliminar-producto', methods=['POST'])
def removeProduct():
    data = request.get_json()
    typeButton = data.get('type')
    product_id = data.get('productId')

    product = Product.query.get_or_404(product_id)
    if typeButton == 'delete-category':
        product.category_id = 1  # Asignar la categoría "Sin categoría"
    elif typeButton == 'delete-supplier':
        product.supplier_id = 1  # Asignar el proveedor "Sin proveedor"
    elif typeButton == 'delete-storage':
        product.storage_id = 1  # Asignar a la bodega "Sin Bodega"
    
    db.session.commit()
    
    return jsonify({"success": True, "message": "Producto actualizado correctamente"})



## -------- CATEGORY --------

@app.route('/add-categoria', methods=['GET', 'POST'])
def addCategory():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        newCategory = Category(name=name, description=description)
        db.session.add(newCategory)
        db.session.commit()

        return redirect(url_for('readCategories'))

    return render_template('category/addCategory.html')

@app.route('/consultar-categorias')
def readCategories():
    categories = Category.query.all()
    return render_template('category/readCategories.html', categories=categories)

@app.route('/consultar-categoria/<int:category_id>')
def readCategory(category_id):
    category = Category.query.get_or_404(category_id)
    return render_template('category/readCategory.html', category=category)

@app.route('/asignar-producto-categoria/<int:product_id>', methods=['GET', 'POST'])
def assignProductCategory(product_id):
    product = Product.query.get_or_404(product_id)
    
    if request.method == 'POST':
        product.category_id = request.form['category_id']
        db.session.commit()
        return redirect(url_for('readProducts'))

    categories = Category.query.all()
    return render_template('category/assignProductCategory.html', product=product, categories=categories)


## -------- SUPPLIER --------

@app.route('/add-proveedor', methods=['GET', 'POST'])
def addSupplier():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        cellphone = request.form['cellphone']

        newSupplier = Supplier(name=name, address=address, cellphone=cellphone)
        db.session.add(newSupplier)
        db.session.commit()

        return redirect(url_for('readSuppliers'))

    return render_template('supplier/addSupplier.html')

@app.route('/consultar-proveedores')
def readSuppliers():
    suppliers = Supplier.query.all()
    return render_template('supplier/readSuppliers.html', suppliers=suppliers)

@app.route('/consultar-proveedor/<int:supplier_id>', methods=['GET', 'POST'])
def consultarProveedor(supplier_id):
    supplier = Supplier.query.get_or_404(supplier_id)
    return render_template('supplier/readSupplier.html', supplier=supplier)

# Relación entre Product y Supplier
@app.route('/asignar-producto-proveedor/<int:product_id>', methods=['GET', 'POST'])
def assignProductSupplier(product_id):
    product = Product.query.get_or_404(product_id)

    if request.method == 'POST':
        product.supplier_id = request.form['supplier_id']
        db.session.commit()
        return redirect(url_for('readProducts'))
    
    suppliers = Supplier.query.all()
    return render_template('supplier/assignProductSupplier.html', product=product, suppliers=suppliers)


## -------- STORAGE ---------
@app.route('/add-bodega', methods=['GET', 'POST'])
def addStorage():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        max_capacity = request.form['max_capacity']

        newStorage = Storage(name=name, location=location, max_capacity=int(max_capacity))
        db.session.add(newStorage)
        db.session.commit()

        return redirect(url_for('readStorages'))

    return render_template('storage/addStorage.html')

@app.route('/consultar-bodegas')
def readStorages():
    storages = Storage.query.all()
    return render_template('storage/readStorages.html', storages=storages)

@app.route('/consultar-bodega/<int:storage_id>')
def readStorage(storage_id):
    storage = Storage.query.get_or_404(storage_id)
    products = storage.products
    totalStock = sum(products.stock for products in products)
    return render_template('storage/readStorage.html', storage=storage, products=products, totalStock=totalStock)

@app.route('/agregar-producto-bodega/<int:product_id>', methods=['GET', 'POST'])
def addProductToStorage(product_id):
    product = Product.query.get_or_404(product_id)
    storages = Storage.query.all()

    if request.method == 'POST':
        storage_id = request.form['storage_id']
        storage = Storage.query.get(storage_id)
        if product.stock <= storage.max_capacity:
            product.storage_id = storage_id
            storage.products.append(product)
            db.session.commit()
            return redirect(url_for('readProducts'))
        else:
            error= True
            return render_template('storage/addProductToStorage.html', product=product, storages=storages, error= error)
        
    return render_template('storage/addProductToStorage.html', product=product, storages=storages)

@app.route('/consultar-disponibilidad', methods=['GET', 'POST'])
def checkProductAvailability():
    if request.method == 'POST':
        product_id = request.form['product_id']
        storage_id = request.form['storage_id']
        product = Product.query.get_or_404(product_id)
        storage = Storage.query.get_or_404(storage_id)
        
        # Obtener la cantidad del producto en la bodega específica
        amount = None
        for prod in storage.products:
            if prod.id == product.id:
                amount = prod.stock
                break
                
        return render_template('storage/checkProductAvailability.html', product=product, storage=storage, amount=amount)

    products = Product.query.all()
    storages = Storage.query.all()
    return render_template('storage/checkAvailabilityForm.html', products=products, storages=storages)

## -------- STOCK --------

@app.route('/add-stock/<int:product_id>', methods=['GET', 'POST'])
def addStock(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        amount = int(request.form['amount'])
        product.stock += amount
        db.session.commit()
        return redirect(url_for('readProducts'))

    return render_template('stock/addStock.html', product=product)

@app.route('/remove-stock/<int:product_id>', methods=['GET', 'POST'])
def removeStock(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        amount = int(request.form['amount'])
        if amount <= product.stock:
            product.stock -= amount
            db.session.commit()
            return redirect(url_for('readProducts'))
        else:
            error= True
            return render_template('stock/removeStock.html', product=product, error= error)

    return render_template('stock/removeStock.html', product=product)

@app.route('/calcular-valor-total-stock')
def calculateStockValue():
    products = Product.query.all()
    
    total_stock_value = sum(product.price * product.stock for product in products)
    totalStock = sum(product.stock for product in products)
    
    product_stock_details = [(product.name, product.stock, product.price * product.stock) for product in products]
    
    return render_template('stock/calculateStockValue.html', total_stock_value=total_stock_value, totalStock=totalStock, product_stock_details=product_stock_details)


@app.route('/informe-stock')
def informeStock():
    products = Product.query.all()
    categories = Category.query.all()
    suppliers = Supplier.query.all()
    storages = Storage.query.all()
    
    # Función para calcular el stock total por categoría
    def categoryStock(category):
        return sum(product.stock for product in products if product.category_id == category.id)

    # Función para calcular el stock total por proveedor
    def supplierStock(supplier):
        return sum(product.stock for product in products if product.supplier_id == supplier.id)

    # Función para calcular el stock total por bodega
    def storageStock(storage):
        return sum(product.stock for product in products if product.storage_id == storage.id)

    stock_total = sum(product.stock for product in products)

    return render_template(
        'stock/reportStock.html',
        stock_total=stock_total,
        categories=categories,
        suppliers=suppliers,
        storages=storages,
        categoryStock=categoryStock,
        supplierStock=supplierStock,
        storageStock=storageStock
    )

if __name__ == '__main__':
    app.run(debug=True)