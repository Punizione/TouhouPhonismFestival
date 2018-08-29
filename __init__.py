# -*- coding: utf-8 -*-
from __future__ import unicode_literals



app = Flask(__name__, static_url_path='')


# Flask-Security
app.config['SECRET_KEY'] = "Delitto"
app.config['SECURITY_TOKEN_AUTHENTICATION_HEADER'] = "Delitto"
app.config['SECURITY_TOKEN_HOUR'] = 2

# Database

from . import config
app.logger.info('>>> {}'.format(app.config['MODE']))

db = SQLAlchemy(app)

from App.api import api_rest, api_bp
from App.client import client_bp

# Flask-Blueprint
app.register_blueprint(api_bp)
app.register_blueprint(client_bp)