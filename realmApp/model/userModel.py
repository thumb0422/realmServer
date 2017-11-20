#-*- coding: UTF-8 -*-
# from .. import db
from realmApp import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'TM_User'
    __table_args__ = {'extend_existing': True}
    userId = db.Column(db.Integer,primary_key=True,autoincrement=True)
    userName = db.Column(db.String(250),nullable=False)
    states = db.Column(db.CHAR(1),nullable=False)
    createDate = db.Column(db.DateTime,default=datetime.now())
    updateDate = db.Column(db.DateTime,default=datetime.now())
    # GroupCode = db.relationship('TM_Group',backref='TM_User',lazy='dynamic')

    def __init__(self,**args):
        if (len(args) > 2):
            print("wrong args number")
            return
        self.__dict__.update(args)

    def __repr__(self):
        return '<userCode %r,userName %r states %r>' % self.userCode,self.userName,self.states

    @classmethod
    def getOrderMains(cls):
        users = db.session.query(User).all()
        return users

    @classmethod
    def getOrderMainsById(cls, userCode):
        user = db.session.query(User).filter(User.orderId == userCode).first()
        return user

    @classmethod
    def getOrderMainsByExpression(cls, expression):
        users = db.session.query(User).filter(eval(expression)).first()
        return users

    @staticmethod
    def saveUser(self, **kwargs):
        return ""

class Group(db.Model):
    __tablename__ = 'TM_Group'
    __table_args__ = {'extend_existing': True}
    groupCode = db.Column(db.String(10), primary_key=True)
    groupName = db.Column(db.String(250))
    states = db.Column(db.CHAR(1))
    createDate = db.Column(db.DateTime,default=datetime.now())
    updateDate = db.Column(db.DateTime,default=datetime.now())
    userId = db.Column(db.String(10),db.ForeignKey('TM_User.userId'))

    def __init__(self,**kwargs):
        if (len(kwargs) > 2):
            print("wrong args number")
            return
        self.__dict__.update(kwargs)

    def __repr__(self):
        return '<groupCode %r,groupName %r states %r>' % self.groupCode,self.groupName,self.states