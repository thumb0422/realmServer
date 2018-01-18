# -*- coding=utf-8 -*-
from flask import render_template
from realmApp.upload import *
from .uForm import *

@upload.route('/abc')
def queryPrp():
    form = ProductInfoForm()
    return render_template('productInfo.html', form=form)
    # return render_template('productInfo.html')