# app/models.py

from app import db
import hashlib

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer)
    motor = db.Column(db.String(50), nullable=False)
    traction = db.Column(db.String(50), nullable=False)
    speedMax = db.Column(db.Integer, nullable=False)
    power = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    urlImage = db.Column(db.Text, nullable=False)

    def __init__(self, brand, model, year, motor, traction, stock, price, urlImage):
        self.brand = brand
        self.model = model
        self.year = year
        self.motor = motor
        self.traction = traction
        self.stock = stock
        self.price = price
        self.urlImage = urlImage


class Motorcycles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer)
    cylinder = db.Column(db.Integer)
    speedMax = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    price = db.Column(db.Float, nullable=False)
    urlImage = db.Column(db.Text, nullable=False)

    def __init__(self, brand, model, year, cylinder, speedMax, stock, price, urlImage):
        self.brand = brand
        self.model = model
        self.year = year
        self.cylinder = cylinder
        self.speedMax = speedMax
        self.stock = stock
        self.price = price
        self.urlImage = urlImage


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    position = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def set_password(self, password):
        hash_object = hashlib.sha256()
        textInBytes = password.encode('utf-8')
        hash_object.update(textInBytes)
        hash_hex = hash_object.hexdigest()
        return hash_hex
    
    def __init__(self, name, lastname, email, position, department, password_hash, is_active=True):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.position = position
        self.department = department
        self.password_hash = self.set_password(password_hash)
        self.is_active = is_active

        

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(15))
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        hash_object = hashlib.sha256()
        textInBytes = password.encode('utf-8')
        hash_object.update(textInBytes)
        hash_hex = hash_object.hexdigest()
        return hash_hex
    
    def __init__(self, name, lastname ,email, address, phone_number, password_hash):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.address = address
        self.phone_number = phone_number
        self.password_hash = self.set_password(password_hash)


class Whitelist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(255), nullable=False)

    def __init__(self, token):
        self.token = token