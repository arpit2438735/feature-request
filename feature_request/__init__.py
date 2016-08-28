from flask import Flask
from config import configure
from models import db

def init_app():
    app = Flask(__name__)

    print "Configuring app"
    app = configure(app)

    # DB Initilization
    db.init_app(app)
    return app


def run_app(app):
    app.run()