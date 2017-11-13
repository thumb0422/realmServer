#-*- coding: UTF-8 -*-
'''
订单相关信息
'''

from flask import Blueprint

order = Blueprint('order', __name__)

from . import views,errors