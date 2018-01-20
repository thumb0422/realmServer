# -*- coding=utf-8 -*-
from flask import render_template
from realmApp.upload import *
from .uForm import *
from .ProductForm import *
from realmApp.model.productAction import *

'''产品 信息展示'''
@upload.route('/index',methods=['GET', 'POST'])
def index():
    pass

'''TM_Product 产品信息 表数据维护'''
@upload.route('/index/infoAdd',methods=['GET', 'POST'])
def infoAdd():
    pass

'''TM_ProductType 产品类型 表数据维护'''
@upload.route('/index/typeAdd',methods=['GET', 'POST'])
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