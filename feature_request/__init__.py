from flask import Flask, render_template, send_from_directory
from flask_webpack import Webpack
from config import configure
from models import db

webpack = Webpack()


def init_app(environment=None):
    app = Flask(__name__)

    print "Configuring app"
    app = configure(app, environment)

    register_blueprints(app)
    # DB Initilization
    db.init_app(app)
    # webpack intialization
    webpack.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/assets/<path:path>')
    def assets(path):
        return send_from_directory('build/public', path)

    return app


def register_blueprints(app):
    from feature_request.request.api import request_api
    from feature_request.request.client import client
    from feature_request.request.product import product
    print "Register Blueprints"
    app.register_blueprint(request_api, url_prefix='/api/feature-request')
    app.register_blueprint(client, url_prefix='/api/client')
    app.register_blueprint(product, url_prefix='/api/product')


def run_app(app, host=None, port=None):
    app.run(host=host, port=port)
