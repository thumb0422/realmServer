#-*- coding: UTF-8 -*-
''''数据库连接'''
from flask_login import LoginManager
from realmApp import db
from realmApp.model import Session
from manage import app


from flask import Blueprint

admin = Blueprint('/upload/admin', __name__)
from . import view


loginManager = LoginManager()
loginManager.init_app(app)
loginManager.login_view = 'login'


db = db
Session = Session
