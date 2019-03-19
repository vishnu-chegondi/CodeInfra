import os, click

from flask import Flask
from .db import migrate, cook_session
from .auth import adduser


def create_app(config_file=None):
    '''
    This creates a flask app
    '''
    app = Flask(__name__, instance_relative_config=True)
    if config_file is None:
        configFile = os.path.join(app.instance_path, "config.py")
        app.config.from_pyfile(configFile, silent=True)
    elif os.path.isfile(config_file):
        app.config.from_pyfile(config_file, silent=True)

    app.cli.add_command(migrate)
    app.cli.add_command(adduser)

    from . import auth, template
    app.register_blueprint(auth.authbp)
    app.register_blueprint(template.tempbp)

    return app
