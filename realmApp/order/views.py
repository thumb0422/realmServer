# -*- coding=utf-8 -*-
from flask import jsonify
from . import order
from ..model.orderModel import *

@order.route('/')
def index():
    return 'Hello World I am order'

@order.route('/getOrder')
def getOrder():
    return OrderMain.getOrderMains()

@order.route('/addOrder')
def addOrder():
    ordermain = OrderMain()
    ordermain.orderId = 'AAAAAAA3'
    ordermain.states = 'Y'
    ordermain.amount = 100
    ordermain.count = 5
    db.session.add(ordermain)
    db.session.flush()
    db.session.commit()
    return jsonify({'status':'0'})