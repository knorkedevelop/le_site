from ..models import *


def delete_card(current_card):
    db.session.delete(current_card)
    db.session.commit()


def delete_user(current_user):
    db.session.delete(current_user)
    db.session.commit()


def delete_cards(cards):
    for current_card in cards:
        db.session.delete(current_card)
    db.session.commit()
