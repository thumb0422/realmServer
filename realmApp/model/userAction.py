# coding: utf-8
from sqlalchemy.ext.declarative import DeclarativeMeta
from realmApp.model import *
from realmApp.model.model import *
from realmApp.utility import *
from realmApp.utility.Response import *
from realmApp.utility.alchemyEncoder import *

class UserView:

    def queryByExpression(self):

        pass

    @classmethod
    def queryUsersORM(cls,userCode):
        session = Session()
        query = session.query(TMUser)
        print(query)
        users = query.all()
        user = users[0]
        print(user.userId,user.userCode,user.userName)

    @classmethod
    def queryUsersSQL(cls,userCode):
        session = Session()
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
        pass

    '''检查用户帐号、密码是否存在'''
    @classmethod
    def checkUser(cls,**kwargs):
        session = Session()
        pwd = kwargs['userPwd']
        phone = kwargs['phone']
        queryPhone = session.query(TMUser).filter(TMUser.phone == phone, TMUser.isValid == 'Y').all()
        isPhoneExist = queryPhone.__len__() > 0
        if isPhoneExist:
            queryPwd = queryPhone.filter(TMUser.userPwd == pwd).all()
            isPwdExist = queryPwd.__len__() > 0
            if isPwdExist:
                return True
            else:
                return False
        else:
            return False

    ''' insert'''
    @classmethod
    def saveUsers(cls,**kwargs):
        session = Session()
        user = TMUser()
        user.userPwd = kwargs['userPwd']
        user.userName = kwargs['userName']
        '''保存的时候以哪个字段为准来判断是否重复'''
        '''以手机号为准'''
        for key in kwargs:
            print('key is :%s,value is :%s' % (key, kwargs[key]))
            if key == 'phone':
                user.phone = kwargs[key]
                query = session.query(TMUser).filter(TMUser.phone==user.phone,TMUser.isValid=='Y').all()
                '''查询是否存在'''
                isExist = query.__len__() > 0
                if isExist:
                   return DataResopnse(-1, '保存失败,该手机号已注册',[]).toJson()
            elif key == 'email':
                user.email = kwargs[key]
                query = session.query(TMUser).filter(TMUser.email == user.email, TMUser.isValid == 'Y').all()
                '''查询是否存在'''
                isExist = query.__len__() > 0
                if isExist:
                    return DataResopnse(-1, '保存失败,该邮箱已注册', []).toJson()
        user.userCode = getModelKey('UR')
        session.add(user)
        try:
            session.flush()
            session.commit()
            return DataResopnse(0, '保持成功', [{'keyId': user.userCode}]).toJson()
        except:
            session.rollback()
            return DataResopnse(-1, '保存失败',[]).toJson()
        finally:
            session.close()

    ''' update'''
    @classmethod
    def updateUsers(cls,**kwargs):
        session = Session()
        user = TMUser()
        user.userCode = kwargs['userCode']
        '''查询'''


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
        finally:
            session.close()

    @classmethod
    def userLogin(cls,**kwargs):
        session = Session()
        userStatus = TMUserStatu()
        '''查询出该用户的信息'''
        phone = kwargs['phone']
        querys = session.query(TMUser).filter(TMUser.phone == phone, TMUser.isValid == 'Y').all()
        user = querys[0]
        userStatus.isLogin = 'Y'
        userStatus.userId = user.userId
        session.add(userStatus)
        try:
            session.flush()
            session.commit()
            return DataResopnse(0, '登录成功', []).toJson()
        except:
            session.rollback()
            return DataResopnse(-1, '登录失败', []).toJson()
        finally:
            session.close()

    @classmethod
    def userLogOut(cls,**kwargs):
        session = Session()
        userStatus = TMUserStatu()
        '''查询出该用户的信息'''
        phone = kwargs['phone']
        querys = session.query(TMUser).filter(TMUser.phone == phone, TMUser.isValid == 'Y').all()
        user = querys[0]
        userStatus.isLogin = 'N'
        userStatus.userId = user.userId
        session.add(userStatus)
        try:
            session.flush()
            session.commit()
            return DataResopnse(0, '退出成功', []).toJson()
        except:
            session.rollback()
            return DataResopnse(-1, '退出失败', []).toJson()
        finally:
            session.close()