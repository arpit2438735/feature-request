from feature_request.models import ModelBase, db
import shortuuid


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
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    client = db.Column(db.Integer, db.ForeignKey('client.id'))
    client_priority = db.Column(db.Integer, nullable=False)
    target_date = db.Column(db.DateTime, default=None)
    ticket_url = db.Column(db.String(300), default=shortuuid.ShortUUID().random(length=10))
    product_area = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __init__(self, title, description, client, client_priority, target_date, product_area):
        self.title = title
        self.description = description
        self.client = client
        self.client_priority = client_priority
        self.target_date = target_date
        self.product_area = product_area

    def __repr__(self):
        return "<Request(title='%s', description='%s', client='%s', " \
               "client_priority='%s', target_date='%s', ticket_url='%s', product_area='%s')>" % (
                self.title, self.description, self.client,
                self.client_priority, self.target_date, self.ticket_url, self.product_area
        )

