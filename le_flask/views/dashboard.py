from flask import Blueprint, request, session
from le_flask.db.models import Card
from le_flask.db.CRUD import read, update, create, delete
from le_flask.utils import security, validate
from le_flask.utils.messages import Error, Success

bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@bp.route('/get_cards', methods=['GET'])
@security.requires_auth
def get_cards():
    try:
        cards = read.get_all_cards_for(read.get_user(session["user_id"]))
        card_repr = []
        for current_card in cards:
            card_repr.append(current_card.repr())
        return Success("SUCCESS").asdict() | {"cards": card_repr}
    except Error as myError:
        return myError.asdict()


@bp.route('/delete_card', methods=['GET'])
@security.requires_auth
def delete_card():
    try:
        attr = validate.attr(request, {"id"})
        delete.delete_card(read.get_card(attr["id"]))
        return Success("SUCCESS").asdict()
    except Error as myError:
        return myError.asdict()


@bp.route('/create_card', methods=['GET'])
@security.requires_auth
def create_card():
    try:
        attr = validate.attr(request, {"name", "url", "image"})
        create.card_for(attr["name"], attr["url"],
                        attr["image"], read.get_user(session["user_id"]))
        return Success("SUCCESS").asdict()
    except Error as myError:
        return myError.asdict()


@bp.route('/update_card', methods=['GET'])
@security.requires_auth
def update_card():
    try:
        attr = validate.attr(request, {"id", "name", "url", "image"})
        update.update_card(read.get_card(
            attr["id"]), attr["name"], attr["image"], attr["url"])
        return Success("SUCCESS").asdict()
    except Error as myError:
        return myError.asdict()


@bp.route('/swap_cards', methods=['GET'])
@security.requires_auth
def swap_cards():
    try:
        attr = validate.attr(request, {"direction", "id"})
        cards = read.get_all_cards_for(read.get_user(session["user_id"]))
        card1_id = attr["id"]
        card1 = read.get_card(card1_id)
        card1_index = cards.index(card1)
        if attr["direction"] == "left":
            card2_index = card1_index-1
        else:
            card2_index = card1_index+1
        if not (card2_index < 0 or card2_index > len(cards)-1):
            card2 = cards[card2_index]
            update.swap_card_id(card1, card2)
            return Success("SUCCESS").asdict()
        raise Error("ERROR")
    except Error as myError:
        return myError.asdict()
