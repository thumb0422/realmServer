# -*- coding=utf-8 -*-

'''
要注意的是，这里可以写入多个配置，就仿照DevelopmentConfig这个类一样，继承Config类即可。
并在最下方的Config字典里添加对应的key:value。
'''

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_ECHO = True
    JSON_AS_ASCII = False
    SQLALCHEMY_POOL_RECYCLE = 2
    SECRET_KEY = '0okmnji9'

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./data.db'

class ProductionConfig(Config):
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_TIMEOUT = 15
    SQLALCHEMY_DATABASE_URI = 'mysql://root:1qazxsw2@127.0.0.1:3306/realm'

config = {
    'default': DevelopmentConfig,
    'production':ProductionConfig
}