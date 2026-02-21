from flask import Flask
from app.config import Config
from app.database import engine, Base
from app.routes.user_routes import user_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    Base.metadata.create_all(bind=engine)

    app.register_blueprint(user_bp)

    return app
