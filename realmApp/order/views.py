# -*- coding=utf-8 -*-
from . import order


@order.route('/')
def index():
    return 'Hello World I am order'