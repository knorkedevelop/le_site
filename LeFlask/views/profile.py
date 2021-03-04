from flask import Blueprint, request, session
from LeFlask.db.models import Card
from LeFlask.db.CRUD import read, update, create, delete
from werkzeug.security import generate_password_hash
from LeFlask.utils import security, validate
from LeFlask.utils.messages import Error, Success

bp = Blueprint("profile", __name__, url_prefix="/profile")


@bp.route('/get_profile', methods=['GET'])
@security.requires_auth
def get_profile():
    try:
        user = read.get_user(session["user_id"])
        return Success("SUCCESS").asdict() | {"user": user.repr()}
    except Error as myError:
        return myError.asdict()


@bp.route('/logout', methods=['GET'])
@security.requires_auth
def logout():
    try:
        session.clear()
    except Error as myError:
        return myError.asdict()


@bp.route('/update_profile', methods=['GET'])
@security.requires_auth
def update_profile():
    try:
        user_id = int(request.args.get("id"))
        name = request.args.get("name")
        image = request.args.get("image")
        password = request.args.get("password")
        user = None
        if user_id != -1:
            user = read.get_user(user_id)
        else:
            user = read.get_user(session["user_id"])

        if password:
            password = generate_password_hash(password)
        update.update_user(user, name, image,  password)
        return Success("SUCCESS").asdict()
    except Error as myError:
        return myError.asdict()
