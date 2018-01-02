# coding: utf-8
from sqlalchemy.ext.declarative import DeclarativeMeta
from realmApp.model import *
from realmApp.model.model import *
from realmApp.utility import *
from realmApp.utility.Response import *
from flask import jsonify
from realmApp.utility.alchemyEncoder import *

'''SQL'''
# sql = text("select * from TM_Address")
# res = session.execute(sql).fetchall()
# for row in res:
#     for col in row:
#         print (col)
#     print
# session.close()

'''ORM'''
# res = session.query(TMAddres).filter(text("addressId=1")).one()
# print (res.addressId,res.userId,res.address)


class UserView:

    @classmethod
    def queryUsersORM(cls):
        query = session.query(TMUSER)
        print(query)
        users = query.all()
        user = users[0]
        print(user.userId,user.userCode,user.userName)

    @classmethod
    def queryUsersSQL(cls):
        sql = text("select * from TM_USER")
        res = session.execute(sql).fetchall()
        resultArray = rowToArray(res)
        session.close()
        # sqlResultStr = json.dumps(resultArray, cls=AlchemyEncoder)
        # print(sqlResultStr)
        resultDic = {"status": 0, 'message': '查询成功', "count": resultArray.__len__(), "datas": resultArray}
        resultJson = json.dumps(resultDic, cls=AlchemyEncoder,indent=4,sort_keys=True)
        return resultJson


    @classmethod
    def queryUsersView(cls):
        pass;

    @classmethod
    def saveUsers(cls):
        user = TMUSER()
        user.userCode = getModelKey('UR')
        user.userName = 'TEST1'
        user.email = 'thumb0422@163.com'
        session.add(user)
        session.commit()

# UserView.saveUsers()
# UserView.queryUsers()
UserView.queryUsersSQL()