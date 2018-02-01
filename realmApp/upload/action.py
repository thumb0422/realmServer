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
                     FROM TM_Product a , producttypeinfoview b WHERE a.isValid='Y' AND  a.typeCode = b.typeCode '''
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

    @classmethod
    def queryProductImgInfo(cls,productCode):
        session = Session()
        sqlText = '''SELECT a.productCode,a.productName,b.defaultImg FROM TM_Product a, TM_Product_LinkInfo b where  a.productCode=b.productCode '''
        sqlDic = {}
        if productCode:
            sqlText = sqlText + 'and a.productCode = :productCode'
            sqlDic['productCode'] = productCode
        res = session.execute(text(sqlText), sqlDic).fetchall()
        productInfos = []
        for row in res:
            row_as_dict = dict(row)
            resultDic = {}
            for (k, v) in row_as_dict.items():
                resultDic[str(k)] = str(v)
                if (str(k) == 'defaultImg'):
                    resultDic['imgUrl'] = '/upload/d/' + str(v)
            productInfos.append(resultDic)
        session.close()
        return productInfos

    @classmethod
    def saveProductTypeInfo(cls,**kwargs):
        session = Session()
        productType = TMProductType()
        version = kwargs['version']
        project = kwargs['project']
        style = kwargs['style']
        model = kwargs['model']
        level = kwargs['level']
        productType.version = version
        productType.projectId = project
        productType.styleId = style
        productType.modelId = model
        productType.levelId = level
        productType.isValid = 'Y'
        querys = session.query(TMProductType).filter(TMProductType.projectId == project, TMProductType.styleId == style,TMProductType.modelId == model,TMProductType.levelId == level,TMProductType.isValid == 'Y').all()
        if querys.__len__()>0:
            query = querys[0]
            query.version = version
            session.add(query)
        else:
            productType.typeCode = 'PT' + str(productType.projectId) + str(productType.styleId) + str(productType.modelId) + str(productType.levelId) + random_str(4)
            session.add(productType)
        try:
            session.flush()
            session.commit()
            return True
        except:
            session.rollback()
            return False
        finally:
            session.close()

    @classmethod
    def saveProductInfo(cls,product,image):
        session = Session()
        productCode = product.productCode
        defaultImg = image

        '''productInfo'''
        querys = session.query(TMProduct).filter(TMProduct.productCode == productCode,TMProduct.isValid == 'Y').all()
        if querys.__len__() > 0:
            query = querys[0]
            query.productName = product.productName
            query.salePrice = product.salePrice
            query.costPrice = product.costPrice
            session.add(query)
        else:
            session.add(product)

        '''img'''
        productLinkInfo = TMProductLinkInfo()
        productLinkInfo.productCode = productCode
        productLinkInfo.defaultImg = defaultImg
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


    @classmethod
    def saveProject(cls,project):
        session = Session()
        session.add(project)
        try:
            session.flush()
            session.commit()
            return True
        except:
            session.rollback()
            return False
        finally:
            session.close()

    @classmethod
    def saveModel(cls,model):
        session = Session()
        session.add(model)
        try:
            session.flush()
            session.commit()
            return True
        except:
            session.rollback()
            return False
        finally:
            session.close()

    @classmethod
    def saveStyle(cls,style):
        session = Session()
        session.add(style)
        try:
            session.flush()
            session.commit()
            return True
        except:
            session.rollback()
            return False
        finally:
            session.close()

    @classmethod
    def saveLevel(cls,level):
        session = Session()
        session.add(level)
        try:
            session.flush()
            session.commit()
            return True
        except:
            session.rollback()
            return False
        finally:
            session.close()