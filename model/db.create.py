from model.user import db,Teacher

db.create_all()

t1 = Teacher('T1','11111')
t2 = Teacher('T2','22222')

db.session.add(t1)
db.session.add(t2)
db.session.commit();