from datetime import datetime
from flask import Blueprint, request, jsonify, send_file
from openpyxl import Workbook
from app.models import Sells
from io import BytesIO
import csv
from reportlab.pdfgen import canvas
from app import db

sells_bp = Blueprint('sells', __name__, url_prefix='/api/sells')

@sells_bp.route('/add', methods=['POST'])
def add_sell():
    data = request.json
    product_id = data.get('product_id')
    brand = data.get('brand')
    model = data.get('model')
    year = data.get('year')
    price = data.get('price')

    # Obtén la fecha y hora actual
    current_datetime = datetime.now()
    purchase_date = current_datetime.date()
    purchase_time = current_datetime.time()

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

@sells_bp.route('/export/excel', methods=['GET'])
def export_excel():
    try:
        sells_query = db.session.query(Sells).all()

        # Crear un archivo Excel en memoria
        workbook = Workbook()
        sheet = workbook.active
        sheet.append(['ID', 'Product ID', 'Brand', 'Model', 'Price'])  # Fila de encabezado

        # Agregar datos de ventas al Excel
        for sell in sells_query:
            sheet.append([sell.id, sell.product_id, sell.brand, sell.model, sell.price])

        # Configurar la respuesta del servidor
        excel_file = BytesIO()
        workbook.save(excel_file)
        excel_file.seek(0)

        return send_file(
            excel_file,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name='ventas_reporte.xlsx'
        )

    except Exception as e:
        return jsonify({'message': 'Error al exportar a Excel', 'error': str(e)}), 500
    
@sells_bp.route('/export/pdf', methods=['GET'])
def export_pdf():
    try:
        sells_query = db.session.query(Sells).all()

        # Crear un archivo PDF en memoria
        pdf_buffer = BytesIO()
        pdf = canvas.Canvas(pdf_buffer)

        # Configurar el encabezado
        pdf.setFont("Helvetica", 12)
        pdf.drawString(100, 800, "Reporte de Ventas")

        # Agregar datos de ventas al PDF
        y_position = 780
        for sell in sells_query:
            sell_info = f"ID: {sell.id}, Product ID: {sell.product_id}, Brand: {sell.brand}, Model: {sell.model}, Price: {sell.price}"
            pdf.drawString(100, y_position, sell_info)
            y_position -= 20

        # Guardar el PDF en memoria
        pdf.save()
        pdf_buffer.seek(0)

        return send_file(
            pdf_buffer,
            mimetype='application/pdf',
            as_attachment=True,
            download_name='ventas_reporte.pdf'
        )

    except Exception as e:
        return jsonify({'message': 'Error al exportar a PDF', 'error': str(e)}), 500
