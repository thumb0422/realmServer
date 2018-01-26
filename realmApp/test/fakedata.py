#-*- coding: UTF-8 -*-
from ..model.model import *
from ..utility import *
from ..model import *


for i in range(10):
    session = Session()
    user = TMUser()
    user.userCode = getModelKey('UR')
    user.userName = 'TEST' + str(i)
    user.email = 'thumb0422@163.com'
    session.add(user)
    session.commit()

