from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from order.orderModel import OrderMain,OrderDetail
from datetime import datetime

app = Flask(__name__)
app.config.from_object('mysqlConfig')
db = SQLAlchemy(app)

db.create_all()
#非关联关系 则正常
ordermain = OrderMain(orderId='001',amount=12,count=22,states='Y',updateDate=datetime.now())
orderId = OrderMain.query.get(1)

orderDetail = OrderDetail(detailId=1,productCode='01',amount=100,count=20,salePrice=30.98,states='N',updateDate=datetime.now(),orderId=orderId)

db.session.add(ordermain,orderDetail)
db.session.commit()