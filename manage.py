# -*- coding=utf-8 -*-
from app import create_app, db
from app.model.orderModel import OrderMain,OrderDetail
from app.model.userModel import User,Group

from flask.ext.script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app('development')
manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('db', MigrateCommand)   #在终端环境下添加一个db命令

if __name__ == '__main__':
    manager.run()