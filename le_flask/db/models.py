from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    password = db.Column(db.String())
    image = db.Column(db.String())
    card = db.relationship(
        "Card", back_populates="user")

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def repr(self):
        return {"id": self.id, "name": self.name, "image": self.image}


class Card(db.Model):
    __tablename__ = 'card'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    url = db.Column(db.String())
    image = db.Column(db.String())
    user = db.relationship(
        "User", uselist=False, back_populates="card")
    # foreignkeys
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'), nullable=False)

    def __init__(self, name, url, image, user):
        self.name = name
        self.url = url
        self.image = image
        self.user = user

    def repr(self):
        return {"id": self.id, "name": self.name, "url": self.url, "image": self.image}
