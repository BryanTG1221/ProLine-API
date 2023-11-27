from flask import Blueprint, request, jsonify
from app.models import Sells
from app import db

sells_bp = Blueprint('sells', __name__, url_prefix='/api/sells')

@sells_bp.route('/add', methods=['POST'])
def add_sell():
    data = request.json
    product_id = data.get('product_id')
    purchase_date = data.get('purchase_date')
    purchase_time = data.get('purchase_time')
    brand = data.get('brand')
    model = data.get('model')
    year = data.get('year')
    price = data.get('price')

    new_sell = Sells(
        product_id=product_id,
        purchase_date=purchase_date,
        purchase_time=purchase_time,
        brand=brand,
        model=model,
        year=year,
        price=price
    )

    try:
        db.session.add(new_sell)
        db.session.commit()
        return jsonify({'message': 'Venta registrada con éxito'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error al registrar la venta', 'error': str(e)}), 500
    

@sells_bp.route('/', methods=['GET'])
def get_all_sells():
    sells_query = db.session.query(Sells).all()

    sells_list = [
        {
            'sell_id': sell.id,
            'product_id': sell.product_id,
            'purchase_date': str(sell.purchase_date),
            'purchase_time': str(sell.purchase_time),
            'brand': sell.brand,
            'model': sell.model,
            'year': sell.year,
            'price': sell.price
        }
        for sell in sells_query
    ]

    return jsonify({'sells': sells_list})


@sells_bp.route('/<int:sell_id>', methods=['GET'])
def get_sell(sell_id):
    sell = Sells.query.get(sell_id)

    if sell:
        sell_details = {
            'sell_id': sell.id,
            'product_id': sell.product_id,
            'purchase_date': str(sell.purchase_date),
            'purchase_time': str(sell.purchase_time),
            'brand': sell.brand,
            'model': sell.model,
            'year': sell.year,
            'price': sell.price
        }

        return jsonify(sell_details)
    else:
        return jsonify({'message': 'Venta no encontrada'}), 404
