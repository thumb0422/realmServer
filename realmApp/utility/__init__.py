#-*- coding: UTF-8 -*-
'''
 utility
'''
from random import Random
import json,decimal
import datetime

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return value.strftime("%Y-%m-%d")

def random_str(randomLength = 12):
    str = ''
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomLength):
        str += chars[random.randint(0, length)]
    return str

def getModelKey(keyPrefix):
    localTimeStr = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    localTime = localTimeStr.replace('-', '').replace(':', '').replace('.', '').replace(' ', '')
    result = keyPrefix + localTime + random_str(4).upper()
    return result

'''JSON 转 Dictionary'''
def converJsonToDic(jsonValue):
    jsonStr = json.dumps(jsonValue)
    dic = eval(jsonStr)
    return dic

'''对象转Dictionary'''
def classToDict(obj):
    is_list = obj.__class__ == [].__class__
    is_set = obj.__class__ == set().__class__

    if is_list or is_set:
        obj_arr = []
        for o in obj:
            dict = {}
            dict.update(o.__dict__)
            obj_arr.append(dict)
        return obj_arr
    else:
        dict = {}
        dict.update(obj.__dict__)
        return dict

def alchemyencoder(obj):
    """JSON encoder function for SQLAlchemy special classes."""
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)

def row2Array(rows):
    d = []
    for row in rows:
        row_as_dict = dict(row)
        d.append(row_as_dict)
    # d = {}
    # for column in row.__table__.columns:
    #     d[column.name] = str(getattr(row, column.name))

    return d