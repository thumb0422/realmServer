# -*- coding=utf-8 -*-
from . import user


@user.route('/')
def index():
    return 'Hello World I am user'