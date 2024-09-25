"""{{ cookiecutter.project_name }}."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
#

from aaron_common_libs.logger.custom_logger import CustomLogger
from flask import Flask
from flask_session import Session
from werkzeug.middleware.proxy_fix import ProxyFix

from {{ cookiecutter.project_slug }}.config import Config
from {{ cookiecutter.project_slug }}.home.views import home

config = Config()


def create_app():
    """Create Application.

    Returns:
        Flask app
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config["APP_DICT"] = config.app_dict
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

    with app.app_context():
        app.register_blueprint(home)

    logging_handler = CustomLogger(log_dict=config.log_dict)
    app.logger = logging_handler.default

    return app
