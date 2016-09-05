import unittest
import json

from test.integration_test_base import IntegrationTestBase
from feature_request.request.model import Request, Client, Product
from test.feature_request_utils import FeatureRequestUtils


class TestRequestAPI(IntegrationTestBase, unittest.TestCase):

    def test_get_response_for_feature_request(self):
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
                          client_priority=1, target_date='2016-12-22', product_area=product.id)

        request.create(request)
        response = self.app.get('/api/feature-request/')

        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertEqual(len(response_data['feature_requests']), 1)
        self.assertEqual(response_data['feature_requests'][0]['client_name'], expected_data['feature_requests'][0]['client_name'])

    def test_bulk_get_response_for_feature_request(self):
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

        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.data)
        self.assertEqual(len(response_data['feature_requests']), 3)
        self.assertIsNotNone(response_data['feature_requests'][0]['id'])
        self.assertEqual(response_data['feature_requests'][0]['client_name'], expected_data['feature_requests'][0]['client_name'])
        self.assertEqual(response_data['feature_requests'][1]['client_name'], expected_data['feature_requests'][1]['client_name'])
        self.assertEqual(response_data['feature_requests'][0]['client_priority'], expected_data['feature_requests'][0]['client_priority'])
        self.assertEqual(response_data['feature_requests'][1]['client_priority'], expected_data['feature_requests'][1]['client_priority'])
        self.assertEqual(response_data['feature_requests'][0]['product_area'], expected_data['feature_requests'][0]['product_area'])
        self.assertEqual(response_data['feature_requests'][1]['product_area'], expected_data['feature_requests'][1]['product_area'])

    def test_post_for_feature_request(self):
        FeatureRequestUtils.create_request()
        client = Client.find_by(name='ClientA')
        product = Product.find_by(name='Billing')

        feature_request = {
            'title': 'Automate the deployment to AWS Server',
            'description': 'As a client I can deploy the latest change to AWS Server for demo',
            "client_id": client.id,
            "client_priority": 1,
            "product_id": product.id,
            "target_date": '2017-09-20'
        }

        expected = {
            'status': 'success',
            'reason': 'Feature request added'
        }

        response = self.app.post(
            '/api/feature-request/',
            data=json.dumps(feature_request),
            content_type='application/json'
        )

        response_data = json.loads(response.data)
        del response_data['feature_request']

        self.assertEqual(response_data, expected)
        self.assertEqual(response.status_code, 201)

    def test_post_getting_saved(self):
        FeatureRequestUtils.create_request()
        client = Client.find_by(name='ClientA')
        product = Product.find_by(name='Billing')

        feature_request = {
            'title': 'Automate the deployment to AWS Server',
            'description': 'As a client I can deploy the latest change to AWS Server for demo',
            "client_id": client.id,
            "client_priority": 1,
            "product_id": product.id,
            "target_date": '2017-09-20'
        }

        response = self.app.post(
            '/api/feature-request/',
            data=json.dumps(feature_request),
            content_type='application/json'
        )

        response = self.app.get('/api/feature-request/')
        response_data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_data["feature_requests"]), 4)

    def test_put_request_for_id_not_present(self):
        FeatureRequestUtils.create_request()

        update_feature_request = {
            'title': 'Automate the deployment to Azure Server',
            'description': 'As a client I can deploy the latest change to Azure Server for demo',
            "client_priority": 2,
            "target_date": '2017-09-20'
        }

        expected = {
            'status': 'fail',
            'reason': 'Resource not found'
        }

        response = self.app.put(
            '/api/feature-request/123',
            data=json.dumps(update_feature_request),
            content_type='application/json'
        )

        response_data = json.loads(response.data)

        self.assertEqual(response_data, expected)
        self.assertEqual(response.status_code, 404)

    def test_put_request_for_id_present(self):
        FeatureRequestUtils.create_request()

        update_feature_request = {
            'title': 'Automate the deployment to Azure Server',
            'description': 'As a client I can deploy the latest change to Azure Server for demo',
            "client_priority": 2,
            "target_date": '2017-09-20'
        }

        client = Client.find_by(name='ClientA')
        feature_request = Request.find_by(client=client.id)

        expected = {
            'status': 'success',
            'reason': 'Feature request updated'
        }

        response = self.app.put(
            '/api/feature-request/' + feature_request.id,
            data=json.dumps(update_feature_request),
            content_type='application/json'
        )

        feature_request = Request.find_by(id=feature_request.id)
        response_data = json.loads(response.data)

        self.assertEqual(response_data['reason'], expected['reason'])
        self.assertEqual(feature_request.title, update_feature_request['title'])
        self.assertEqual(feature_request.description, update_feature_request['description'])
        self.assertEqual(response.status_code, 200)