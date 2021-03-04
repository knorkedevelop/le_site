from flask import Flask, render_template, request, send_from_directory
from flask_cors import CORS
from flask_migrate import Migrate
from le_flask.db.CRUD import create
from le_flask.db.models import db
from le_flask.views import dashboard, profile, admin
from le_flask.utils.security import *
from werkzeug.security import generate_password_hash, check_password_hash


def create_app(test_config=None):
    server = Flask(__name__)
    CORS(server)
    server.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://tim:secret@le_postgres:5432/le_db"
    server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(server)
    migrate = Migrate(server, db)
    server.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev"
    )

    # with server.app_context():
    #     create.user("tim", generate_password_hash("Test"))

    if test_config is None:
        # load the instance config, if it exists, when not testing
        server.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        server.config.from_mapping(test_config)

    server.register_blueprint(dashboard.bp)
    server.register_blueprint(profile.bp)
    server.register_blueprint(admin.bp)
    return server


server = create_app()


@ server.route('/', methods=['GET'])
@ requires_auth
def main():
    return render_template("index.html")
