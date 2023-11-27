from flask import Blueprint, request, jsonify
from app.models import User  # Update this import based on your project structure
from app import db

users_bp = Blueprint('users', __name__, url_prefix='/api/users')  

@users_bp.route('/add', methods=['POST'])
def add_user():
    data = request.json
    name = data.get('name')
    lastname = data.get('lastname')
    email = data.get('email')
    position = data.get('position')
    department = data.get('department')
    password_hash = data.get('password_hash')
    is_active = data.get('is_active', True)
    is_employee = data.get('is_employee', True)

    new_user = User(
        name=name,
        lastname=lastname,
        email=email,
        position=position,
        department=department,
        password_hash=password_hash,
        is_active=is_active,
        is_employee=is_employee
    )

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'Usuario registrado con éxito'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error al registrar el usuario', 'error': str(e)}), 500

@users_bp.route('/employees', methods=['GET'])
def get_all_employees():
    employees_query = db.session.query(User).filter_by(is_employee=True).all()

    employees_list = [
        {
            'user_id': user.id,
            'name': user.name,
            'lastname': user.lastname,
            'email': user.email,
            'position': user.position,
            'department': user.department,
            'is_active': user.is_active,
            'is_employee': user.is_employee
        }
        for user in employees_query
    ]

    return jsonify({'employees': employees_list})

@users_bp.route('/clients', methods=['GET'])
def get_all_clients():
    clients_query = db.session.query(User).filter_by(is_employee=False).all()

    clients_list = [
        {
            'user_id': user.id,
            'name': user.name,
            'lastname': user.lastname,
            'email': user.email,
            'position': user.position,
            'department': user.department,
            'is_active': user.is_active,
            'is_employee': user.is_employee
        }
        for user in clients_query
    ]

    return jsonify({'clients': clients_list})


@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)

    if user and user.is_active:
        user_details = {
            'user_id': user.id,
            'name': user.name,
            'lastname': user.lastname,
            'email': user.email,
            'position': user.position,
            'department': user.department,
            'is_active': user.is_active,
            'is_employee': user.is_employee
        }

        return jsonify(user_details)
    else:
        return jsonify({'message': 'Usuario no encontrado'}), 404

@users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)

    if not user or not user.is_active:
        return jsonify({'message': 'Usuario no encontrado'}), 404

    data = request.json
    user.name = data.get('name', user.name)
    user.lastname = data.get('lastname', user.lastname)
    user.email = data.get('email', user.email)
    user.position = data.get('position', user.position)
    user.department = data.get('department', user.department)
    user.is_active = data.get('is_active', user.is_active)
    user.is_employee = data.get('is_employee', user.is_employee)

    try:
        db.session.commit()
        return jsonify({'message': 'Usuario actualizado con éxito'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error al actualizar el usuario', 'error': str(e)}), 500

@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)

    if user and user.is_active:
        # Soft delete by setting is_active to False
        user.is_active = False

        try:
            db.session.commit()
            return jsonify({'message': 'Usuario eliminado con éxito (lógicamente)'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': 'Error al eliminar el usuario (lógicamente)', 'error': str(e)}), 500
    else:
        return jsonify({'message': 'Usuario no encontrado'}), 404
