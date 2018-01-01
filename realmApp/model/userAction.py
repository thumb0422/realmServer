# coding: utf-8
from realmApp.model import *
from realmApp.model.model import *

'''SQL'''
# sql = text("select * from TM_Address")
# res = session.execute(sql).fetchall()
# for row in res:
#     for col in row:
#         print (col)
#     print
# session.close()

'''ORM'''
res = session.query(TMAddres).filter(text("addressId=1")).one()
print (res.addressId,res.userId,res.address)