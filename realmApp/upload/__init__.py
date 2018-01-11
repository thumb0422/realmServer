#-*- coding: UTF-8 -*-
'''
图片资源上传下载
'''

from flask import Blueprint

upload = Blueprint('upload', __name__)

from . import views,errors