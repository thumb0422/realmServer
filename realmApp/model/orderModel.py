#-*- coding: UTF-8 -*-
from flask import jsonify,request
from sqlalchemy import func,select
from realmApp import db
from realmApp.utility import *
import datetime


from sqlalchemy import Column,text
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from realmApp.utility import *
BaseModel = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,mapper
import config

enginee = create_engine(config.MySQLConfig.SQLALCHEMY_DATABASE_URI,echo=True)
DBSession = sessionmaker(bind=enginee)
session = DBSession()


tableOrderKey = 'OD'

class OrderMain(db.Model):
    __tablename__ = 'TM_OrderMain'
    __table_args__ = {'extend_existing': True}
    orderId = db.Column(db.String(30), primary_key=True)
    sumAmount = db.Column(db.DECIMAL(10,2))
    sumCount = db.Column(db.Integer)
    states = db.Column(db.CHAR(1))
    createDate = db.Column(db.DateTime)
    updateDate = db.Column(db.DateTime)

    def __init__(self):
        self.orderId = getModelKey(tableOrderKey)
        self.states = 'Y'
        self.createDate = datetime.datetime.now()
        # self.updateDate = datetime.datetime.now()

    def __repr__(self):
        return "<OrderMain('%s','%s')>" % (self.orderId,self.states)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'orderId': self.orderId,
            'sumCount': self.sumCount,
            'sumAmount': str(self.sumAmount),
            'states': self.states if self.states is not None else "",
            'createDate':dump_datetime(self.createDate),
        }

    @classmethod
    def getOrderMainMaxOrder(cls):
        maxOrder = OrderMain.query.order_by((OrderMain.orderId.desc())).first()
        return maxOrder.orderId

    @classmethod
    def getOrderMains(cls):
        ordersResult = OrderMain.query.all()
        return jsonify(status = '0',datas=[i.serialize for i in ordersResult])

    @classmethod
    def getOrderMainsJson(cls):
        # querySqls = enginee.execute(text("select * from TM_OrderMain"))
        # queryAnss = querySqls.fetchall()
        # queryAns = queryAnss[0]
        # queryDics = classToDict(queryAns)
        # json2 = json.dumps([dict(r) for r in queryAnss], default=alchemyencoder)
        # json3 = json.dumps(json2, status = '0')
        # return json2

        '''查询语句查询出来解析成json'''
        resultProxy = enginee.execute(text("select * from TM_OrderMain"))
        results = resultProxy.fetchall()
        result0 = results[0]

        resultArray = row2Array(results)
        resultProxy.close()
        return jsonify({"status":0,"count":resultArray.__len__(),"datas":resultArray})

    @classmethod
    def getOrderMainsById(cls,orderId):
        ordersResult = OrderMain.query.filter_by(orderId = orderId).all()
        return jsonify(status = '0',datas=[i.serialize for i in ordersResult])

    @classmethod
    def getOrderMainsByExpression(cls,expression):
        ordersResult = OrderMain.query.all().filter(eval(expression)).first()
        return jsonify(status='0', datas=[i.serialize for i in ordersResult])

    @classmethod
    def saveOrderMain(cls,**kwargs):
        orderMain = OrderMain()
        for key in kwargs:
            print('key is :%s,value is :%s' % (key, kwargs[key]))
            if key == 'sumAmount':
                orderMain.sumAmount = kwargs[key]
            elif key == 'sumCount':
                orderMain.sumCount = kwargs[key]
            else:
                break
        db.session.add(orderMain)
        try:
            db.session.flush()
            db.session.commit()
            return jsonify({'status':'0','message':'保存成功','keyId':orderMain.orderId})
        except:
            db.session.rollback()
            return jsonify({'status': '-1','message':'保存失败'})

    @classmethod
    def updateOrderMain(cls,**kwargs):
        orderId = kwargs['orderId']
        orders = OrderMain.query.filter_by(orderId=orderId).all()

        return ''

class OrderDetail(db.Model):
    __tablename__ = 'TM_OrderDetail'
    __table_args__ = {'extend_existing': True}
    detailId = db.Column(db.Integer,primary_key=True,autoincrement=True)
    productCode = db.Column(db.String(15),unique=True)
    salePrice = db.Column(db.DECIMAL(10,2))
    count = db.Column(db.Integer)
    amount = db.Column(db.DECIMAL(10,2))
    states = db.Column(db.CHAR(1))
    createDate = db.Column(db.DateTime)
    updateDate = db.Column(db.DateTime)
    # 用于外键的字段
    orderId = db.Column(db.String(30),db.ForeignKey('TM_OrderMain.orderId'))
    # 外键对象，不会生成数据库实际字段
    # backref指反向引用，也就是外键Category通过backref(OrderMain_Detail)查询Post
    # orderMain = db.relationship('orderDetail',backref=db.backref('orderDetail',lazy='dynamic'))

    def __init__(self,**kwargs):
        self.states = 'Y'
        self.createDate = datetime.datetime.now()
        # self.updateDate = datetime.datetime.now()

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
