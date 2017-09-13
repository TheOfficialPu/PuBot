"""initializes the application
"""
from flask import Flask, render_template

from flaskserver.blueprints.public.controller import public
def create_app(config="test_config"):
    """factory function for the app
    """
    app = Flask(__name__)
    app.config.from_object(config)
    _register_blueprints(app)
    return app

def _register_blueprints(app):
    """register blueprints here
    """
    app.register_blueprint(public)


def _register_errorhandlers(app):
    """register the error handlers
    """
    def render_error(error):
        """If a HTTPException, pull the `code` attribute; default to 500
        """
        error_code = getattr(error, 'code', 500)
        return render_template("{0}.html".format(error_code)), error_code

    for errcode in [404, 500]:
        app.errorhandler(errcode)(render_error)
