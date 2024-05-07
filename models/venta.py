from utilities import database as db, add_schema
from models.venta_detalle import VentaDetalleSchema
from sqlalchemy.orm import relationship
from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields


class Venta(db.Model):

    __tablename__ = 'ventas'

    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100), nullable=False)
    razon_social = db.Column(db.String(300))
    nit = db.Column(db.String(300))
    fecha_creacion = db.Column(db.DateTime, default=datetime.now())

    productos = relationship("VentaDetalle", backref="venta", lazy="dynamic")
        
    def __init__(self, cliente, razon_social, nit):
        self.cliente = cliente
        self.razon_social = razon_social
        self.nit = nit

    def __str__(self):
        return self.id

class VentaSchema(SQLAlchemyAutoSchema):
    productos = fields.Nested(VentaDetalleSchema, many=True)

    class Meta:
        model = Venta
        include_relationships = True