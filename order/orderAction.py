from flask import Flask ,request
from flask_restful import reqparse,Api,abort,Resource
from main import app

parse = reqparse.RequestParser

#GET byOrderId
@app.route('queryOrderByOrderId/<string:orderId>',methods=['GET'])
def queryOrderByOrderId(orderId):
    if request.method == 'GET':
        return {'':''}

def queryOrderMainByOrderId(orderId):
    return {'':''}

def queryOrderDetailByOrderId(orderId):
    return {'':''}

#POST
@app.route('saveOrder',methods=['POST'])
def saveOrder():
    if request.method == 'POST':
        return {'':''}

def saveOrderMain():
    args = parse.parse_args()
    return {'':''}

def saveOrderDetail():
    return {'':''}

#DELETE byOrderId
@app.route('deleteOrderByOrderId/<string:orderId>',methods=['DELETE'])
def deleteOrderByOrderId(orderId):
    if request.method == 'DELETE':
        return {'':''}

def deleteOrderMainByOrderId(orderId):
    return {'':''}

def deleteOrderDetailByOrderId(orderId):
    return {'':''}