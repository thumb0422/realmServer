#-*- coding: UTF-8 -*-
'''
 utility
'''

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    from datetime import date, datetime
    # if isinstance(value,(date,datetime)):
    #     return value.isoformat()
    # return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]
    return value.strftime("%Y-%m-%d")