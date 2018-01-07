# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, Numeric, String, Text, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class TMAddres(Base):
    __tablename__ = 'TM_Address'

    addressId = Column(Integer, primary_key=True)
    userId = Column(Integer)
    address = Column(Text)
    isValid = Column(String(1), server_default=text("'Y'"))
    createDate = Column(DateTime)


class TMGroup(Base):
    __tablename__ = 'TM_Group'

    groupId = Column(Integer, primary_key=True)
    groudCode = Column(String(30))
    isValid = Column(String(1), server_default=text("'Y'"))
    createDate = Column(DateTime)


class TMOrderDetail(Base):
    __tablename__ = 'TM_OrderDetail'

    detailId = Column(Integer, primary_key=True)
    orderId = Column(Integer, nullable=False)
    productCode = Column(String(30), nullable=False)
    salePrice = Column(Numeric(10, 2))
    saleCount = Column(Numeric(10, 2))
    saleAmount = Column(Numeric(10, 2))
    isValid = Column(String(1), server_default=text("'Y'"))
    createDate = Column(DateTime)
    updateDate = Column(DateTime)


class TMOrderMain(Base):
    __tablename__ = 'TM_OrderMain'

    orderId = Column(Integer, primary_key=True)
    orderCode = Column(String(30), nullable=False)
    sumCount = Column(Numeric(10, 2))
    sumAmout = Column(Numeric(10, 2))
    isValid = Column(String(1))
    userId = Column(Integer, nullable=False)
    addressId = Column(Integer)
    createDate = Column(DateTime)
    updateDate = Column(DateTime)


class TMProduct(Base):
    __tablename__ = 'TM_Product'

    productId = Column(Integer, primary_key=True)
    productCode = Column(String(30))
    productName = Column(String(255))
    typeId = Column(Integer)
    costPrice = Column(Numeric(10, 2))
    salePrice = Column(Numeric(10, 2))
    isValid = Column(String(1), server_default=text("'Y'"))
    defaultImg = Column(String(255))
    createDate = Column(DateTime)
    updateDate = Column(DateTime)


class TMProductType(Base):
    __tablename__ = 'TM_ProductType'

    typeId = Column(Integer, primary_key=True)
    typeCode = Column(String(255))
    isValid = Column(String(1))
    createDate = Column(DateTime)
    updateDate = Column(DateTime)


class TMProductLinkInfo(Base):
    __tablename__ = 'TM_Product_LinkInfo'

    linkInfoId = Column(Integer, primary_key=True)
    productCode = Column(String(30))
    defaultImg = Column(String(255))
    remark = Column(String(255))
    isValid = Column(String(1), server_default=text("'Y'"))
    createDate = Column(DateTime)


class TMUser(Base):
    __tablename__ = 'TM_User'

    userId = Column(Integer, primary_key=True)
    userCode = Column(String(30), nullable=False)
    userName = Column(String(100), nullable=False)
    userPwd = Column(String(255))
    isValid = Column(String(1), server_default=text("'Y'"))
    groupId = Column(Integer)
    addressId = Column(Integer)
    phone = Column(String(30))
    email = Column(String(255))
    createDate = Column(DateTime)
    updateDate = Column(DateTime)


class TMUserLog(Base):
    __tablename__ = 'TM_UserLog'

    logId = Column(Integer, primary_key=True)
    logType = Column(String(10))
    userId = Column(Integer)
    createDate = Column(DateTime)
    remark = Column(String(255))


class TMUserStatu(Base):
    __tablename__ = 'TM_User_Status'

    userId = Column(Integer, primary_key=True)
    isLogin = Column(String(1), server_default=text("'Y'"))
    updateDate = Column(DateTime)
