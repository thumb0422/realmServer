#-*- coding: UTF-8 -*-
from .. import db
from datetime import datetime

class OrderMain(db.Model):
    __tablename__ = 'TM_OrderMain'
    __table_args__ = {'extend_existing': True}
    orderId = db.Column(db.String(15), primary_key=True)
    amount = db.Column(db.DECIMAL(10,2))
    count = db.Column(db.Integer)
    states = db.Column(db.CHAR(1))
    createDate = db.Column(db.DateTime,default=datetime.now())
    updateDate = db.Column(db.DateTime,default=datetime.now())

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
