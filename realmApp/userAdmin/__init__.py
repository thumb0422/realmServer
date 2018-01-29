#-*- coding: UTF-8 -*-
''''数据库连接'''

from flask import Blueprint

admin = Blueprint('/admin', __name__)

from . import view

