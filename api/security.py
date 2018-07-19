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
                abort(400)
            except jwt.ExpiredSignatureError:
                abort(400)
            if not decoded['token']:
                abort(401)
            else:
                token = None #Todo  decoded['token']
                if not token:
                    abort(401)
                else:
                    g.token = token
                    g.difficulty = decoded['difficult']
                    g.randomID = decoded['randomID']
                    return func(*args, **kwargs)

