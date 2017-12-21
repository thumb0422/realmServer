#-*- coding: UTF-8 -*-
from flask import jsonify,session
from realmApp import db
from realmApp.utility import *
import datetime

tableOrderKey = 'UR'
class User(db.Model):
    __tablename__ = 'TM_User'
    __table_args__ = {'extend_existing': True}
    userId = db.Column(db.Integer,primary_key=True,autoincrement=True)
    userCode = db.Column(db.String(30),nullable=False)
    userPwd = db.Column(db.String(200), nullable=False)
    userName = db.Column(db.String(250),nullable=False)
    states = db.Column(db.CHAR(1),nullable=False)
    createDate = db.Column(db.DateTime)
    updateDate = db.Column(db.DateTime)
    # 用于外键的字段
    groupId = db.Column(db.Integer, db.ForeignKey('TM_Group.groupId'))

    def __init__(self):
        self.userCode = getModelKey(tableOrderKey)
        self.states = 'Y'
        self.createDate = datetime.datetime.now()
        # self.updateDate = datetime.datetime.now()

    def __repr__(self):
        return "<User('%s','%s')>" % (self.userCode, self.userName)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'userCode': self.userCode,
            'userName': self.userName,
            'states':self.states if self.states is not None else "",
        }

    @classmethod
    def getUsers(cls):
        users = db.session.query(User).all()
        return users

    @classmethod
    def getUsersById(cls, userCode):
        user = User.query.filter_by(userCode = userCode).all()
        return jsonify(status='0', datas=[i.serialize for i in user])

    @classmethod
    def saveUsers(cls, **kwargs):
        user = User()
        user.userPwd = kwargs['userPwd']
        user.userName = kwargs['userName']
        '''TODO: check userName'''
        db.session.add(user)
        try:
            db.session.flush()
            db.session.commit()
            return jsonify({'status': '0', 'message': '保存成功', 'keyId': user.userCode})
        except:
            db.session.rollback()
            return jsonify({'status': '-1', 'message': '保存失败'})

    @classmethod
    def updateUser(cls,**kwargs):
        userCode = kwargs['userCode']
        user = User.query.filter_by(userCode=userCode).first()
        user.userName = kwargs['userName']
        user.userPwd = kwargs['userPwd']
        user.states = 'Y'
        user.updateDate = datetime.datetime.now()
        db.session.add(user)
        try:
            db.session.flush()
            db.session.commit()
            return jsonify({'status': '0', 'message': '更新成功', 'keyId': user.userCode})
        except:
            db.session.rollback()
            return jsonify({'status': '-1', 'message': '更新失败'})

    @classmethod
    def login(cls, userCode, userPwd, **kwargs):
        user = User
        user.userCode = userCode
        user.userPwd = userPwd
        if user.checkUser(self=user):
            '''
            login
            push session
            session存储的key
            '''
            session[user.userCode] = user.userCode
            return jsonify({'status': '0', 'message': '登录成功','sessionId':user.userCode})
        else:
            return jsonify({'status': '-1', 'message': '登录失败'})

    @classmethod
    def logout(cls, **kwargs):
        '''
        logout
        pop session
        '''
        user = User
        '''
        TODO: 检验session的标准
        '''
        user.userCode = kwargs['userCode']
        user.userPwd = kwargs['userPwd']
        if user.checkUser(self=user):
            session.pop(user.userCode,None)
            return jsonify({'status': '0', 'message': '退出成功'})
        else:
            return jsonify({'status': '-1', 'message': '退出失败'})

    @staticmethod
    def checkUser(self):
        userCode = self.userCode
        userPWD = self.userPwd
        if userCode is not None and userPWD is not None:
            user = User.query.filter_by(userCode=userCode,userPwd=userPWD).all()
            if user is not None:
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def checkUserAndPwd(cls,userCode,userPwd):
        user = User.query.filter_by(userCode = userCode,userPwd=userPwd).all()
        if user is not None:
            return True
        else:
            return False


class Group(db.Model):
    __tablename__ = 'TM_Group'
    __table_args__ = {'extend_existing': True}
    groupId = db.Column(db.Integer, primary_key=True,autoincrement=True)
    groupName = db.Column(db.String(250))
    states = db.Column(db.CHAR(1))
    createDate = db.Column(db.DateTime)
    updateDate = db.Column(db.DateTime)
    # userId = db.Column(db.Integer,db.ForeignKey('TM_User.userId'))

    def __init__(self):
        self.states = 'Y'
        self.createDate = datetime.datetime.now()
        # self.updateDate = datetime.datetime.now()
        pass

    def __repr__(self):
        return '<groupCode %r,groupName %r states %r>' % self.groupCode,self.groupName,self.states