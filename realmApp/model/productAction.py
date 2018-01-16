# coding: utf-8
from sqlalchemy.ext.declarative import DeclarativeMeta
from realmApp.model import *
from realmApp.model.model import *
from realmApp.utility import *
from realmApp.utility.Response import *
from realmApp.utility.alchemyEncoder import *

class ProductView:

    '''单个产品的信息'''
    @classmethod
    def queryProductCode(cls,productCode):
        session = Session()
        sqlText = '''SELECT a.productCode,a.productName,a.costPrice,a.salePrice,b.typeCode,b.version,b.styleName,b.projectName,b.modelName,b.levelName 
                     FROM TM_Product a , producttypeinfoview b WHERE a.isValid='Y' AND  a.typeCode = b.typeCode'''
        sqlDic = {}
        if productCode:
            sqlText = sqlText + 'and productCode = :productCode'
            sqlDic['productCode'] = productCode
        res = session.execute(text(sqlText), sqlDic).fetchall()
        resultArray = rowToArray(res)
        session.close()
        return DataResopnse(0, '查询成功', resultArray).toJson()

    '''首页几个轮动的屏幕图片'''
    @classmethod
    def queryProductThree(cls):
        pass

    '''首页分类汇总'''
    @classmethod
    def queryProductHome(cls):
        pass;

    '''单个分类里的内容'''
    @classmethod
    def queryProductByType(cls,type):
        pass

    '''存储图片位置表'''
    @classmethod
    def saveProductImgInfo(cls,**kwargs):
        session = Session()
        productLinkInfo = TMProductLinkInfo()
        productLinkInfo.productCode = kwargs['productCode']
        productLinkInfo.defaultImg = kwargs['defaultImg']
        productImgInfos = session.query(TMProductLinkInfo).filter(TMProductLinkInfo.productCode == productLinkInfo.productCode).all()
        for productImgInfo in productImgInfos:
            session.delete(productImgInfo)
        session.add(productLinkInfo)
        try:
            session.flush()
            session.commit()
            return True
        except:
            session.rollback()
            return False
        finally:
            session.close()

