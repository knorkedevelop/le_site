from ..models import *


def card_for(name, url, image, user):
    new_card = Card(name, url, image, user)
    db.session.add(new_card)
    db.session.commit()


def user(name, password):
    new_user = User(name, password)
    db.session.add(new_user)
    db.session.commit()
