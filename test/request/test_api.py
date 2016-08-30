import unittest
import datetime
import json

from test.integration_test_base import IntegrationTestBase
from feature_request.request.model import Request, Client, Product
from test.feature_request_utils import FeatureRequestUtils

class TestRequestAPI(IntegrationTestBase, unittest.TestCase):

    def test_get_response(self):
        expected_data = {
            "feature_requests": [
                {
                    "client_name": "Client_A",
                    "client_priority": 1,
                    "description": "this is test",
                    "product_area": "Billing",
                    "target_date": "Tue, 30 Aug 2016 15:49:56 GMT",
                    "title": "test"
                }
            ]
        }
        product = Product('Billing')
        product.create(product)

        client = Client('Client_A')
        client.create(client)

        request = Request(title='test', description='this is test', client=client.id,
                          client_priority=1, target_date=datetime.datetime.now(), product_area=product.id)

        request.create(request)
        response = self.app.get('/api/feature-request/')

        self.assertTrue(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertEqual(len(response_data['feature_requests']), 1)
        self.assertEqual(response_data['feature_requests'][0]['client_name'], expected_data['feature_requests'][0]['client_name'])

    def test_bulk_get_response(self):
        expected_data = {
            "feature_requests": [
                {
                    "client_name": "ClientA",
                    "client_priority": 1,
                    "description": "Client want to have oauth base login",
                    "product_area": "Policies",
                    "target_date": "Tue, 30 Aug 2016 16:09:07 GMT",
                    "title": "Add Login Page"
                },
                {
                    "client_name": "ClientB",
                    "client_priority": 2,
                    "description": "Client want to have bootstrap framework in user module",
                    "product_area": "Billing",
                    "target_date": "Tue, 30 Aug 2016 16:09:07 GMT",
                    "title": "Add Bootstrap in User Module"
                }
            ]
        }

        FeatureRequestUtils.create_request()
        response = self.app.get('/api/feature-request/')

        self.assertTrue(response.status_code, 200)

        response_data = json.loads(response.data)
        self.assertEqual(len(response_data['feature_requests']), 2)
        self.assertEqual(response_data['feature_requests'][0]['client_name'], expected_data['feature_requests'][0]['client_name'])
        self.assertEqual(response_data['feature_requests'][1]['client_name'], expected_data['feature_requests'][1]['client_name'])
        self.assertEqual(response_data['feature_requests'][0]['client_priority'], expected_data['feature_requests'][0]['client_priority'])
        self.assertEqual(response_data['feature_requests'][1]['client_priority'], expected_data['feature_requests'][1]['client_priority'])
        self.assertEqual(response_data['feature_requests'][0]['product_area'], expected_data['feature_requests'][0]['product_area'])
        self.assertEqual(response_data['feature_requests'][1]['product_area'], expected_data['feature_requests'][1]['product_area'])