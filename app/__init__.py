# -*- coding=utf-8 -*-
'''
提供给app作为apiServer
'''

from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):
    """
    binding extensions to app
    regist blue prients
    """
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config[config_name])
    # config[config_name].init_app(app)

    db.init_app(app)
    with app.app_context():
        db.create_all()
        # Extensions like Flask-SQLAlchemy now know what the "current" app
        # is while within this block. Therefore, you can now run........

        # from .init_seed import init_DB_data
        # init_DB_data(db)

    # bootstrap.init_app(app)
    # login_manager.init_app(app)

    # from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint)
    #
    # from .admin import views
    # from .admin import admin as admin_blueprint
    # app.register_blueprint(admin_blueprint, url_prefix='/admin')

    return app