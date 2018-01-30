# coding: utf-8
# from . import Session
from ..model import Session
from ..model.model import TMAdminUser

class UserAdminAction:

    @classmethod
    def queryUserAdmin(cls,userName):
        session = Session()
        user = session.query(TMAdminUser).filter(TMAdminUser.userName == userName).first()
        return user

    @classmethod
    def queryUserAdminByCode(cls, userCode):
        session = Session()
        user = session.query(TMAdminUser).filter(TMAdminUser.userCode == userCode).first()
        return user

    @classmethod
    def registerUserAdmin(cls,adminUser):
        session = Session()
        session.add(adminUser)
        try:
            session.flush()
            session.commit()
            return True
        except:
            session.rollback()
            return False
        finally:
            session.close()