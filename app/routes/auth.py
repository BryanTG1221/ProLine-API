from flask import Blueprint, request, jsonify
from app.models import Employee, Whitelist
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from app import db
import jwt, hashlib

secret = 'proline'

def check_password (passwordToCheck):
    hash_object = hashlib.sha256()
    passwordUser = passwordToCheck.encode('utf-8')
    hash_object.update(passwordUser)
    passwordUserHash = hash_object.hexdigest()
    return passwordUserHash


def write_token(payload: dict):    
    token_bytes = jwt.encode(payload, secret, algorithm='HS256')
    return token_bytes

def validate_token(encoded_jwt):
    try:
        response = jwt.decode(encoded_jwt, secret, algorithms=['HS256'])
        return response
    except jwt.exceptions.DecodeError:
        return "Token no valido"


auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    employeeExits = Employee.query.filter_by(email=email, password_hash=check_password(password)).first()
    payload = { 'email': email, 'password': password }
    tokenUser = write_token(payload)
    try:
        if employeeExits and check_password(password):
              return jsonify({'message': 'Inicio de sesión exitoso', 'token': tokenUser})
        else:
            raise Exception()
    except Exception as e:
        return jsonify({'message': 'Credenciales incorrectas'}), 401

@auth_bp.route('/add', methods=['POST'])
def create():
    data = request.json
    name = data.get('name')
    lastname = data.get('lastname')
    email = data.get('email')
    position = data.get('position')
    department = data.get('department')
    password = data.get('password')
    new_employee = Employee(name, lastname, email, position, department, password)
    payload = {'email': email, 'password': password}
    tokenUser = write_token(payload)
    new_whitelist = Whitelist(tokenUser)
    try:
        db.session.add(new_employee)
        db.session.add(new_whitelist)
        db.session.commit()
        return jsonify({'message': 'Usuario creado con exito'}), 201
    except IntegrityError as e:
        db.session.rollback()
        if "duplicate key" in str(e):
            return jsonify({'message': 'El correo ya esta registrado', 'error': str(e)}), 409
        else:
            return jsonify({'message': 'Hubo un error de integridad en la base de datos', 'error': str(e)}), 401
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'message': 'Hubo un error en la base de datos', 'error': str(e)}), 401
    except Exception as e:
        return jsonify({'message': 'Hubo un error ', 'error': str(e)}), 401