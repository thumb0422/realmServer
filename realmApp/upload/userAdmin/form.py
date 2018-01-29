#-*- coding: UTF-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from .action import UserAdminAction

class LoginForm(FlaskForm):
    username = StringField(u'用户名', validators=[DataRequired()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    remember_me = BooleanField(u'记住我')
    submit = SubmitField(u'登录')


class RegistrationForm(FlaskForm):
    username = StringField(u'用户名', validators=[DataRequired()])
    email = StringField(u'Email', validators=[DataRequired(), Email()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    password2 = PasswordField(
        u'确认密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(u'注册')

    def validate_username(self, username):
        user = UserAdminAction.queryUserAdmin(username.data)
        if user is not None:
            raise ValidationError('该用户名已被注册')

    # def validate_email(self, email):
    #     user = User.query.filter_by(email=email.data).first()
    #     user = UserAdminView.queryUserAdmin(username.data)
    #     if user is not None:
    #         raise ValidationError('Please use a different email address.')
