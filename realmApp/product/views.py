# -*- coding=utf-8 -*-
from . import product
from realmApp.model.model import *
from flask import jsonify,request,make_response,abort,render_template
from realmApp.utility.Response import *
from realmApp.utility import *
from realmApp.model.productAction import *


# 用于测试上传，稍后用到
@product.route('/F3000')
def upload_test():
    return render_template('upload.html')

'''图片上传'''
@product.route('/F3001',methods = ['POST'])
def uploadProductImg():
    pass