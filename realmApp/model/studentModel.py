# -*- coding=utf-8 -*-

from sqlalchemy import Column
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,mapper
from datetime import *
import config


enginee = create_engine(config.MySQLConfig.SQLALCHEMY_DATABASE_URI,echo=True)
DBSession = sessionmaker(bind=enginee)
session = DBSession()

class Student(BaseModel):
    __tablename__ = "TM_Student"
    user_name = Column(CHAR(30), primary_key=True)
    pwd = Column(VARCHAR(20), default='aaa', nullable=False)
    age = Column(SMALLINT(), server_default='12')
    accout = Column(INT())
    birthday = Column(TIMESTAMP())
    article = Column(TEXT())
    height = Column(FLOAT())

def init_db():
    BaseModel.metadata.create_all(enginee)

def drop_db():
    BaseModel.metadata.drop_all(enginee)



init_db()

# student = Student(user_name="AAA2",accout=21)
# session.add(student)
# session.commit()

querys = session.query(Student)
print (querys)  # 只显示sql语句，不会执行查询
print (querys[0])  # 执行查询
print (querys.all())  # 执行查询
print (querys.first())  # 执行查询
for query in querys:  # 执行查询
   print (query.user_name)