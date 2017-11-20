#-*- coding: UTF-8 -*-
'''
用户相关信息
'''

from flask import Blueprint

user = Blueprint('user', __name__)

from . import views,errors