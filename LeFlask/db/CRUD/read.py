from LeFlask.db.models import *


def get_card(id):
    return Card.query.filter_by(id=id).first()


def get_user(id):
    return User.query.filter_by(id=id).first()


def get_all_users():
    return User.query.order_by(User.id).all()


def get_all_cards():
    return Card.query.order_by(Card.id).all()


def get_all_cards_for(current_user):
    return Card.query.filter_by(user=current_user).order_by(Card.id).all()
