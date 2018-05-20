#-*- coding: UTF-8 -*-
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse

from . import admin
from .action import UserAdminAction
from .form import LoginForm, RegistrationForm
from ..model.model import TMAdminUser


@admin.route('/')
@admin.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('userAdmin/index.html', title='Home', posts=posts)


@admin.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        # return redirect(url_for('/admin.index'))
        return redirect(url_for('upload.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = UserAdminAction.queryUserAdmin(userName=form.username.data)
        if user is None or not user.check_userPwd(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('/admin.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            # next_page = url_for('/admin.index')
            next_page = url_for('upload.index')
        return redirect(next_page)
    return render_template('userAdmin/login.html', title='Sign In', form=form)


@admin.route('/logout')
def logout():
    logout_user()
    # return redirect(url_for('/admin.index'))
    return redirect(url_for('upload.index'))


@admin.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        # return redirect(url_for('/admin.index'))
        return redirect(url_for('upload.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        adminUser = TMAdminUser()
        from ..utility import random_str
        adminUser.userCode = 'AU' + random_str(8)
        adminUser.set_userPwd(form.password.data)
        adminUser.email = form.email.data
        adminUser.isValid = 'Y'
        adminUser.userName = form.username.data
        if UserAdminAction.registerUserAdmin(adminUser):
            flash(u'恭喜,注册成功!')
        else:
            flash(u'注册失败!')
        return redirect(url_for('/admin.login'))
    return render_template('userAdmin/register.html', title='Register', form=form)

from .. import loginManager
@loginManager.user_loader
def load_user(user_id):
        return UserAdminAction.queryUserAdminByCode(user_id)