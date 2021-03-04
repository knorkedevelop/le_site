from flask import Blueprint, request, session
from LeFlask.db.models import Card
from LeFlask.db.CRUD import read, update, create, delete
from werkzeug.security import generate_password_hash
from LeFlask.utils import security, validate
from LeFlask.utils.messages import Error, Success

bp = Blueprint("admin", __name__, url_prefix="/admin")


@bp.route('/create_user', methods=['GET'])
@security.requires_auth
def create_user():
    try:
        attr = validate.attr(request, {"name", "password"})
        create.user(attr["name"], generate_password_hash(attr["password"]))
        return Success("SUCCESS").asdict()
    except Error as myError:
        return myError.asdict()


@bp.route('/get_users', methods=['GET'])
@security.requires_auth
def get_users():
    try:
        users = read.get_all_users()
        user_repr = []
        for current_user in users:
            user_repr.append(current_user.repr())
        return Success("SUCCESS").asdict() | {"users": user_repr}
    except Error as myError:
        return myError.asdict()


@bp.route('/delete_user', methods=['GET'])
@security.requires_auth
def delete_user():
    try:
        attr = validate.attr(request, {"id"})
        current_user = read.get_user(attr["id"])
        cards_for_user = read.get_all_cards_for(current_user)
        delete.delete_cards(cards_for_user)
        delete.delete_user(current_user)
        return Success("SUCCESS").asdict()
    except Error as myError:
        return myError.asdict()
