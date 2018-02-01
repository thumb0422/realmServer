# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField,FloatField,PasswordField
from wtforms.validators import Required,DataRequired,Length
from flask_wtf.file import FileField,FileRequired,FileAllowed
from ..model.staticAction import *
from .action import ProductView
import os

class ProductTypeForm(FlaskForm):
    version = StringField(u'版本名称', validators=[DataRequired('')])
    project = SelectField(u'项目',    choices=StaticDataView.queryProdcuctProjectView(), validators=[DataRequired()])  # key 不能是int
    style   = SelectField(u'款式',    choices=StaticDataView.queryProdcuctStyleView(),   validators=[DataRequired()])  # key 不能是int
    model   = SelectField(u'型号',    choices=StaticDataView.queryProdcuctModelView(),   validators=[DataRequired()])  # key 不能是int
    level   = SelectField(u'单/双层', choices=StaticDataView.queryProdcuctLevelView(),   validators=[DataRequired()])  # key 不能是int
    submit  = SubmitField(u'提交')


class ProductInfoForm(FlaskForm):
    from ..utility import random_str
    productCode = StringField(u'产品代码', validators=[DataRequired(''),Length(min=4,max=4,message=u'必须等于4字符！')],render_kw={"placeholder":random_str(4)})
    productName = StringField(u'产品名称', validators=[DataRequired(''),Length(min=4,max=200,message=u'必须介于4-200字符！')])
    typeCode    = SelectField(u'产品类型', validators=[DataRequired()])  # key 不能是int
    productImg  = FileField(u'选择图片',validators=[FileRequired(u'请选择图片'),FileAllowed(['png','jpg','jpeg'],u'必须为图片类型')])
    costPrice   = FloatField(u'成本价格', validators=[DataRequired(u'必须为数字类型')])
    salePrice   = FloatField(u'销售价格',validators=[DataRequired(u'必须为数字类型')])
    submit = SubmitField(u'提交')


class ProjectForm(FlaskForm):
    code = StringField(u'项目代码', validators=[DataRequired(''),Length(min=3,max=3,message=u'必须等于3字符！')],render_kw={"placeholder":ProductView.queryMaxId()})
    name = StringField(u'项目名称', validators=[DataRequired(''),Length(min=4,max=200,message=u'必须介于4-200字符！')])
    submit = SubmitField(u'提交')

class StyleForm(FlaskForm):
    code = StringField(u'款式代码', validators=[DataRequired(''),Length(min=3,max=3,message=u'必须等于3字符！')],render_kw={"placeholder":'001'})
    name = StringField(u'款式名称', validators=[DataRequired(''),Length(min=4,max=200,message=u'必须介于4-200字符！')])
    submit = SubmitField(u'提交')

class ModelForm(FlaskForm):
    code = StringField(u'型号代码', validators=[DataRequired(''),Length(min=3,max=3,message=u'必须等于3字符！')],render_kw={"placeholder":'001'})
    name = StringField(u'型号名称', validators=[DataRequired(''),Length(min=4,max=200,message=u'必须介于4-200字符！')])
    submit = SubmitField(u'提交')

class LevelForm(FlaskForm):
    code = StringField(u'层次代码', validators=[DataRequired(''),Length(min=3,max=3,message=u'必须等于3字符！')],render_kw={"placeholder":'001'})
    name = StringField(u'层次名称', validators=[DataRequired(''),Length(min=4,max=200,message=u'必须介于4-200字符！')])
    submit = SubmitField(u'提交')
