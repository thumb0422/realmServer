# -*- coding=utf-8 -*-
from app import create_app, db

app = create_app('default')
app.debug = True

if __name__ == '__main__':
    app.run()
