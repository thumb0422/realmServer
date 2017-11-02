from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'TM_User'
    userCode = db.Column(db.String(10), primary_key=True)
    userName = db.Column(db.String(250),nullable=False)
    states = db.Column(db.CHAR(1),nullable=False)
    createDate = db.Column(db.DateTime)
    updateDate = db.Column(db.DateTime)
    GroupCode = db.relationship('TM_Group',backref='TM_User',lazy='dynamic')

    def __init__(self,userCode,userName,states):
        self.userCode = userCode
        self.userName = userName
        self.states = states
        self.createDate = datetime.now()

    def __repr__(self):
        return '<userCode %r,userName %r states %r>' % self.userCode,self.userName,self.states

class Group(db.Model):
    __tablename__ = 'TM_Group'
    groupCode = db.Column(db.String(10), primary_key=True)
    groupName = db.Column(db.String(250))
    states = db.Column(db.CHAR(1))
    createDate = db.Column(db.DateTime)
    updateDate = db.Column(db.DateTime)
    userCode = db.Column(db.String(10),db.ForeignKey('TM_User.userCode'))

    def __init__(self,groupCode,groupName,states):
        self.groupCode = groupCode
        self.groupName = groupName
        self.states = states
        self.createDate = datetime.now()

    def __repr__(self):
        return '<groupCode %r,groupName %r states %r>' % self.groupCode,self.groupName,self.states