from flask_script import Manager, Command
from flask_migrate import MigrateCommand, Migrate

from feature_request import init_app, run_app
from feature_request.models import db
from feature_request.setup_data import SetupData

app = init_app()
migrate = Migrate(app, db)
manager = Manager(app)


class RunServer(Command):

    def __init__(self, app):
        self.app = app

    def run(self):
        run_app(self.app)


class InitData(Command):

    def __init__(self):
        pass

    @staticmethod
    def run():
        SetupData()

manager.add_command('runserver', RunServer(app))
manager.add_command('db', MigrateCommand)
manager.add_command('add', InitData())

if __name__ == "__main__":
    manager.run()