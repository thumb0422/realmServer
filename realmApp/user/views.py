# -*- coding=utf-8 -*-
from . import user
from flask import jsonify,request,make_response,abort
from ..utility.Response import *
from ..utility import *
from ..model.userAction import *

@user.route('/')
def index():
    return 'Hello World I am user'

'''查询单个用户信息'''
@user.route('/F1001',methods = ['POST'])
def getUser():
    if not request.json :
        return  DataResopnse(-1, '非json格式', []).toJson()
    data = request.data.decode('utf-8')
    requestDic = json.loads(data)
    if 'userCode' in requestDic.keys():
        userCode = requestDic['userCode'] if requestDic['userCode'] is not None else ""
    else:
        userCode = ''
    return UserView.queryUsersSQL(userCode)

'''用户注册'''
@user.route('/F1005',methods = ['POST'])
def register():
    if not request.json :
        return  DataResopnse(-1, '非json格式', []).toJson()
    data = request.data.decode('utf-8')
    requestDic = json.loads(data)
    result = UserView.saveUsers(**requestDic)
    return result

'''更新用户资料'''
@user.route('/F1006',methods = ['POST'])
def updateregister():
    if not request.json :
        return  DataResopnse(-1, '非json格式', []).toJson()
    data = request.data.decode('utf-8')
    requestDic = json.loads(data)
    pass

'''用户登录'''
@user.route('/F1007',methods = ['POST'])
def login():
    if not request.json :
        return  DataResopnse(-1, '非json格式', []).toJson()
    data = request.data.decode('utf-8')
    requestDic = json.loads(data)
    '''check'''
    if UserView.checkUser(**requestDic):
        '''login'''
        return UserView.userLogin(**requestDic)
    else:
        return DataResopnse(-1, '该用户未注册', []).toJson()

'''用户登出'''
@user.route('/F1008',methods = ['POST'])
def logout():
    if not request.json :
        return  DataResopnse(-1, '非json格式', []).toJson()
    data = request.data.decode('utf-8')
    requestDic = json.loads(data)
    return UserView.userLogOut(**requestDic)

'''用户注销'''
@user.route('/F1009',methods = ['POST'])
def deleteUser():
    if not request.json :
        return  DataResopnse(-1, '非json格式', []).toJson()
    data = request.data.decode('utf-8')
    requestDic = json.loads(data)
    phone = requestDic['phone']
    return UserView.deleteUser(phone)