from feature_request import init_app, db


class UnitTestBase:

    def setUp(self):
        self.app = init_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()