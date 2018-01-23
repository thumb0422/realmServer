# -*- coding=utf-8 -*-
'''
提供给app作为apiServer
'''

from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_nav import Nav
from flask_nav.elements import *

db = SQLAlchemy()

nav = Nav()

# registers the "top" menubar
nav.register_element(
    'top',
    Navbar(
        View('产品展示', 'upload.index'),
        View('产品信息维护', 'upload.infoAdd'),
        View('产品类型维护', 'upload.typeAdd'),
        # Subgroup('Products',
        #          View('Wg240-Series',
        #               'products',
        #               product='wg240'),
        #          View('Wg250-Series',
        #               'products',
        #               product='wg250'),
        #          Separator(),
        #          Text('Discontinued Products'),
        #          View('Wg10X',
        #               'products',
        #               product='wg10x'), ),
        # Link('Tech Support', 'http://techsupport.invalid/widgits_inc'),
    )
)

def create_app(config_name):
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    nav.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    from .order import order as order_blueprint
    app.register_blueprint(order_blueprint,url_prefix='/order')

    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/user')

    from .product import product as product_blueprint
    app.register_blueprint(product_blueprint, url_prefix='/product')

    from .upload import upload as upload_blueprint
    app.register_blueprint(upload_blueprint, url_prefix='/upload')

    return app
