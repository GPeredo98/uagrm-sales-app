from models.producto import ProductoSchema
from sqlalchemy.orm import relationship
from utilities import database as db, add_schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields

@add_schema()
class VentaDetalle(db.Model):

    __tablename__ = 'ventas_detalle'

    id = db.Column(db.Integer, primary_key=True)
    fk_venta = db.Column(db.Integer, db.ForeignKey('ventas.id'), nullable=False)
    fk_producto = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)

    producto = relationship("Producto")

    def __init__(self, fk_producto, fk_venta):
        self.fk_producto = fk_producto
        self.fk_venta = fk_venta

    def __str__(self):
        return self.id


class VentaDetalleSchema(SQLAlchemyAutoSchema):
    producto = fields.Nested(ProductoSchema)  # Assuming a 'producto' relationship in VentaDetalle

    class Meta:
        model = VentaDetalle