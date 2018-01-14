# -*- coding=utf-8 -*-
from flask import jsonify,request,make_response,abort
from . import order
from random import random, randint
from ..model.orderModel import *
import json

@order.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not Found'}),404)

@order.route('/')
def index():
    return 'Hello World I am order'

'''getOrder'''
@order.route('/F2001',methods = ['POST'])
def getOrder():
    if request.json is not None:
        jsonDic = converJsonToDic(request.json)
        if 'orderId' in jsonDic.keys():
            orderId = jsonDic['orderId'] if jsonDic['orderId'] is not None else ""
        else:
            orderId = ''
        # if 'orderId' in jsonDic.keys():
        #     orderId = jsonDic['orderId']
        #     if orderId is None:
        #         return OrderMain.getOrderMainsJson()
        #     return OrderMain.getOrderMainsById(orderId)
        # else:
        #     return OrderMain.getOrderMainsJson()
        return OrderMain.getOrderMainsJson(orderId)
    return jsonify({'status': -1, 'message': '非json格式'})

'''saveOrder'''
@order.route('/F2002',methods = ['POST','GET'])
def saveOrder():
    if not request.json :
        return  DataResopnse(-1, '非json格式', []).toJson()
    data = request.data.decode('utf-8')
    requestDic = json.loads(data)
    result = OrderMain.saveOrderMain(**requestDic)
    return result


