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
