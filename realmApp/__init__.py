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

# def create_app(config_name):
#     """
#     binding extensions to realmApp
#     regist blue prients
#     """
#     realmApp = Flask(__name__, template_folder='templates')
#     realmApp.config.from_object(config[config_name])
#     # config[config_name].init_app(realmApp)
#
#     db.init_app(realmApp)
#     with realmApp.app_context():
#         db.create_all()
#         # Extensions like Flask-SQLAlchemy now know what the "current" realmApp
#         # is while within this block. Therefore, you can now run........
#
#         # from .init_seed import init_DB_data
#         # init_DB_data(db)
#
#     from .order import order as order_blueprint
#     realmApp.register_blueprint(order_blueprint)
#
#     from .user import user as user_blueprint
#     realmApp.register_blueprint(user_blueprint)
#
#     return realmApp
