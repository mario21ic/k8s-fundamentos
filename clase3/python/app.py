#!/usr/bin/env python

"""
Inicia en 5 segundos
/live demora 1 segundo y funciona al 1er intento
/ready demora 1 segundo y funciona al 3er intento
/ demora 1 segundo
"""

import os
import time

from bottle import route, run, template, response


@route('/error')
def myerror():
    print("/error sleep 1sec")
    response.status = 500
    return "Error in server"

@route('/redirect')
def redirect():
    print("/redirect 301")
    response.status = 301
    return "OK"

@route('/live')
def live():
    print("/live sleep 1sec")
    time.sleep(1)
    return "OK"

intento=1
@route('/ready')
def ready():
    time.sleep(1)
    global intento
    print("/ready intento: ", intento)
    if intento>=3:
        return "OK"
    intento+=1
    response.status = 404
    return "Try again"


@route('/')
def index():
    time.sleep(1)
    return template('<b>MY_KEY: {{my_value}}<br/>foo: {{foo}}</b>!', my_value=os.environ['MY_KEY'], foo=os.environ['foo'])


print("Starting in 3 sec")
time.sleep(5)
run(host='0.0.0.0', port=8080)

