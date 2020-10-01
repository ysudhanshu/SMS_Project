"""
Command line utility for flask
"""

import click
from flask.cli import with_appcontext

from app.models.models import db
from .dataload import load_data


def init_db():
    print("creating database")
    db.create_all()
    print(db)
    print("database created")

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    load_data()
    click.echo('Initialized the database')


def init_app(app):
    app.cli.add_command(init_db_command)