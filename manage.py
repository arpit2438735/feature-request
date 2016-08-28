from feature_request import init_app, run_app
from flask_script import Manager, Command
import os

app = init_app()
manager = Manager(app)


class RunServer(Command):

    def __init__(self, app):
        self.app = app

    def run(self):
        run_app(self.app)


class RunTests(Command):
    """Run the unit tests."""

    def __init__(self, coverage=False):
        self.coverage = coverage

    def run(self):
        test_coverage = None

        if self.coverage and not os.environ.get('FLASK_COVERAGE'):
            import sys
            os.environ['FLASK_COVERAGE'] = '1'
            os.execvp(sys.executable, [sys.executable] + sys.argv)

        if self.coverage and os.environ.get('FLASK_COVERAGE'):
            import coverage
            test_coverage = coverage.coverage(branch=True, include='feature_request/*')
            test_coverage.start()

        import unittest
        tests = unittest.TestLoader().discover('test')
        unittest.TextTestRunner(verbosity=2).run(tests)

        if test_coverage:
            test_coverage.stop()
            test_coverage.save()
            print('Coverage Summary:')
            test_coverage.report()
            basedir = os.path.abspath(os.path.dirname(__file__))
            covdir = os.path.join(basedir, 'tmp/coverage')
            test_coverage.html_report(directory=covdir)
            print('HTML version: file://%s/index.html' % covdir)
            test_coverage.erase()


manager.add_command('runserver', RunServer(app))
manager.add_command('test', RunTests())
manager.add_command('coverage', RunTests(coverage=True))

if __name__ == "__main__":
    manager.run()