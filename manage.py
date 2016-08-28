from feature_request import init_app, run_app
from flask_script import Manager, Command

app = init_app()
manager = Manager(app)


class RunServer(Command):

    def __init__(self, app):
        self.app = app

    def run(self):
        run_app(self.app)


manager.add_command('runserver', RunServer(app))

if __name__ == "__main__":
    manager.run()