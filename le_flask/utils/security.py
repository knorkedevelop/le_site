from functools import wraps
from flask import request, Response, session
from werkzeug.security import generate_password_hash, check_password_hash
from le_flask.db.CRUD import read


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    all_users = read.get_all_users()
    for current_user in all_users:
        if username == current_user.name and check_password_hash(current_user.password, password):
            session["user_id"] = current_user.id
            return True
    return False


def requires_auth(f):
    @ wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return Response(
                'Could not verify your access level for that URL.\n'
                'You have to login with proper credentials', 401,
                {'WWW-Authenticate': 'Basic realm="Login Required"'})
        return f(*args, **kwargs)
    return decorated
