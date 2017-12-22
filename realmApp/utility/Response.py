#-*- coding: UTF-8 -*-
from flask import jsonify

class DataResopnse(object):
    # status = '0'
    # message = ''
    # datas = []
    # count = 0

    def __init__(self,status,message,datas):
        self.status = status
        self.message = message
        self.datas = datas
        self.count = datas.__len__()

    def toJson(self):
        return jsonify({"status":self.status,'message':self.message,"count":self.count,"datas":self.datas})