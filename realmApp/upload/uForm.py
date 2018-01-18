# -*- coding=utf-8 -*-
from flask_wtf import FlaskForm as Form
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, FloatField, SelectField
from wtforms.validators import Required, length, Regexp, EqualTo
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class ProductInfoForm(Form):
    payment = SelectField(u'payment', choices=[('wallet', 'wallet'), ('bank_card', 'bank_card')], default='bank_card')
    wallet = FloatField(u'wallet')

    bank_card = FloatField(u'bank_card')

    submit = SubmitField(u'pay')