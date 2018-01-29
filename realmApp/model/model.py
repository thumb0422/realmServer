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
    createDate = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))


class TMGroup(Base):
    __tablename__ = 'TM_Group'

    groupId = Column(Integer, primary_key=True)
    groudCode = Column(String(30))
    isValid = Column(String(1), server_default=text("'Y'"))
    createDate = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))


class TMLevel(Base):
    __tablename__ = 'TM_Level'

    levelId = Column(String(5), primary_key=True)
    levelName = Column(String(255))
    isValid = Column(String(1), server_default=text("'Y'"))


class TMModel(Base):
    __tablename__ = 'TM_Model'

    modelId = Column(String(5), primary_key=True)
    modelName = Column(String(255))
    isValid = Column(String(1), server_default=text("'Y'"))


class TMOrderDetail(Base):
    __tablename__ = 'TM_OrderDetail'

    detailId = Column(Integer, primary_key=True)
    orderId = Column(Integer, nullable=False)
    productCode = Column(String(30), nullable=False)
    salePrice = Column(Numeric(10, 2))
    saleCount = Column(Numeric(10, 2))
    saleAmount = Column(Numeric(10, 2))
    isValid = Column(String(1), server_default=text("'Y'"))
    createDate = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
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
    createDate = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updateDate = Column(DateTime)


class TMProduct(Base):
    __tablename__ = 'TM_Product'

    productId = Column(Integer, primary_key=True)
    productCode = Column(String(30), nullable=False)
    productName = Column(String(255), nullable=False)
    typeCode = Column(String(30), nullable=False)
    costPrice = Column(Numeric(10, 2))
    salePrice = Column(Numeric(10, 2))
    isValid = Column(String(1), server_default=text("'Y'"))
    createDate = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updateDate = Column(DateTime)


class TMProductType(Base):
    __tablename__ = 'TM_ProductType'

    typeCode = Column(String(30), primary_key=True)
    typeName = Column(String(255))
    version = Column(String(255))
    projectId = Column(String(5))
    styleId = Column(String(5))
    modelId = Column(String(5))
    levelId = Column(String(5))
    isValid = Column(String(1), server_default=text("'Y'"))
    createDate = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updateDate = Column(DateTime)


class TMProductLinkInfo(Base):
    __tablename__ = 'TM_Product_LinkInfo'

    linkInfoId = Column(Integer, primary_key=True)
    productCode = Column(String(30))
    defaultImg = Column(String(255))
    remark = Column(String(255))
    isValid = Column(String(1), server_default=text("'Y'"))
    createDate = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))


class TMProject(Base):
    __tablename__ = 'TM_Project'

    projectId = Column(String(5), primary_key=True)
    projectName = Column(String(255))
    isValid = Column(String(1), server_default=text("'Y'"))


class TMStyle(Base):
    __tablename__ = 'TM_Style'

    styleId = Column(String(5), primary_key=True)
    styleName = Column(String(255))
    isValid = Column(String(1), server_default=text("'Y'"))


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
    createDate = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updateDate = Column(DateTime)


class TMUserLog(Base):
    __tablename__ = 'TM_UserLog'

    logId = Column(Integer, primary_key=True)
    logType = Column(String(10))
    userId = Column(Integer)
    createDate = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    remark = Column(String(255))


class TMUserStatu(Base):
    __tablename__ = 'TM_User_Status'

    userId = Column(Integer, primary_key=True)
    isLogin = Column(String(1), server_default=text("'Y'"))
    updateDate = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))


class TMAdminUser(Base):
    __tablename__ = 'TM_Admin_User'

    userCode = Column(String(30), primary_key=True)
    userName = Column(String(100))
    userPwd = Column(String(255))
    isValid = Column(String(1), server_default=text("'Y'"))
    phone = Column(String(30))
    email = Column(String(255))
    createDate = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updateDate = Column(DateTime)