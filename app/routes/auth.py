from flask import Blueprint, request, jsonify
from app.models import User, Whitelist
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
    
    # Cambiado el nombre de la variable para reflejar que es un usuario y no solo empleados
    user = User.query.filter_by(email=email, password_hash=check_password(password)).first()

    payload = {'email': email, 'password': password}

    try:
        if user and check_password(password):
            user_data = {
                'name': user.name,
                'lastname': user.lastname,
                'position': user.position,
                'department': user.department,
                'is_employee': user.is_employee
            }
            
            # Modificado para verificar si el usuario es un empleado antes de generar el token
            if user.is_employee:
                token_user = write_token(payload)
                return jsonify({'message': 'Inicio de sesión exitoso', 'token': token_user, 'user': user_data})
            else:
                return jsonify({'message': 'Inicio de sesión exitoso, pero el usuario no es un empleado', 'user': user_data})
        else:
            raise Exception()
    except Exception as e:
        print(e)
        return jsonify({'message': 'Credenciales incorrectas o usuario no encontrado'}), 401


@auth_bp.route('/add', methods=['POST'])
def create():
    data = request.json
    name = data.get('name')
    lastname = data.get('lastname')
    email = data.get('email')
    position = data.get('position')
    department = data.get('department')
    password = data.get('password')
    is_employee = data.get('is_employee')
    is_active = data.get('is_active')
    print(is_employee)
    new_User = User(name, lastname, email, is_active, is_employee, password, position, department)
    payload = {'email': email, 'password': password}
    tokenUser = write_token(payload)
    new_whitelist = Whitelist(tokenUser)
    try:
        db.session.add(new_User)
        db.session.add(new_whitelist)
        db.session.commit()
        return jsonify({'message': 'Usuario creado con éxito'}), 201
    except IntegrityError as e:
        db.session.rollback()
        if "duplicate key" in str(e):
            return jsonify({'message': 'El correo ya está registrado', 'error': str(e)}), 409
        else:
            return jsonify({'message': 'Hubo un error de integridad en la base de datos', 'error': str(e)}), 401
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'message': 'Hubo un error en la base de datos', 'error': str(e)}), 401
    except Exception as e:
        return jsonify({'message': 'Hubo un error ', 'error': str(e)}), 401

    

@auth_bp.route('/employees', methods=['GET'])
def get_non_clients():
    non_clients = User.query.filter_by(is_employee=True).all()

    non_clients_list = []
    for user in non_clients:
        user_data = {
            'id': user.id,
            'name': user.name,
            'lastname': user.lastname,
            'email': user.email,
            'position': user.position,
            'department': user.department,
            'is_active': user.is_active
        }
        non_clients_list.append(user_data)

    return jsonify({'employees': non_clients_list})

@auth_bp.route('/clients', methods=['GET'])
def get_clients():
    clients = User.query.filter_by(is_employee=False).all()

    clients_list = []
    for user in clients:
        user_data = {
            'id': user.id,
            'name': user.name,
            'lastname': user.lastname,
            'email': user.email,
            'position': user.position,
            'department': user.department,
            'is_active': user.is_active
        }
        clients_list.append(user_data)

    return jsonify({'clients': clients_list})
