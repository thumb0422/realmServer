# -*- coding=utf-8 -*-
from flask import render_template
from realmApp.upload import *
from .uForm import *
from .ProductForm import *

@upload.route('/abc')
def queryPrp():
    form = ProductInfoForm()
    return render_template('productInfo.html', form=form)
    # return render_template('productInfo.html')


@upload.route('/index',methods=['GET', 'POST'])
def index():
    name = None
    form = ProductForm()
    # 如果提交的数据验证通过，则返回True
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('productIndex.html', form=form, name=name)

@upload.route('/add',methods=['GET', 'POST'])
def add():
    name = None
    form = ProductForm()
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
        name = '提交成功'
    return render_template('productAdd.html', form=form, name=name)