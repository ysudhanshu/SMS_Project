#!-*- coding: utf-8 -*-!
"""
This file contains model definition 
"""

from sqlalchemy.orm import backref

from . import db
from .base_model import BaseModel


class ChemicalComposition(db.Model, BaseModel):

    """
    Model definition for Chemical Element"
    id - id of the element
    name - name of the element
    """

    __tablename__ = "chemical_composition"

    def __init__(self,commodity_id, element_id, percentage, **kwargs):
        super(ChemicalComposition, self).__init__(**kwargs)
        self.commodity_id = commodity_id
        self.element_id = element_id
        self.percentage = percentage

    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    commodity_id = db.Column(db.Integer, db.ForeignKey('commodity.id'))
    element_id = db.Column(db.Integer, db.ForeignKey('chemical_element.id'))
    percentage = db.Column(db.Float(precision=2))


    # relationships
    
    element = db.relationship('ChemicalElement', backref=db.backref('element', lazy=True))

    def json(self):
        element_name = None
        element = ChemicalElement.find_by_id(self.element_id)
        if element:
            element_name = element.json()['name']
        return {
            "element": {"id": self.element_id, "name": element_name},
            "percentage": self.percentage
        }

class ChemicalElement(db.Model, BaseModel):

    """
    Model definition for Chemical Element"
    id - id of the element
    name - name of the element
    """

    __tablename__ = "chemical_element"

    def __init__(self, id, name, **kwargs):
        super(ChemicalElement, self).__init__(**kwargs)
        self.id = id
        self.name = name

    
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(255))

    def json(self):
        return {
            "id": self.id,
            "name": self.name
        }


class Commodity(db.Model, BaseModel):

    """
    Model definition for commodity
    - id - id of the commodity
    - name - name of the commodity
    - inventory - current amount of the commodity on stock (in tons)
    - price - current price of the commodity ($/ton)
    - chemical_composition - chemical elements and their percentage in the commodity.
    """

    __tablename__ = "commodity"

    def __init__(self, id, name, inventory, price, **kwargs):
        super(Commodity, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.inventory = inventory
        self.price = price


    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    inventory = db.Column(db.Float(precision=2))
    price = db.Column(db.Float(precision=2))

    # relationship
    chemical_composition = db.relationship('ChemicalComposition', backref=db.backref('commodity', lazy='joined'))


    def json(self):
        composition= list(map(lambda x:x.json(), ChemicalComposition.query.filter_by(commodity_id=self.id).all()))
        percentage = 0
  
        for element in composition:

            percentage += element['percentage']

        if percentage < 100:
            composition.append(
                {
                    "element": {"id": 9999, "name": "Unknown"},
                    "percentage": 100 - percentage
                }
            )

        return {
            "id": self.id,
            "name": self.name,
            "inventory": self.inventory,
            "price":self.price,
            "chemical_composition": composition
        }


class User(db.Model, BaseModel):

    """
    Model definition for User
    id = id of the user
    user_id = user_id of the user
    email = email of the user
    name = name of user
    password = password for user
    """

    __tablename__ = "user"

    def __init__(self, id, username, password, **kwargs):
        super(User, self).__init__(**kwargs)
        self.id = id
        self.username = username
        self.password = password
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))


    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()


    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id)