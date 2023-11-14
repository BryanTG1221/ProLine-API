# app/models.py

from app import db
import hashlib

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer)
    motor = db.Column(db.String(50), nullable=False)
    # Agrega más campos según sea necesario

    def __init__(self, brand, model, year, motor):
        self.brand = brand
        self.model = model
        self.year = year
        self.motor = motor

class Motorcycles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer)
    # Agrega más campos según sea necesario

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    position = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        hash_object = hashlib.sha256()
        textInBytes = password.encode('utf-8')
        hash_object.update(textInBytes)
        hash_hex = hash_object.hexdigest()
        return hash_hex
    
    def __init__(self, name, lastname ,email, position, department, password_hash):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.position = position
        self.department = department
        self.password_hash = self.set_password(password_hash)
        

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