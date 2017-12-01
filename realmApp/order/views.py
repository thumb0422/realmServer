# -*- coding=utf-8 -*-
from flask import jsonify
from . import order
from random import random, randint
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
    ordermain.orderId = 'AAAAAAA' + str(randint(10,100))
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
