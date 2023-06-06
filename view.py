from flask import jsonify

from models import Shipment


class ShipmentSchema:
    pass


def get(id=None):
    """
    get Shipment
    """
    try:
        if id is None:
            shipment = Shipment.query.filter().all()
            shipment_schema =  ShipmentSchema(many=True)
            return shipment_schema.jsonify(shipment)
        else:
            shipment = Shipment.query.filter_by(id=id).first()
            shipment_schema = ShipmentSchema()
            return shipment_schema.jsonify(shipment)
    except Exception as e:
        return jsonify({"error": "There was an error please contact the administrator"})
