import unittest
import datetime
from feature_request.request.model import Product, Client, Request
from test.unit_test_base import UnitTestBase


class TestProduct(UnitTestBase, unittest.TestCase):
    def test_product_model(self):
        product = Product('Billing')
        product.create(product)

        self.assertTrue(product.id)
        self.assertTrue(product.created_at)
        self.assertTrue(product == Product.find_by(name='Billing'))


class TestClient(UnitTestBase, unittest.TestCase):
    def test_product_model(self):
        client = Client('Client_A')
        client.create(client)

        self.assertTrue(client.id)
        self.assertTrue(client.created_at)
        self.assertTrue(client == Client.find_by(name='Client_A'))


class TestRequest(UnitTestBase, unittest.TestCase):
    def test_request_model(self):
        product = Product('Billing')
        product.create(product)

        client = Client('Client_A')
        client.create(client)

        request = Request(title='test', description='this is test', client=client.id,
                          client_priority=1, target_date=datetime.datetime.now(), product_area=product.id)
        request.create(request)

        find_all_request = Request.query.filter().all()
        self.assertTrue('test' == find_all_request[0].title)
        self.assertTrue('this is test' == find_all_request[0].description)
        self.assertTrue(client.id == find_all_request[0].client)
        self.assertTrue(product.id == find_all_request[0].product_area)
