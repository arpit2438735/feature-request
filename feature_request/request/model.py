import shortuuid
from datetime import datetime

from feature_request.models import ModelBase, db


class Client(db.Model, ModelBase):
    name = db.Column(db.String(50), default=None, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Client %r>' % self.name


class Product(db.Model, ModelBase):
    name = db.Column(db.String(50), default=None, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Product %r>' % self.name


class Request(db.Model, ModelBase):
    title = db.Column(db.String(300), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    client = db.Column(db.String, db.ForeignKey('client.id'))
    client_priority = db.Column(db.Integer, nullable=False)
    target_date = db.Column(db.Date, default=None)
    ticket_url = db.Column(db.String(300), default=shortuuid.ShortUUID().random(length=10))
    product_area = db.Column(db.String, db.ForeignKey('product.id'))

    def __init__(self, title, description, client, client_priority, target_date, product_area):
        self.title = title
        self.description = description
        self.client = client
        self.client_priority = client_priority
        self.target_date = datetime.strptime(target_date, '%Y-%m-%d').date()
        self.product_area = product_area

    def to_json(self, feature_request):

        return {'title': feature_request.title,
                'description': feature_request.description,
                'client_name': Client.find_by(id=feature_request.client).name,
                'client_priority': feature_request.client_priority,
                'target_date': feature_request.target_date,
                'product_area': Product.find_by(id=feature_request.product_area).name
                }

    @staticmethod
    def update_request(feature_request, update_feature_request):
        # FixMe create function which will remove duplication
        if update_feature_request.get('title'):
            feature_request.title = update_feature_request['title']

        if update_feature_request.get('description'):
            feature_request.description = update_feature_request['description']

        if update_feature_request.get('client_id'):
            feature_request.client_id = update_feature_request['client_id']

        if update_feature_request.get('client_priority'):
            feature_request.client_priority = update_feature_request['client_priority']

        if update_feature_request.get('client_id'):
            feature_request.client_id = update_feature_request['client_id']

        if update_feature_request.get('target_date'):
            feature_request.target_date = datetime.strptime(update_feature_request['target_date'], '%Y-%m-%d').date()

        if update_feature_request.get('product_id'):
            feature_request.target_date = update_feature_request['product_id']

        return feature_request

    def __repr__(self):
        return "<Request(title='%s', description='%s', client='%s', " \
               "client_priority='%s', target_date='%s', ticket_url='%s', product_area='%s')>" % (
                self.title, self.description, self.client,
                self.client_priority, self.target_date, self.ticket_url, self.product_area
        )


