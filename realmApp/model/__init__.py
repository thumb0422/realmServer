#-*- coding: UTF-8 -*-
'''
数据模型
'''

'''数据库连接'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,mapper
import config

enginee = create_engine(config.MySQLConfig.SQLALCHEMY_DATABASE_URI,echo=True)
Session = sessionmaker(bind=enginee)
# session = Session()