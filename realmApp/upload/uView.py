# -*- coding=utf-8 -*-
from flask import render_template, flash
from flask_login import login_required

from realmApp.upload.action import *
from .form import *
from ..upload import *

UPLOAD_FOLDER = 'image'
basedir = os.path.abspath(os.path.dirname(__file__))
from manage import app
basedir = app.root_path
# ALLOWED_EXTENSIONS = set(['png','jpg','JPG','PNG','gif','GIF'])

'''产品首页'''
@upload.route('/index',methods=['GET', 'POST'])
@login_required
def index():
    return render_template('productIndex.html',title =u'首页')

'''产品 信息展示'''
@upload.route('/infos',methods=['GET', 'POST'])
@login_required
def infos():
    list = []
    # productCode = request.form['productId']
    productCode = ''
    headlist = {"productCode": "产品代码", "productName": "产品名称", "imgUrl": "图片显示"}
    list = ProductView.queryProductImgInfo(productCode)
    return render_template('productInfo.html',title=u'产品 信息展示',headlist=headlist,list = list)

'''TM_Product 产品信息 表数据维护'''
@upload.route('/infoAdd',methods=['GET', 'POST'])
@login_required
def infoAdd():
    name = None
    form = ProductInfoForm()
    form.typeCode.choices = [(v[0], v[1]) for v in StaticDataView.queryProdcuctTypeView()]
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
            message = '提交成功'
        else:
            message = '提交失败'
        flash(message)
    return render_template('productInfoAdd.html', form=form,title=u'产品信息维护')

'''TM_ProductType 产品类型 表数据维护'''
@upload.route('/typeAdd',methods=['GET', 'POST'])
@login_required
def typeAdd():
    name = None
    form = ProductTypeForm()
    ''' 如果这些数据变化比较频繁，需要放开这个以便能实时更新
    form.project.choices = [(v[0], v[1]) for v in StaticDataView.queryProdcuctProjectView()]
    form.style.choices = [(v[0], v[1]) for v in StaticDataView.queryProdcuctStyleView()]
    form.model.choices = [(v[0], v[1]) for v in StaticDataView.queryProdcuctModelView()]
    form.level.choices = [(v[0], v[1]) for v in StaticDataView.queryProdcuctLevelView()]
    '''
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
            message = '提交成功'
        else:
            message = '提交失败'
        flash(message)
    return render_template('productType.html', form=form,title=u'产品类型维护')


'''TM_Project 产品类型项目 表数据维护'''
@upload.route('/project',methods=['GET', 'POST'])
@login_required
def project():
    name = None
    form = ProjectForm()
    # 如果提交的数据验证通过，则返回True
    if form.validate_on_submit():
        code = form.code.data
        form.code.data = ''
        name = form.name.data
        form.name.data = ''
        project = TMProject()
        project.projectId = code
        project.projectName = name
        project.isValid = 'Y'
        '''save Data'''
        if ProductView.saveProject(project):
            message = '提交成功'
        else:
            message = '提交失败'
        flash(message)
    return render_template('project.html', form=form,title=u'项目维护')

'''TM_Style 产品类型款式 表数据维护'''
@upload.route('/style',methods=['GET', 'POST'])
@login_required
def style():
    name = None
    form = StyleForm()
    # 如果提交的数据验证通过，则返回True
    if form.validate_on_submit():
        code = form.code.data
        form.code.data = ''
        name = form.name.data
        form.name.data = ''
        style = TMStyle()
        style.styleId = code
        style.styleName = name
        style.isValid = 'Y'
        '''save Data'''
        if ProductView.saveStyle(style):
            message = '提交成功'
        else:
            message = '提交失败'
        flash(message)
    return render_template('style.html', form=form,title=u'款式维护')

'''TM_Project 产品类型型号 表数据维护'''
@upload.route('/model',methods=['GET', 'POST'])
@login_required
def model():
    name = None
    form = ModelForm()
    # 如果提交的数据验证通过，则返回True
    if form.validate_on_submit():
        code = form.code.data
        form.code.data = ''
        name = form.name.data
        form.name.data = ''
        model = TMModel()
        model.modelId = code
        model.modelName = name
        model.isValid = 'Y'
        '''save Data'''
        if ProductView.saveModel(model):
            message = '提交成功'
        else:
            message = '提交失败'
        flash(message)
    return render_template('model.html', form=form,title=u'型号维护')

'''TM_Project 产品类型层次 表数据维护'''
@upload.route('/level',methods=['GET', 'POST'])
@login_required
def level():
    name = None
    form = LevelForm()
    # 如果提交的数据验证通过，则返回True
    if form.validate_on_submit():
        code = form.code.data
        form.code.data = ''
        name = form.name.data
        form.name.data = ''
        level = TMLevel()
        level.levelId = code
        level.levelName = name
        level.isValid = 'Y'
        '''save Data'''
        if ProductView.saveLevel(level):
            message = '提交成功'
        else:
            message = '提交失败'
        flash(message)
    return render_template('level.html', form=form,title=u'层次维护')