#-*- coding: UTF-8 -*-
from flask import jsonify,request
from sqlalchemy import func,select
from realmApp import db
from datetime import datetime
from ..utility import *

tableOrderKey = 'O'

class OrderMain(db.Model):
    __tablename__ = 'TM_OrderMain'
    __table_args__ = {'extend_existing': True}
    orderId = db.Column(db.String(15), primary_key=True)
    amount = db.Column(db.DECIMAL(10,2))
    count = db.Column(db.Integer)
    states = db.Column(db.CHAR(1))
    createDate = db.Column(db.DateTime,default=datetime.now())
    updateDate = db.Column(db.DateTime,default=datetime.now())

    def __init__(self,**kwargs):
        self.orderId = getModelKey(tableOrderKey)
        self.updateDate =  datetime.now()

    def __repr__(self):
        return "<OrderMain('%s','%s')>" % (self.orderId,self.states)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'orderId': self.orderId,
            'amount' : str(self.amount),
            'count'  : str(self.count),
            'states' : self.states,
            'createDate':dump_datetime(self.createDate),
        }

    @classmethod
    def getOrderMainMaxOrder(cls):
        maxOrder = OrderMain.query.order_by((OrderMain.orderId.desc())).first()
        return maxOrder.orderId

    @classmethod
    def getOrderMains(cls):
        ordersResult = OrderMain.query.all()
        #TODO:
        # orderCount = select([func.count("*")],from_obj=[ordersResult])
        # orderCount = ordersResult.rowcount
        return jsonify(status = '0',datas=[i.serialize for i in ordersResult])

    @classmethod
    def getOrderMainsById(cls,orderId):
        ordersResult = OrderMain.query.all().filter(OrderMain.orderId == orderId).first()
        return jsonify(status = '0',datas=[i.serialize for i in ordersResult])

    @classmethod
    def getOrderMainsByExpression(cls,expression):
        ordersResult = OrderMain.query.all().filter(eval(expression)).first()
        return jsonify(status='0', datas=[i.serialize for i in ordersResult])

    @staticmethod
    def saveOrderMain(self,**kwargs):
        return ""

class OrderDetail(db.Model):
    __tablename__ = 'TM_OrderDetail'
    __table_args__ = {'extend_existing': True}
    detailId = db.Column(db.Integer,primary_key=True)
    productCode = db.Column(db.String(15),unique=True)
    salePrice = db.Column(db.DECIMAL(10,2))
    count = db.Column(db.Integer)
    amount = db.Column(db.DECIMAL(10,2))
    states = db.Column(db.CHAR(1))
    createDate = db.Column(db.DateTime,default=datetime.now())
    updateDate = db.Column(db.DateTime,default=datetime.now())
    # 用于外键的字段
    orderId = db.Column(db.String(15),db.ForeignKey('TM_OrderMain.orderId'))
    # 外键对象，不会生成数据库实际字段
    # backref指反向引用，也就是外键Category通过backref(OrderMain_Detail)查询Post
    # orderMain = db.relationship('orderDetail',backref=db.backref('orderDetail',lazy='dynamic'))

    def __init__(self,**kwargs):
        self.createDate = datetime.now()
        self.updateDate = datetime.now()

    def __repr__(self):
        return "<OrderDetail('%s','%s, %s')>" % (self.orderId, self.states,self.orderId)

    @classmethod
    def getOrderdetails(cls):
        orderdetails = db.session.query(OrderDetail).all()
        return orderdetails

    @classmethod
    def getOrderMainsById(cls, orderId):
        orderdetails = db.session.query(OrderDetail).filter(OrderMain.orderId == orderId).first()
        return orderdetails

    @classmethod
    def getOrderMainsByExpression(cls, expression):
        orderdetails = db.session.query(OrderDetail).filter(eval(expression)).first()
        return orderdetails

    @staticmethod
    def saveOrderDetails(self,**kwargs):
        return ""
