# -*- coding=utf-8 -*-
'''
提供给app作为apiServer
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

from flask_login import LoginManager
loginManager = LoginManager()

def create_app(config_name):
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    app.config['SECRET_KEY'] = '0okmnji98uhb'

    loginManager.login_view = '/admin/login'
    loginManager.session_protection = "strong"
    loginManager.login_message = u"请登录！"
    loginManager.login_message_category = "info"
    from datetime import timedelta
    '''cookie 的默认有效期'''
    loginManager.remember_cookie_duration = timedelta(days=1)
    loginManager.init_app(app)
    # 可以设置None,'basic','strong'  以提供不同的安全等级,一般设置strong,如果发现异常会登出用户

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

    from .userAdmin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    return app
