# app/routes/motorcycles.py

from flask import Blueprint, request, jsonify
from app.models import Motorcycles
from app import db

motorcycles_bp = Blueprint('motorcycles', __name__)

@motorcycles_bp.route('/', methods=['GET'])
def get_all_motorcycles():
    motorcycles = Motorcycles.query.all()
    result = []
    for motorcycle in motorcycles:
        result.append({
            'id': motorcycle.id,
            'brand': motorcycle.brand,
            'model': motorcycle.model,
            'year': motorcycle.year,
            'cylinder': motorcycle.cylinder,
            'speedMax': motorcycle.speedMax,
            'stock': motorcycle.stock,
            'price': motorcycle.price,
            'urlImage': motorcycle.urlImage
        })
    return jsonify(result)

@motorcycles_bp.route('/<int:id>', methods=['GET'])
def get_motorcycle(id):
    motorcycle = Motorcycles.query.get(id)
    if motorcycle:
        return jsonify({
            'id': motorcycle.id,
            'brand': motorcycle.brand,
            'model': motorcycle.model,
            'year': motorcycle.year,
            'cylinder': motorcycle.cylinder,
            'speedMax': motorcycle.speedMax,
            'stock': motorcycle.stock,
            'price': motorcycle.price,
            'urlImage': motorcycle.urlImage
        })
    return jsonify({'message': 'Motocicleta no encontrada'}), 404

@motorcycles_bp.route('/<int:id>', methods=['PUT'])
def update_motorcycle(id):
    try:
        motorcycle = Motorcycles.query.get(id)
        if motorcycle:
            data = request.json
            motorcycle.brand = data.get('brand', motorcycle.brand)
            motorcycle.model = data.get('model', motorcycle.model)
            motorcycle.year = data.get('year', motorcycle.year)
            motorcycle.cylinder = data.get('cylinder', motorcycle.cylinder)
            motorcycle.speedMax = data.get('speedMax', motorcycle.speedMax)
            motorcycle.stock = data.get('stock', motorcycle.stock)
            motorcycle.price = data.get('price', motorcycle.price)
            motorcycle.urlImage = data.get('urlImage', motorcycle.urlImage)
            motorcycle.is_deleted = data.get('is_deleted', motorcycle.is_deleted)
            db.session.commit()
            return jsonify({'message': 'Motocicleta actualizada correctamente'})
        return jsonify({'message': 'Motocicleta no encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@motorcycles_bp.route('/<int:id>', methods=['DELETE'])
def delete_motorcycle(id):
    try:
        motorcycle = Motorcycles.query.get(id)
        if motorcycle:
            motorcycle.is_deleted = True
            db.session.commit()
            return jsonify({'message': 'Motocicleta marcada como eliminada correctamente'}), 200
        return jsonify({'message': 'Motocicleta no encontrada'}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@motorcycles_bp.route('/', methods=['POST'])
def create_motorcycle():
    try:
        data = request.json
        new_motorcycle = Motorcycles(
            brand=data.get('brand'),
            model=data.get('model'),
            year=data.get('year'),
            cylinder=data.get('cylinder'),
            speedMax=data.get('speedMax'),
            stock=data.get('stock'),
            price=data.get('price'),
            urlImage=data.get('urlImage')
        )

        db.session.add(new_motorcycle)
        db.session.commit()
        return jsonify({'message': 'Motocicleta creada correctamente'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
