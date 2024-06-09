from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Tabla de asociación para la relación muchos a muchos con cantidad
storage_product = db.Table('storage_product',
    db.Column('storage_id', db.Integer, db.ForeignKey('storage.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True),
    db.Column('amount', db.Integer, nullable=False, default=0)
)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    products = db.relationship('Product', backref='category', lazy=True)

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    cellphone = db.Column(db.String(50), nullable=False)
    products = db.relationship('Product', backref='supplier', lazy=True)

class Storage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    max_capacity = db.Column(db.Integer, nullable=False)
    products = db.relationship('Product', backref='storage', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=False)
    storage_id = db.Column(db.Integer, db.ForeignKey('storage.id'), nullable=True)
