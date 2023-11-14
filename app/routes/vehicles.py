# app/routes/vehicles.py

from flask import Blueprint, request
from app.models import Vehicles 
from app import db

vehicles_bp = Blueprint('vehicles', __name__)

@vehicles_bp.route('/all', methods=['GET'])
def get_all_vehicles():
    # Lógica para obtener todos los vehículos
    return "Lista de vehículos"

@vehicles_bp.route('/<int:id>', methods=['GET'])
def get_vehicle(id):
    # Lógica para obtener un vehículo por id
    return "Vehículo con id {}".format(id)

@vehicles_bp.route('/<int:id>', methods=['PUT'])
def update_vehicle(id):
    # Lógica para actualizar un vehículo por id
    return "Vehículo con id {} actualizado".format(id)

@vehicles_bp.route('/<int:id>', methods=['DELETE'])
def delete_vehicle(id):
    # Lógica para eliminar un vehículo por id
    return "Vehículo con id {} eliminado".format(id)

@vehicles_bp.route('/new', methods=['POST'])
def create_vehicle():
    data = request.json
    brand = data.get('brand')
    model = data.get('model')
    year = data.get('year')
    motor = data.get('motor')

    new_vehicle = Vehicles(brand, model, year, motor)
    
    db.session.add(new_vehicle)
    db.session.commit()
    # Lógica para crear un vehículo
    return "Vehículo creado"
# Otros endpoints según sea necesario
