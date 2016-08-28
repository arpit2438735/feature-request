import yaml
import os

current_dir = os.path.dirname(os.path.realpath(__file__))


def configure(app=None, **settings):

    default_config = current_dir + '/default.yaml'

    if os.path.isfile(default_config): # Load the base default config (default.yaml)
        with open(default_config, 'r') as default_file:
            default_settings = yaml.load(default_file)
            app.config.update(**default_settings)

    # Update config with any runtime settings
    app.config.update(**settings)

    return app