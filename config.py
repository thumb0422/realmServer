# -*- coding=utf-8 -*-
'''
要注意的是，这里可以写入多个配置，就仿照DevelopmentConfig这个类一样，继承Config类即可。
并在最下方的Config字典里添加对应的key:value。
'''

import logging
from logging.handlers import RotatingFileHandler

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_ECHO = True
    JSON_AS_ASCII = False
    SQLALCHEMY_POOL_RECYCLE = 2
    SECRET_KEY = '0okmnji9'

    @staticmethod
    def init_app(app):
        _handler = RotatingFileHandler(
            'log.log', maxBytes=10000, backupCount=1)
        _handler.setLevel(logging.WARNING)
        app.logger.addHandler(_handler)

class DevelopmentConfig(Config):
    debug = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./realm.sqlite3'

class MySQLConfig(Config):
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_TIMEOUT = 15
    SQLALCHEMY_DATABASE_URI = 'mysql://root:1qazxsw2@127.0.0.1:3306/realm'

config = {
    'development': DevelopmentConfig,
    'mysql':MySQLConfig
}