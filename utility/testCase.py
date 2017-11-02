from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from main import db

app = Flask(__name__)
app.config.from_object('mysqlConfig')
db = SQLAlchemy(app)

class student(db.Model):
    userCode = db.Column(db.String(10), primary_key=True)
    userName = db.Column(db.String(250),nullable=False)


db.create_all()



# student1 = student(userCode='001',userName='A1')
# student2 = student(userCode='002',userName='B2')
# student3 = student(userCode='003',userName='C3')
# student4 = student(userCode='004',userName='D4')
# student5 = student(userCode='005',userName='G5')
# db.session.add(student1)
# db.session.add(student2)
# db.session.add(student3)
# db.session.add(student4)
# db.session.add(student5)
# db.session.commit()



students = student.query.all()
print(students)