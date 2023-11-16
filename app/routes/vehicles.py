# app/routes/vehicles.py

from flask import Blueprint, request, jsonify
from app.models import Vehicles
from app import db

vehicles_bp = Blueprint('vehicles', __name__)

vehicles_bp.route('/', methods=['GET'])
def get_all_vehicles():
    vehicles = Vehicles.query.filter_by(is_deleted=False).all()
    result = []
    for vehicle in vehicles:
        result.append({
            'id': vehicle.id,
            'brand': vehicle.brand,
            'model': vehicle.model,
            'year': vehicle.year,
            'motor': vehicle.motor,
            'traction': vehicle.traction,
            'speedMax': vehicle.speedMax,
            'power': vehicle.power,
            'stock': vehicle.stock,
            'type': vehicle.type,
            'price': vehicle.price,
            'urlImage': vehicle.urlImage
        })
    return jsonify(result)

@vehicles_bp.route('/<int:id>', methods=['GET'])
def get_vehicle(id):
    vehicle = Vehicles.query.get(id)
    if vehicle:
        return jsonify({
            'id': vehicle.id,
            'brand': vehicle.brand,
            'model': vehicle.model,
            'year': vehicle.year,
            'motor': vehicle.motor,
            'traction': vehicle.traction,
            'speedMax': vehicle.speedMax,
            'power': vehicle.power,
            'stock': vehicle.stock,
            'type': vehicle.type,
            'price': vehicle.price,
            'urlImage': vehicle.urlImage
        })
    return jsonify({'message': 'Vehículo no encontrado'}), 404

@vehicles_bp.route('/<int:id>', methods=['PUT'])
def update_vehicle(id):
    try:
        vehicle = Vehicles.query.get(id)
        if vehicle:
            data = request.json
            vehicle.brand = data.get('brand', vehicle.brand)
            vehicle.model = data.get('model', vehicle.model)
            vehicle.year = data.get('year', vehicle.year)
            vehicle.motor = data.get('motor', vehicle.motor)
            vehicle.traction = data.get('traction', vehicle.traction)
            vehicle.speedMax = data.get('speedMax', vehicle.speedMax)
            vehicle.power = data.get('power', vehicle.power)
            vehicle.stock = data.get('stock', vehicle.stock)
            vehicle.type = data.get('type', vehicle.type)
            vehicle.price = data.get('price', vehicle.price)
            vehicle.urlImage = data.get('urlImage', vehicle.urlImage)
            vehicle.is_deleted = data.get('is_deleted', vehicle.is_deleted)
            db.session.commit()
            return jsonify({'message': 'Vehículo actualizado correctamente'})
        return jsonify({'message': 'Vehículo no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@vehicles_bp.route('/<int:id>', methods=['DELETE'])
def delete_vehicle(id):
    try:
        vehicle = Vehicles.query.get(id)
        if vehicle:
            vehicle.is_deleted = True
            db.session.commit()
            return jsonify({'message': 'Vehículo marcado como eliminado correctamente'}), 200
        return jsonify({'message': 'Vehículo no encontrado'}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@vehicles_bp.route('/', methods=['POST'])
def create_vehicle():
    try:
        data = request.json
        new_vehicle = Vehicles(
            brand=data.get('brand'),
            model=data.get('model'),
            year=data.get('year'),
            motor=data.get('motor'),
            traction=data.get('traction'),
            speedMax= data.get('speedMax'),
            power=data.get('power'),
            stock=data.get('stock'),
            type=data.get('type'),
            price=data.get('price'),
            urlImage=data.get('urlImage')
        )

        db.session.add(new_vehicle)
        db.session.commit()
        return jsonify({'message': 'Vehículo creado correctamente'}), 201 
    except Exception as e:
        db.session.rollback() 
        return jsonify({'error': str(e)}), 500  

