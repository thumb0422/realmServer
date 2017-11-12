#-*- coding: UTF-8 -*-
from .. import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'TM_User'
    __table_args__ = {'extend_existing': True}
    userCode = db.Column(db.String(10), primary_key=True)
    userName = db.Column(db.String(250),nullable=False)
    states = db.Column(db.CHAR(1),nullable=False)
    createDate = db.Column(db.DateTime,default=datetime.now())
    updateDate = db.Column(db.DateTime,default=datetime.now())
    GroupCode = db.relationship('TM_Group',backref='TM_User',lazy='dynamic')

    def __init__(self,**args):
        if (len(args) > 2):
            print("wrong args number")
            return
        self.__dict__.update(args)

    def __repr__(self):
        return '<userCode %r,userName %r states %r>' % self.userCode,self.userName,self.states

class Group(db.Model):
    __tablename__ = 'TM_Group'
    __table_args__ = {'extend_existing': True}
    groupCode = db.Column(db.String(10), primary_key=True)
    groupName = db.Column(db.String(250))
    states = db.Column(db.CHAR(1))
    createDate = db.Column(db.DateTime,default=datetime.now())
    updateDate = db.Column(db.DateTime,default=datetime.now())
    userCode = db.Column(db.String(10),db.ForeignKey('TM_User.userCode'))

    def __init__(self,**args):
        if (len(args) > 2):
            print("wrong args number")
            return
        self.__dict__.update(args)

    def __repr__(self):
        return '<groupCode %r,groupName %r states %r>' % self.groupCode,self.groupName,self.states