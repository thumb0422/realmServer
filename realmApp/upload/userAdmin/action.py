# coding: utf-8
from realmApp.upload.userAdmin import Session
from .model import TMAdminUser

class UserAdminAction:

    @classmethod
    def queryUserAdmin(cls,userCode):
        session = Session()
        user = session.query(TMAdminUser).filter(TMAdminUser.userCode == userCode).first()
        return user

    @classmethod
    def registerUserAdmin(cls,*userAdmin):
        pass