#-*- coding: UTF-8 -*-
'''
 utility
'''
from random import Random

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    from datetime import date, datetime
    # if isinstance(value,(date,datetime)):
    #     return value.isoformat()
    # return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]
    return value.strftime("%Y-%m-%d")

def random_str(randomLength = 12):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomLength):
        str += chars[random.randint(0, length)]
    return str