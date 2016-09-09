import yaml
import os

current_dir = os.path.dirname(os.path.realpath(__file__))


def configure(app=None, environment=None):

    default_config = current_dir + '/default.yaml'
    test_config = current_dir + '/testing.yaml'
    prodcution_config = current_dir + '/prod.yaml'

    if os.path.isfile(default_config): # Load the base default config (default.yaml)
        with open(default_config, 'r') as default_file:
            default_settings = yaml.load(default_file)
            app.config.update(**default_settings)

    if environment == 'testing':
        with open(test_config, 'r') as test_config:
            test_settings = yaml.load(test_config)
            app.config.update(**test_settings)
    elif environment == 'production':
        with open(prodcution_config, 'r') as test_config:
            test_settings = yaml.load(test_config)
            app.config.update(**test_settings)

    if environment != 'testing':
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(
            DB_USER=app.config['DB_USER'],
            DB_PASS=app.config['DB_PASS'],
            DB_ADDR=app.config['DB_ADDR'],
            DB_NAME=app.config['DB_NAME']
        )

    return app