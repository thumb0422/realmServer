#-*- coding: UTF-8 -*-
from realmApp.model.userModel  import User
import datetime
import random
from uuid import uuid4

user = User()
user.userId = random.randint(1,1000)
user.states='Y'
user.userName = 'Tom'
db.session.add(user)
db.session.commit()
