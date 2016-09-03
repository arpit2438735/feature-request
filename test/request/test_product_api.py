import unittest
import json

from test.feature_request_utils import FeatureRequestUtils
from test.integration_test_base import IntegrationTestBase


class Product(IntegrationTestBase, unittest.TestCase):

    def test_get_product_list(self):
        FeatureRequestUtils.create_request()
        response = self.app.get('/api/product/')

        response_data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_data["products"]), 2)