# app/routes/motorcycles.py

from flask import Blueprint, jsonify
from app.models import Brand

brands_bp = Blueprint('brands', __name__, url_prefix='/api/brands')


@brands_bp.route('/cars', methods=['GET'])
def get_car_brands():
    car_brands = Brand.query.filter_by(is_car=True).all()
    car_brands_data = [{'id': brand.id, 'name': brand.name, 'logo_url': brand.logo_url} for brand in car_brands]
    return jsonify({'car_brands': car_brands_data})

@brands_bp.route('/motorcycles', methods=['GET'])
def get_motorcycle_brands():
    motorcycle_brands = Brand.query.filter_by(is_car=False).all()
    motorcycle_brands_data = [{'id': brand.id, 'name': brand.name, 'logo_url': brand.logo_url} for brand in motorcycle_brands]
    return jsonify({'motorcycle_brands': motorcycle_brands_data})
