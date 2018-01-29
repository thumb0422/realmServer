#-*- coding: UTF-8 -*-
from sqlalchemy import Column, DateTime, Integer, Numeric, String, Text, text
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from realmApp.upload.userAdmin import loginManager,db
from .action import UserAdminAction

class TMAdminUser(UserMixin, db.Model):
    userCode   = db.Column(db.String(64), index=True, unique=True)
    userName   = db.Column(db.String(255))
    userPwd    = db.Column(db.String(128))
    isValid    = db.Column(String(1), server_default=text("'Y'"))
    phone      = db.Column(db.String(30), index=True, unique=True)
    email      = db.Column(db.String(30), index=True, unique=True)
    createDate = db.Column(db.DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updateDate = db.Column(db.DateTime)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_userPwd(self, password):
        self.userPwd = generate_password_hash(password)

    def check_userPwd(self, password):
        return check_password_hash(self.userPwd, password)


@loginManager.user_loader
def load_user(id):
    return UserAdminAction.queryUserAdmin(id)
