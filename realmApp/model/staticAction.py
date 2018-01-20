# coding: utf-8
#常量数据查询
from realmApp.model import *
from realmApp.model.model import *
from realmApp.utility import *
from realmApp.utility.alchemyEncoder import *

class StaticDataView:

    @classmethod
    def queryProdcuctProjectView(cls):
        session = Session()
        sqlText = '''SELECT a.projectId,a.projectName FROM TM_Project a  WHERE 1=1 '''
        res = session.execute(text(sqlText)).fetchall()
        resultArray = rowToTuple(res)
        session.close()
        return resultArray

    @classmethod
    def queryProdcuctStyleView(cls):
        session = Session()
        sqlText = '''SELECT a.styleId,a.styleName FROM TM_Style a  WHERE 1=1 '''
        res = session.execute(text(sqlText)).fetchall()
        resultArray = rowToTuple(res)
        session.close()
        return resultArray

    @classmethod
    def queryProdcuctModelView(cls):
        session = Session()
        sqlText = '''SELECT a.modelId,a.modelName FROM TM_Model a WHERE 1=1 '''
        res = session.execute(text(sqlText)).fetchall()
        resultArray = rowToTuple(res)
        session.close()
        return resultArray

    @classmethod
    def queryProdcuctLevelView(cls):
        session = Session()
        sqlText = '''SELECT a.levelId,a.levelName FROM TM_Level a  WHERE 1=1 '''
        res = session.execute(text(sqlText)).fetchall()
        resultArray = rowToTuple(res)
        session.close()
        return resultArray

