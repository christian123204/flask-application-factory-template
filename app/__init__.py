from flask import Flask
from config import config

from .extensions import db, mail, migrate
from .routes.main import main

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main)

    return app