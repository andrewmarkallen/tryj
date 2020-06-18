import os

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS
from project.controller import Controller

# instantiate the extensions
toolbar = DebugToolbarExtension()


class MyFlask(Flask):
    def __init__(self, __name__):
        super().__init__(__name__)
        self.controller = Controller()


def create_app(script_info=None):

    # instantiate the app
    app = MyFlask(__name__)

    # enable CORS
    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    toolbar.init_app(app)

    # register blueprints
    from project.routes import routes_blueprint
    app.register_blueprint(routes_blueprint)

    # shell context for flask cli
    app.shell_context_processor({'app': app})
    return app
