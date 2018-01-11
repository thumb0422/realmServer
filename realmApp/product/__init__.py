#-*- coding: UTF-8 -*-
'''
产品相关信息
'''

from flask import Blueprint

product = Blueprint('product', __name__)

from . import views,errors