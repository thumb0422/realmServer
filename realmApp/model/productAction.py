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
    def queryProductByProductCode(cls):
        pass

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

