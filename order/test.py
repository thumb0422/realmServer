from main import db
from order.orderModel import OrderDetail,OrderMain


detail1 = OrderDetail(orderId='A1',detail1=1)
# detail1.orderId = 'A1'
# detail1.detailId = 1
db.session.add(detail1)
# main1 = OrderMain(orderId='A1',count=5,amount=15.02,states='1')
main1 = OrderMain(orderId='A1',states='N')
# main1.orderId = 'A1'
main1.count = 2
main1.amout = 21.03
# main1.states = 'N'
db.session.add(main1)
db.session.commit()