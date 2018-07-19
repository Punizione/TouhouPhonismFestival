# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_url_path='')


# Flask-Security
app.config['SECRET_KEY'] = "Delitto"
app.config['SECURITY_TOKEN_AUTHENTICATION_HEADER'] = "Delitto"


# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:000000@127.0.0.1:3306/vma'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from . import config
app.logger.info('>>> {}'.format(app.config['MODE']))

db = SQLAlchemy(app)

from App.api import api_rest, api_bp
from App.client import client_bp

# Flask-Blueprint
app.register_blueprint(api_bp)
app.register_blueprint(client_bp)