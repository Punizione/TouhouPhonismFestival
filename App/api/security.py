# -*- coding: utf-8 -*-
from __future__ import unicode_literals
""" Security Related things """
from functools import wraps
from flask_restful import abort
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from App import app
import jwt
import datetime
import time
from flask import request, g
def require_auth(func):
    """ Secure method decorator """
    @wraps(func)
    def wrapper(*args, **kwargs):
        header = request.headers.get("Authorization")
        if not header:
            abort(401, message='Not Token')
        else:
            _, token = header.split()
            try:
                decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
            except jwt.DecodeError:
                abort(401)
            except jwt.ExpiredSignatureError:
                abort(401)
            if not decoded['token']:
                abort(401)
            else:
                token = decoded['token']
                g.token = token
                g.difficulty = decoded['difficulty']
                return func(*args, **kwargs)
    return wrapper
