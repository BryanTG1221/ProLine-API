from flask import Blueprint, request, jsonify
from app.models import Sells
from app import db

sells_bp = Blueprint('sells', __name__, url_prefix='/api/sells')

# Endpoint para agregar una venta
@sells_bp.route('/add', methods=['POST'])
def add_sell():
    data = request.json
    product_id = data.get('product_id')
    purchase_date = data.get('purchase_date')
    purchase_time = data.get('purchase_time')

    new_sell = Sells(product_id=product_id, purchase_date=purchase_date, purchase_time=purchase_time)

    try:
        db.session.add(new_sell)
        db.session.commit()
        return jsonify({'message': 'Venta registrada con éxito'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error al registrar la venta', 'error': str(e)}), 500

# Endpoint para obtener todas las ventas
@sells_bp.route('/', methods=['GET'])
def get_all_sells():
    sells = Sells.query.all()
    sells_list = [{'id': sell.id, 'product_id': sell.product_id, 'purchase_date': str(sell.purchase_date), 'purchase_time': str(sell.purchase_time)} for sell in sells]
    return jsonify({'sells': sells_list})

# Endpoint para obtener detalles de una venta específica por su ID
@sells_bp.route('/<int:sell_id>', methods=['GET'])
def get_sell(sell_id):
    sell = Sells.query.get(sell_id)

    if sell:
        sell_details = {'id': sell.id, 'product_id': sell.product_id, 'purchase_date': str(sell.purchase_date), 'purchase_time': str(sell.purchase_time)}
        return jsonify(sell_details)
    else:
        return jsonify({'message': 'Venta no encontrada'}), 404
