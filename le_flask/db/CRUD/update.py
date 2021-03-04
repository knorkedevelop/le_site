from le_flask.db.models import *


def update_card(card, name, image, url):
    if name:
        card.name = name
    if image:
        card.image = image
    if url:
        card.url = url
    db.session.commit()


def update_user(user, name, image, password):
    if name:
        user.name = name
    if image:
        user.image = image
    if password:
        user.password = password
    db.session.commit()


def swap_card_id(card1, card2):
    card1_id = card1.id
    card2_id = card2.id

    card1.id = 10000
    db.session.commit()
    card2.id = card1_id
    card1.id = card2_id
    db.session.commit()
