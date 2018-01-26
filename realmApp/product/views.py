# -*- coding=utf-8 -*-
from flask import jsonify,request,make_response,abort
from . import product
from ..model.model import *
from ..utility.Response import *
from ..utility import *
from ..model.productAction import *


@product.route('/')
def index():
    return 'Hello World I am product'

'''查询单个产品信息'''
@product.route('/F2001',methods = ['POST'])
def getUser():
    if not request.json :
        return  DataResopnse(-1, '非json格式', []).toJson()
    data = request.data.decode('utf-8')
    requestDic = json.loads(data)
    if 'productCode' in requestDic.keys():
        productCode = requestDic['productCode'] if requestDic['productCode'] is not None else ""
    else:
        productCode = ''
    return ProductView.queryProductCode(productCode)