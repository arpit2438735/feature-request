import yaml
import os

current_dir = os.path.dirname(os.path.realpath(__file__))


def configure(app=None, environment=None):

    default_config = current_dir + '/default.yaml'
    test_config = current_dir + '/testing.yaml'

    if os.path.isfile(default_config): # Load the base default config (default.yaml)
        with open(default_config, 'r') as default_file:
            default_settings = yaml.load(default_file)
            app.config.update(**default_settings)

    if environment == 'testing':
        with open(test_config, 'r') as test_config:
            test_settings = yaml.load(test_config)
            app.config.update(**test_settings)

    return app