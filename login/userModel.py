from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from main import db

class user(db.Model):
    userCode = db.Column(db.String(10), primary_key=True)
    userName = db.Column(db.String(250))
    states = db.Column(db.String(1))
    createDate = db.Column(db.DateTime)
    updateDate = db.Column(db.DateTime)
    # groupCode = db.Column

    def __init__(self,userCode,userName,states):
        self.userCode = userCode
        self.userName = userName
        self.states = states
        self.createDate = datetime.now()

    def __repr__(self):
        return '<userCode %r,userName %r states %r>' % self.userCode,self.userName,self.states

class group(db.Model):
    groupCode = db.Column(db.String(10), primary_key=True)
    groupName = db.Column(db.String(250))
    states = db.Column(db.String(1))
    createDate = db.Column(db.DateTime)
    updateDate = db.Column(db.DateTime)

    def __init__(self,groupCode,groupName,states):
        self.groupCode = groupCode
        self.groupName = groupName
        self.states = states
        self.createDate = datetime.now()

    def __repr__(self):
        return '<groupCode %r,groupName %r states %r>' % self.groupCode,self.groupName,self.states
