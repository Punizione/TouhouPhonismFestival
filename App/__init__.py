# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask

import sys

app = Flask(__name__, static_url_path='')


# Flask-Security
app.config['SECRET_KEY'] = "Delitto"
app.config['SECURITY_TOKEN_AUTHENTICATION_HEADER'] = "Delitto"
app.config['WTF_CSRF_ENABLED'] = False
app.config['SECURITY_TOKEN_USER_HOUR'] = 1
app.config['SECURITY_TOKEN_VISITOR_HOUR'] = 1
app.config['SECURITY_UNAUTHORIZED_VIEW'] = '/'

# Database


#Constant

from . import config
app.logger.info('>>> {}'.format(app.config['MODE']))




from App.api import api_rest, api_bp
from App.client import client_bp

# Flask-Blueprint
app.register_blueprint(api_bp)
app.register_blueprint(client_bp)