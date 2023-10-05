from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata = metadata)

#models
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    second_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    email=db.Column(db.String(100), nullable=False)
    password=db.Column(db.String(100), nullable=False)
      
class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    image=db.Column(db.String(255), nullable=False)
    product_name=db.Column(db.String(255), nullable=False)
    description=db.Column(db.String(400), nullable=False)
    type=db.Column(db.String(50), nullable=False)
    supplier_id=db.Column(db.Integer, db.ForeignKey('suppliers.id'), nullable=False)
    quantity=db.Column(db.Integer, nullable=False)
    minimum_stock=db.Column(db.Integer, nullable=False)
    
    #relationships
    # heroes_powers = db.relationship('Hero_powers', back_populates = 'hero')
    purchases= db.relationship('Purchase', back_populates = 'product')
    shippings= db.relationship('Shipping', back_populates = 'product')

class Supplier(db.Model, SerializerMixin):
    __tablename__ = 'suppliers'
    
    id=db.Column(db.Integer, primary_key=True)
    logo=db.Column(db.String(255), nullable=False)
    name=db.Column(db.String(255), nullable=False)
    contact=db.Column(db.String(255), nullable=False)
    
    #relationships
    purchases=db.relationship('Purchase', back_populates ='supplier')
    
class Purchase(db.Model, SerializerMixin):
    __tablename__='purchases'
    
    id=db.Column(db.Integer, primary_key=True)
    supplier_id=db.Column(db.Integer,  db.ForeignKey('suppliers.id'), nullable=True)
    product_id=db.Column(db.Integer, db.ForeignKey('products.id'), nullable=True)
    
    #relationships
    product=db.relationship('Product', back_populates='purchases')
    supplier=db.relationship('Supplier', back_populates='purchases')

class Shipping (db.Model, SerializerMixin):
    __tablename__='shippings'
    
    id=db.Column(db.Integer, primary_key=True)
    product_id=db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    status=db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    #relationships
    product=db.relationship('Product', back_populates ='shippings')
    
    
    