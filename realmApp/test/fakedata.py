#-*- coding: UTF-8 -*-
from realmApp.model.model import *
from realmApp.utility import *
from realmApp.model import *


for i in range(10):
    session = Session()
    user = TMUser()
    user.userCode = getModelKey('UR')
    user.userName = 'TEST' + str(i)
    user.email = 'thumb0422@163.com'
    session.add(user)
    session.commit()

