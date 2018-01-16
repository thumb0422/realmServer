# -*- coding=utf-8 -*-
from . import upload
from realmApp.model.model import *
from flask import jsonify,request,make_response,abort,render_template,send_from_directory,flash,redirect,url_for
from realmApp.utility.Response import *
from realmApp.utility import *
from realmApp.model.productAction import *

from werkzeug.utils import secure_filename
from flask import Flask,render_template,jsonify,request
import time
import os
import base64
import uuid

UPLOAD_FOLDER = 'image'
basedir = os.path.abspath(os.path.dirname(__file__))
from manage import app
basedir = app.root_path
ALLOWED_EXTENSIONS = set(['png','jpg','JPG','PNG','gif','GIF'])

# 用于判断文件后缀
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

'''图片上传html'''
@upload.route('/')
def upload_test():
    return render_template('upload.html')

'''图片上传'''
@upload.route('/u',methods = ['POST'],strict_slashes=False)
def uploadProductImg():
    file_dir = os.path.join(basedir, UPLOAD_FOLDER)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['myfile']  # 从表单的file字段获取文件，myfile为该表单的name值
    if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型
        fname = secure_filename(f.filename)
        print(fname)
        ext = fname.rsplit('.', 1)[1]  # 获取文件后缀
        unix_time = int(time.time())
        new_filename = str(uuid.uuid1()) + '.' + ext  # 修改了上传的文件名
        f.save(os.path.join(file_dir, new_filename))  # 保存文件到upload目录
        # token = base64.b64encode(new_filename)
        # print(token)
        token = ''
        flash(u'上传成功')
        # return jsonify({"errno": 0, "errmsg": "上传成功", "token": token})
    else:
        flash(u'上传失败')
        # return jsonify({"errno": 1001, "errmsg": "上传失败"})
    #return render_template('upload.html')
    return redirect(url_for('upload.upload_test'))



'''图片下载'''
@upload.route("/d/<path:filename>")
def downloader(filename):
    dirpath = os.path.join(basedir, UPLOAD_FOLDER)  # 这里是下在目录，从工程的根目录写起，比如你要下载static/js里面的js文件，这里就要写“static/js”
    return send_from_directory(dirpath, filename, as_attachment=False)  # as_attachment=True 一定要写，不然会变成打开，而不是下载
