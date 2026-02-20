from flask import Flask, render_template
from .config import Config


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(Config)

    from .routes.user import user_bp

    app.register_blueprint(user_bp)

    @app.route("/")
    def home():
        return render_template("index.html")

    return app
