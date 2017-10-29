from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from main import db

class trans_inst(db.Model):
    __tablename__ = 'TRANS_INST'
    __table_args__ = 'test'  # 查询带上库名前缀
    TRANS_ID = db.Column(db.INTEGER, primary_key=True)
    TITLE = db.Column(db.VARCHAR(255), nullable=False)
    VERSION_ID = db.Column(db.INTEGER)
    PROJECT_ID = db.Column(db.INTEGER, nullable=False)
    TEMPLET_ID = db.Column(db.INTEGER)
    STAFF_ID = db.Column(db.INTEGER, nullable=False)
    CREATE_DATE = db.Column(db.DATE)
    STATE = db.Column(db.CHAR(1))
    PATCH_ID = db.Column(db.INTEGER, db.ForeignKey(version_patch.PATCH_ID))
    UP_TRANS_ID = db.Column(db.INTEGER)  # 子单/关联单ID
    TYPE = db.Column(db.CHAR(1))  # 子单关联单类型
    SUBMITTER = db.Column(db.INTEGER)


class version_patch(db.Model):
    """
    补丁（版本）定义表
    """
    __tablename__ = 'VERSION_PATCH'
    __table_args__ = 'test'         # 查询带上库名前缀

    PATCH_ID = db.Column(db.INTEGER, primary_key=True)
    VERSION_ID = db.Column(db.INTEGER)                   # 版本标识
    UP_PATCH_ID = db.Column(db.INTEGER)
    PATCH_CODE = db.Column(db.VARCHAR(255))
    patchcode = db.relationship("trans_inst")