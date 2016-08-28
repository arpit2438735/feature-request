import unittest
from feature_request import init_app, db
from feature_request.request.model import Product, Client


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.app = init_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_product_model(self):
        product = Product('Billing')
        product.create(product)

        self.assertTrue(product.id)
        self.assertTrue(product.created_at)
        self.assertTrue(product == Product.find_by(name='Billing'))


class TestClient(unittest.TestCase):
    def setUp(self):
        self.app = init_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_product_model(self):
        client = Client('Client_A')
        client.create(client)

        self.assertTrue(client.id)
        self.assertTrue(client.created_at)
        self.assertTrue(client == Client.find_by(name='Client_A'))