"""
Controller contains all the rest endpoints definition
"""

from flask.globals import request
from flask import jsonify, request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from flasgger import swag_from


from ..models.models import ChemicalComposition, Commodity, ChemicalElement


class CommodityResource(Resource):

    @jwt_required()
    @swag_from('swags/commodity_resource.yml')
    def get(self, id):

        data =  Commodity.find_by_id(id)
        if data:
            return data.json(), 200


    @jwt_required()
    def put(self, id):

        data = request.get_json()
    
        commodity = Commodity.find_by_id(id)

        if commodity:
            commodity.name, commodity.inventory, commodity.price = data['name'], data['inventory'], data['price']
        else:
            commodity = Commodity(id, data['name'], data['inventory'], data['price'])
        commodity.save_to_db()
        return {"message": "data updated"}, 200
        


class ChemicalElementsResource(Resource):

    @jwt_required()
    def get(self):
        return (list(map(lambda x:x.json(), ChemicalElement.query.all())))


class ChemicalCompositionResource(Resource):

    @jwt_required()
    def post(self):
        data = request.get_json()
        chem_composition = ChemicalComposition(data['commodity_id'], data['element_id'], data['percentage'])
        chem_composition.save_to_db()
        return chem_composition.json(), 200


    @jwt_required
    def delete(self, id):
        data = request.get_json()
        chem_composition = ChemicalComposition.query.filter_by(commodity_id=id).filter_by(element_id=data['element_id']).first()
        if chem_composition:
            chem_composition.delete_from_db()
            return {"message": "data deleted "}
        return {"message": "data not found"}, 400