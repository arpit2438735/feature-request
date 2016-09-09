from feature_request.models import db, ModelBase
from werkzeug.security import generate_password_hash


class User(db.Model, ModelBase):
    email = db.Column(db.String(250), unique=True)
    password = db.Column(db.String(250), default=None, nullable=True)

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % self.email