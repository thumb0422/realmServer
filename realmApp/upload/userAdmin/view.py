#-*- coding: UTF-8 -*-
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from .. import upload
from .form import LoginForm, RegistrationForm
from .action import UserAdminAction

@upload.route('/')
@upload.route('/index')
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


@upload.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = UserAdminView.queryUserAdmin(userCode=form.username.data)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('userAdmin/login.html', title='Sign In', form=form)


@upload.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@upload.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = UserAdminView.queryUserAdmin(userCode=form.username.data)
        UserAdminView.registerUserAdmin(user)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('userAdmin/register.html', title='Register', form=form)
