# -*- coding=utf-8 -*-
'''
提供给app作为apiServer
'''

from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    from .order import order as order_blueprint
    app.register_blueprint(order_blueprint,url_prefix='/order')

    return app
