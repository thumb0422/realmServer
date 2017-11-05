from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class OrderMain(db.Model):
    __tablename__ = 'TM_OrderMain'
    orderId = db.Column(db.String(15), primary_key=True)
    amount = db.Column(db.DECIMAL(10,2))
    count = db.Column(db.Integer)
    states = db.Column(db.CHAR(1))
    createDate = db.Column(db.DateTime)
    updateDate = db.Column(db.DateTime)

    def __init__(self,orderId,amount,count,states,updateDate):
        self.orderId = orderId
        if amount is None:
            amount = 0.00
        self.amount = amount
        if count is None:
            count = 0
        self.count = count
        if states is None:
            states = 'Y'
        self.states = states
        self.createDate = datetime.now()
        if updateDate is None:
            updateDate = datetime.now()

    def __repr__(self):
        return "<OrderMain('%s','%s')>" % (self.orderId,self.states)

class OrderDetail(db.Model):
    __tablename__ = 'TM_OrderDetail'
    detailId = db.Column(db.Integer,primary_key=True)
    productCode = db.Column(db.String(15),unique=True)
    salePrice = db.Column(db.DECIMAL(10,2))
    count = db.Column(db.Integer)
    amount = db.Column(db.DECIMAL(10,2))
    states = db.Column(db.CHAR(1))
    createDate = db.Column(db.DateTime)
    updateDate = db.Column(db.DateTime)
    # 用于外键的字段
    orderId = db.Column(db.String(15),db.ForeignKey('TM_OrderMain.orderId'))
    # 外键对象，不会生成数据库实际字段
    # backref指反向引用，也就是外键Category通过backref(OrderMain_Detail)查询Post
    # orderMain = db.relationship('orderDetail',backref=db.backref('orderDetail',lazy='dynamic'))

    def __init__(self,detailId,productCode,salePrice,count,amount,states,updateDate,orderId):
        self.detailId = detailId
        self.productCode = productCode
        self.salePrice = salePrice
        self.count = count
        if states is None:
            states = 'Y'
        self.states = states
        if updateDate is None:
            updateDate = datetime.now()
        self.updateDate = updateDate
        # self.orderMain = orderMain
        self.createDate = datetime.now()
        self.orderId = orderId

    def __repr__(self):
        return "<OrderDetail('%s','%s, %s')>" % (self.orderId, self.states,self.orderId)

# db.create_all()