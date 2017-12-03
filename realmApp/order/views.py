# -*- coding=utf-8 -*-
from flask import jsonify,request,make_response,abort
from . import order
from random import random, randint
from ..model.orderModel import *

@order.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not Found'}),404)

@order.route('/')
def index():
    return 'Hello World I am order'

@order.route('/getOrder')
def getOrder():
    return OrderMain.getOrderMains()

@order.route('/addOrder')
def addOrder():
    ordermain = OrderMain()
    ordermain.states = 'Y'
    ordermain.amount = 100
    ordermain.count = 5
    db.session.add(ordermain)
    try:
        db.session.flush()
        db.session.commit()
        return jsonify({'status': '0'})
    except:
        db.session.rollback()
        return jsonify({'status': '-1'})

@order.route('/saveOrder',methods = ['POST','GET'])
def saveOrder():
    if not request.json or not 'amount' in request.json:
        abort(400)
    print('----------')
    return ""
