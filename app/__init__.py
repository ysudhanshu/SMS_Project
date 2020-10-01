"""
Flask app factory
"""

import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT, current_identity
from jinja2.runtime import identity

from .resources import flow_api
from .models.models import db
from .resources.controller import CommodityResource, ChemicalElementsResource, ChemicalCompositionResource
from .utils import commands
from .resources.manager import authenticate, identity


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_envvar('REST_API_APP')

    db.init_app(app)
    commands.init_app(app)

    api = Api(app)
    jwt = JWT(app, authenticate, identity)

    api.add_resource(CommodityResource, '/commodity/<int:id>')
    api.add_resource(ChemicalElementsResource, '/chemical-elements')
    api.add_resource(ChemicalCompositionResource, '/chemical-composition', '/chemical-composition/<int:id>')


    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
