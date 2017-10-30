from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from main import db

class OrderMain(db.Model):
    __tablename__ = 'TM_OrderMain'
    orderId = db.Column(db.String(15), primary_key=True)
    amout = db.Column(db.DECIMAL(10,2))
    count = db.Column(db.Integer)
    states = db.Column(db.CHAR(1))
    createDate = db.Column(db.DateTime)
    updateDate = db.Column(db.DateTime)
    OrderDetail_orderId = db.relationship('TM_OrderDetail',backref='TM_OrderMain',lazy='dynamic')

    def __init__(self,orderId,states):
        self.orderId = orderId
        self.states = states
        self.createDate = datetime.now()

    def __repr__(self):
        return '<orderId %r,states %r>' %self.orderId,self.states


class OrderDetail(db.Model):
    __tablename__ = 'TM_OrderDetail'
    detailId = db.Column(db.Integer,primary_key=True)
    productCode = db.Column(db.String(15),unique=True)
    salePrice = db.Column(db.DECIMAL(10,2))
    count = db.Column(db.Integer)
    amount = db.Column(db.DECIMAL(10,2))
    orderId = db.Column(db.String(15),db.ForeignKey('TM_OrderMain.orderId'))
    states = db.Column(db.CHAR(1))
    createDate = db.Column(db.DateTime)
    updateDate = db.Column(db.DateTime)

    def __init__(self,detailId,orderId,states):
        self.detailId = detailId
        self.orderId = orderId
        self.states = states
        self.createDate = datetime.now()

    def __repr__(self):
        return '<orderId %r,states %r>' %self.orderId,self.states


# db.create_all()