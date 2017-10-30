from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from main import db

# 建立user表
class Usr(db.Model):
    __tablename__ = 'usr'
    id = db.Column(db.Integer, primary_key=True)
    usrname = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    phone = db.relationship('Phone', backref='user', lazy='dynamic')

    def __init__(self, username, email):
        self.usrname = username
        self.email = email

class Phone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    factory = db.Column(db.String(20))
    userId = db.Column(db.Integer, db.ForeignKey('usr.id'))
    attr = db.relationship(
        'Atttr', backref='phone', lazy='dynamic')

    def __init__(self, name, factory, userId):
        self.name = name
        self.factory = factory
        self.userId = userId


class Atttr(db.Model):
    id = db .Column(db.Integer, primary_key=True)
    color = db.Column(db.String(20))
    price = db.Column(db.String(20))
    macId = db.Column(db.Integer, db.ForeignKey('phone.id'))

    def __init__(self, color, price, macId):
        self.color = color
        self.price = price
        self.macId = macId






# Role表
class Role(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    role_type_id=db.Column(db.Integer,db.ForeignKey('role_type.id'))

# RoleType表
class Role_type(db.Model):
    # query_class=Common_list_name_Query
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(120))
    role=db.relationship('Role',backref='role_type',lazy='dynamic', uselist=False)


db.create_all()