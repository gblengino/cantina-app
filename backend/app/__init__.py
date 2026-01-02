from flask import Flask
from app.exensions import db, ma

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)
    ma.init_app(app)

    return app