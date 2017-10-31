from flask import Flask ,request,jsonify
from flask_restful import reqparse,Api,abort,Resource
from order.orderModel import OrderMain,OrderDetail
from main import app


class OrderAction:
    def queryOrderByOrderId(orderId):
        if request.method == 'GET':
            data = request.get_data()
            dataDic = jsonify(data)
            data1 = queryOrderMainByOrderId(orderId)

            data2 = data1.OrderMain_Detail.all()
            return jsonify({'status': '0',
                            'data1': data1,
                            'data2': data2})

    def queryOrderMainByOrderId(orderId):
        data = OrderMain(orderId=orderId)
        return jsonify({'data1': data})

    def queryOrderDetailByOrderId(orderId):
        data = OrderDetail(orderId=orderId)
        return jsonify({'data2': data})