import shortuuid
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ModelBase:
    id = db.Column(db.String(22), primary_key=True, default=shortuuid.uuid)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)

    def __init__(self):
        pass

    @staticmethod
    def create(resource):
        db.session.add(resource)
        return db.session.commit()

    @staticmethod
    def update():
        return db.session.commit()

    @staticmethod
    def delete(resource):
        db.session.delete(resource)
        return db.session.commit()

    @classmethod
    def get(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def find_all(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()