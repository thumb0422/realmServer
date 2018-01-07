# -*- coding=utf-8 -*-
from . import user
from flask import jsonify,request,make_response,abort
from realmApp.utility.Response import *
from realmApp.utility import *
from realmApp.model.userAction import *

@user.route('/')
def index():
    return 'Hello World I am user'

'''getUser'''
@user.route('/F1001',methods = ['POST'])
def getUser():
    if request.json is not None:
        jsonDic = converJsonToDic(request.json)
        if 'userCode' in jsonDic.keys():
            userCode = jsonDic['userCode'] if jsonDic['userCode'] is not None else ""
        else:
            userCode = ''
        return UserView.queryUsersSQL(userCode)
    return DataResopnse(0, '查询成功', []).toJson()

'''register'''
@user.route('/F1005',methods = ['POST'])
def register():
    '''
    用户注册事件
    :return:
    '''
    if not request.json :
        return  DataResopnse(-1, '非json格式', []).toJson()
    requestStr = json.dumps(request.json)
    requestDic = eval(requestStr)
    result = UserView.saveUsers(**requestDic)
    return result

'''update用户资料'''
@user.route('/F1006',methods = ['POST'])
def updateregister():
    '''
    更新用户状态
    TODO:
    '''
    if not request.json :
        return DataResopnse(-1, '非json格式', []).toJson()
    requestStr = json.dumps(request.json)
    requestDic = eval(requestStr)
    pass

'''login'''
@user.route('/F1007',methods = ['POST'])
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
        return DataResopnse(-1, '非json格式', []).toJson()
    requestStr = json.dumps(request.json)
    requestDic = eval(requestStr)
    '''check'''
    if UserView.checkUser(**requestDic):
        '''login'''
        return UserView.userLogin(**requestDic)
    else:
        return DataResopnse(-1, '该用户未注册', []).toJson()

'''logout'''
@user.route('/F1008',methods = ['POST'])
def logout():
    '''
    用户登出
    :return:
    '''
    if not request.json :
        return jsonify({'status':-1,'message':'非json格式'})
    requestStr = json.dumps(request.json)
    requestDic = eval(requestStr)
    return UserView.userLogOut(**requestDic)

'''deleteUser'''
@user.route('/F1009',methods = ['POST'])
def deleteUser():
    if not request.json :
        return jsonify({'status':-1,'message':'非json格式'})
    requestStr = json.dumps(request.json)
    requestDic = eval(requestStr)
    phone = requestDic['phone']
    return UserView.deleteUser(phone)