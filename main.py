# -*- coding=utf-8 -*-
from flask_script import Manager, Shell
from flask import render_template, redirect, url_for, flash,session
from datetime import timedelta, datetime

from realmApp import create_app, db

app = create_app('default')
app.debug = True

manager = Manager(app)

@manager.command
def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)

@app.before_request
def make_session_permanent():
    # print("#"*80)
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=120)


@app.before_first_request
def before_first_request():
    print ('########### Restarted, first request @ {} ############'.format(
        datetime.utcnow()))

if __name__ == '__main__':
    app.run()
