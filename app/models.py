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
    is_deleted = db.Column(db.Boolean, default=False)
    is_deleted = db.Column(db.Boolean, default=False)

    def __init__(self, brand, model, year=None, motor=None, traction=None, speedMax=None, power=None, stock=None, type=None, price=None, urlImage=None):
        self.brand = brand
        self.model = model
        self.year = year
        self.motor = motor
        self.traction = traction
        self.speedMax = speedMax
        self.power = power
        self.stock = stock
        self.type = type
        self.price = price
        self.urlImage = urlImage
        self.is_deleted = False

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
    is_deleted = db.Column(db.Boolean, default=False)

    def __init__(self, brand, model, year, cylinder, speedMax, stock, price, urlImage):
        self.brand = brand
        self.model = model
        self.year = year
        self.cylinder = cylinder
        self.speedMax = speedMax
        self.stock = stock
        self.price = price
        self.urlImage = urlImage


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    position = db.Column(db.String(50), nullable=True)
    department = db.Column(db.String(50), nullable=True)
    password_hash = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    is_employee = db.Column(db.Boolean, nullable=False)

    def set_password(self, password):
        hash_object = hashlib.sha256()
        textInBytes = password.encode('utf-8')
        hash_object.update(textInBytes)
        hash_hex = hash_object.hexdigest()
        return hash_hex

    def check_password(self, password):
        hashed_password = self.set_password(password)
        return self.password_hash == hashed_password

    def __init__(self, name, lastname, email, is_active, is_employee, password_hash, position=None, department=None):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.position = position
        self.department = department
        self.password_hash = self.set_password(password_hash)
        self.is_active = is_active
        self.is_employee = is_employee



class Whitelist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(255), nullable=False)

    def __init__(self, token):
        self.token = token


class Sells(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    purchase_date = db.Column(db.Date, nullable=False)
    purchase_time = db.Column(db.Time, nullable=False)
    brand = db.Column(db.String(50))
    model = db.Column(db.String(50))
    year = db.Column(db.Integer)
    price = db.Column(db.Float)

    def __init__(self, product_id, purchase_date, purchase_time, brand=None, model=None, year=None, price=None):
        self.product_id = product_id
        self.purchase_date = purchase_date
        self.purchase_time = purchase_time
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    logo_url = db.Column(db.Text, nullable=False)
    is_car = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, logo_url, is_car):
        self.name = name
        self.logo_url = logo_url
        self.is_car = is_car