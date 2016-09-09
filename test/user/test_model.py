import unittest
from feature_request.auth.model import User
from test.unit_test_base import UnitTestBase


class TestUser(UnitTestBase, unittest.TestCase):
    def test_user_model(self):
        user = User('arpit@gmail.com', '1234567')
        user.create(user)

        self.assertEqual(user.email, 'arpit@gmail.com')
        self.assertNotEqual(user.password, '1234567')
        self.assertIsNotNone(user.id)