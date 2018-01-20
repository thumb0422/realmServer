# -*- coding=utf-8 -*-
from realmApp import create_app, db
from realmApp.model.orderModel import OrderMain,OrderDetail
from realmApp.model.userModel import User,Group

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask_bootstrap import Bootstrap

app = create_app('mysql')
app.config['SECRET_KEY'] = 'hard to guess string'
manager = Manager(app)
bootstrap = Bootstrap(app)
migrate = Migrate(app,db)

manager.add_command('db', MigrateCommand)   #在终端环境下添加一个db命令

if __name__ == '__main__':
    manager.run()