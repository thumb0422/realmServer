# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import Required,DataRequired
from realmApp.model.staticAction import *

class ProductForm(FlaskForm):
    version = StringField(u'版本名称', validators=[DataRequired('')])
    # project = StringField(u'项目', validators=[DataRequired()])
    # style   = StringField(u'款式', validators=[DataRequired()])
    # model   = StringField(u'型号', validators=[DataRequired()])
    # level   = StringField(u'单/双层', validators=[DataRequired()])

    project = SelectField(u'项目',   choices=StaticDataView.queryProdcuctProjectView(), validators=[DataRequired()])  # key 不能是int
    style   = SelectField(u'款式',   choices=StaticDataView.queryProdcuctStyleView(),   validators=[DataRequired()])  # key 不能是int
    model   = SelectField(u'型号',   choices=StaticDataView.queryProdcuctModelView(),   validators=[DataRequired()])  # key 不能是int
    level   = SelectField(u'单/双层',choices=StaticDataView.queryProdcuctLevelView(),    validators=[DataRequired()])  # key 不能是int
    submit  = SubmitField(u'提交')