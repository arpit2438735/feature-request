import unittest
from feature_request import init_app, db


class IntegrationTestBase(unittest.TestCase):

    def setUp(self):
        app = init_app('testing')
        app.test_mode = True
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()