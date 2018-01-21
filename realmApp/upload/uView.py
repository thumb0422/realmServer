# -*- coding=utf-8 -*-
from flask import render_template
from realmApp.upload import *
from .ProductForm import *
from realmApp.model.productAction import *

UPLOAD_FOLDER = 'image'
basedir = os.path.abspath(os.path.dirname(__file__))
from manage import app
basedir = app.root_path
# ALLOWED_EXTENSIONS = set(['png','jpg','JPG','PNG','gif','GIF'])

'''产品 信息展示'''
@upload.route('/index',methods=['GET', 'POST'])
def index():
    return render_template('productIndex.html')

'''TM_Product 产品信息 表数据维护'''
@upload.route('/infoAdd',methods=['GET', 'POST'])
def infoAdd():
    name = None
    form = ProductInfoForm()
    if form.validate_on_submit():
        productCode = form.productCode.data
        productName = form.productName.data
        productTypeCode = form.typeCode.data
        productSalePrice = form.salePrice.data
        productCostPrice = form.costPrice.data
        productImg = form.productImg.data
        '''清空数据'''
        form.productCode.data = ''
        form.productName.data = ''
        form.typeCode.data = ''
        form.salePrice.data = ''
        form.costPrice.data = ''
        form.productImg.data = ''

        from werkzeug.utils import secure_filename
        import time
        import os
        import base64
        import uuid

        f = productImg
        file_dir = os.path.join(basedir, UPLOAD_FOLDER)
        fname = secure_filename(f.filename)
        ext = fname.rsplit('.', 1)[1]  # 获取文件后缀
        unix_time = int(time.time())
        new_filename = str(uuid.uuid1()) + '.' + ext  # 修改了上传的文件名
        f.save(os.path.join(file_dir, new_filename))  # 保存文件到upload目录

        product = TMProduct()
        product.typeCode = productTypeCode
        product.productCode = productTypeCode + productCode
        product.productName = productName
        product.salePrice = productSalePrice
        product.costPrice = productCostPrice
        if ProductView.saveProductInfo(product,new_filename):
            name = '提交成功'
        else:
            name = '提交失败'
    return render_template('productInfoAdd.html', form=form,name=name)

'''TM_ProductType 产品类型 表数据维护'''
@upload.route('/typeAdd',methods=['GET', 'POST'])
def typeAdd():
    name = None
    form = ProductTypeForm()
    # 如果提交的数据验证通过，则返回True
    if form.validate_on_submit():
        version = form.version.data
        form.version.data = ''
        project = form.project.data
        form.project.data = ''
        style = form.style.data
        form.style.data = ''
        model = form.model.data
        form.model.data = ''
        level = form.level.data
        form.level.data = ''

        '''save Data'''
        productInfoDic = {'version':version,'project':project,'style':style,'model':model,'level':level}
        if ProductView.saveProductTypeInfo(**productInfoDic):
            name = '提交成功'
        else:
            name = '提交失败'
    return render_template('productType.html', form=form, name=name)