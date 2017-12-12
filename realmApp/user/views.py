# -*- coding=utf-8 -*-
from . import user
from flask import jsonify,request,make_response,abort
from random import random, randint
from ..model.userModel import *
import json

@user.route('/')
def index():
    return 'Hello World I am user'

@user.route('/getUser',methods = ['POST'])
def getUser():
    if not request.json :
        return jsonify({'status':-1,'message':'非json格式'})
    requestStr = json.dumps(request.json)
    requestDic = eval(requestStr)
    userCode = requestDic['userCode']
    result = User.getUsersById(userCode)
    return result

@user.route('/register',methods = ['POST'])
def register():
    '''
    用户注册事件
    :return:
    '''
    if not request.json :
        return jsonify({'status':-1,'message':'非json格式'})
    requestStr = json.dumps(request.json)
    requestDic = eval(requestStr)
    result = User.saveUsers(**requestDic)
    return result

@user.route('/updateregister',methods = ['POST'])
def updateregister():
    '''
    更新用户状态
    :return:
    '''
    if not request.json :
        return jsonify({'status':-1,'message':'非json格式'})
    requestStr = json.dumps(request.json)
    requestDic = eval(requestStr)
    result = User.updateUser(**requestDic)
    return result

@user.route('/login',methods = ['POST'])
def login():
    '''
    用户登录
    :return:
    '''
    '''
    parser = reqparse.RequestParser()
    parser.add_argument('userCode', type=str, help='XXXXXX')
    parser.add_argument('userPwd', type=str)
    args = parser.parse_args()
    '''

    if not request.json :
        return jsonify({'status':-1,'message':'非json格式'})
    requestStr = json.dumps(request.json)
    requestDic = eval(requestStr)
    result = User.login(**requestDic)
    return result

@user.route('/logout',methods = ['POST'])
def logout():
    '''
    用户登出
    :return:
    '''
    if not request.json :
        return jsonify({'status':-1,'message':'非json格式'})
    requestStr = json.dumps(request.json)
    requestDic = eval(requestStr)
    result = User.logout(**requestDic)
    return result