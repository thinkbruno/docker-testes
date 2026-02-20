from flask import Flask

# import routers
from .config import Server
from .repositories.base_repository import mysql_db
from .routers.user_router import user_route

app = Flask(__name__)

app.config["DEBUG"] = True
app.config["DATABASE"] = mysql_db


@app.before_request
def _db_connect():
    mysql_db.connect()


@app.teardown_request
def _db_close(exc):
    if not mysql_db.is_closed():
        mysql_db.close()


# register client routers
app.register_blueprint(user_route)
