from flask import Flask

from talana_kombat.config import get_config


def create_app(config_name):
    """Application factory used in flask apps,
    if we had more services this is the place to
    plug them into our app"""

    app = Flask("talana-kombat")
    app.config.from_object(get_config(config_name))

    from talana_kombat.api import api_bp
    app.register_blueprint(api_bp)

    return app
