from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from order.orderModel import OrderMain,OrderDetail
from datetime import datetime
import random
import math

app = Flask(__name__)
app.config.from_object('mysqlConfig')
db = SQLAlchemy(app)
#
# db.create_all()


ordermains = OrderMain.query.get(1)
print(ordermains)
# db.session.delete(ordermains)


# orderIds = ['00001','00002','00003','00004','00005','00006']
# for orderId  in orderIds:
#     orderMain = OrderMain(orderId,round(random.random(),2),random.randint(1,1000),random.choices(["Y","N"]),datetime.now())
#     orderMain.updateDate = datetime.now()
#     db.session.add(orderMain)
#
# db.session.commit()
