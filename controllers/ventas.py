from flask import Blueprint, jsonify, request
from models.venta_detalle import VentaDetalle
from models.venta import Venta, VentaSchema

from utilities import database as db

ventas = Blueprint('ventas', __name__)


@ventas.route('')
def obtener_ventas():
    try:
        lista_ventas = Venta.query.all()
        venta_schema = VentaSchema(many=True)
        return jsonify(
            {'data': venta_schema.dump(lista_ventas), 'success': True, 'message': 'Ventas listadas'})
    except Exception as e:
        return jsonify({'data': str(e), 'success': False, 'message': 'Ocurrió un error en el servidor'})
    
@ventas.route('/registrar', methods=['POST'])
def registrar_venta():
    try:
        cliente = request.json['cliente']
        razon_social = request.json['razon_social']
        nit = request.json['nit']
        nueva_venta = Venta(cliente, razon_social, nit)
        db.session.add(nueva_venta)
        db.session.commit()
        for producto in request.json['productos']:
            nuevo_detalle_venta = VentaDetalle(producto, nueva_venta.id)
            db.session.add(nuevo_detalle_venta)
        db.session.commit()
        venta_schema = VentaSchema()
        return jsonify({'data': venta_schema.dump(nueva_venta), 'success': True, 'message': 'Venta registrada'})
    except Exception as e:
        return jsonify({'data': str(e), 'success': False, 'message': 'Ocurrió un error en el servidor'})
    