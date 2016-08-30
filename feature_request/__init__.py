from flask import Flask
from config import configure
from models import db


def init_app(environment=None):
    app = Flask(__name__)

    print "Configuring app"
    app = configure(app, environment)

    register_blueprints(app)
    # DB Initilization
    db.init_app(app)

    return app


def register_blueprints(app):
    from feature_request.request.api import request_api

    print "Register Blueprints"
    app.register_blueprint(request_api, url_prefix='/api/feature-request')


def run_app(app):
    app.run()
