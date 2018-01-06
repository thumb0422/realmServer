# coding: utf-8
from sqlalchemy.ext.declarative import DeclarativeMeta
from realmApp.model import *
from realmApp.model.model import *
from realmApp.utility import *
from realmApp.utility.Response import *
from realmApp.utility.alchemyEncoder import *

class UserView:

    @classmethod
    def queryUsersORM(cls,userCode):
        query = session.query(TMUser)
        print(query)
        users = query.all()
        user = users[0]
        print(user.userId,user.userCode,user.userName)

    @classmethod
    def queryUsersSQL(cls,userCode):
        sqlText = 'select userCode,userName from TM_USER where 1=1 '
        sqlDic = {}
        if userCode:
            sqlText = sqlText + 'and userCode = :userCode'
            sqlDic['userCode'] = userCode
        res = session.execute(text(sqlText),sqlDic).fetchall()
        resultArray = rowToArray(res)
        session.close()
        # resultDic = {"status": 0, 'message': '查询成功', "count": resultArray.__len__(), "datas": resultArray}
        # resultJson = json.dumps(resultDic, cls=AlchemyEncoder,indent=4,sort_keys=True)
        # return resultJson
        return DataResopnse(0, '查询成功', resultArray).toJson()

    '''视图查询'''
    @classmethod
    def queryUsersView(cls):
        pass;

    ''' insert'''
    @classmethod
    def saveUsers(cls,**kwargs):
        user = TMUSER()
        user.userPwd = kwargs['userPwd']
        user.userName = kwargs['userName']
        '''保存的时候以哪个字段为准来判断是否重复'''
        '''以手机号为准'''
        user.phone = kwargs['phone']
        user.email = kwargs['email']
        user.userCode = getModelKey('UR')
        session.add(user)
        try:
            session.flush()
            session.commit()
            return DataResopnse(0, '保持成功', [{'keyId': user.userCode}]).toJson()
        except:
            session.rollback()
            return DataResopnse(-1, '保存失败',[]).toJson()

    ''' update'''
    @classmethod
    def updateUsers(cls,**kwargs):
        user = TMUSER()
        '''保存的时候以哪个字段为准来判断是否重复'''
        '''以手机号为准'''
        user.phone = kwargs['phone']

        user.userPwd = kwargs['userPwd']
        user.userName = kwargs['userName']

        user.userCode = getModelKey('UR')
        session.add(user)
        try:
            session.flush()
            session.commit()
            return DataResopnse(0, '保持成功', [{'keyId': user.userCode}]).toJson()
        except:
            session.rollback()
            return DataResopnse(-1, '保存失败',[]).toJson()