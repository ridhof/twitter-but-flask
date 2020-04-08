import random

from app import DB as db
from app.mod_auth.models import Base, User

class Tweet(Base):

    __tablename__ = 'tweets'

    text = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    liked = db.Column(db.Integer, nullable=False)
    retweet = db.Column(db.Integer, nullable=False)

    def __init__(self, text, user=None, username=None):
        self.text = text
        if username is not None:
            user = User.query.filter_by(name=username).first()
            self.user_id = user.id
        else:
            self.user_id = user.id
        self.liked = random.randint(0, 10)
        self.retweet = random.randint(0, 10)

    def __repr__(self):
        return '<Tweet %r>' % (self.text)

    def get_username(self):
        user = User.query.filter_by(id=self.user_id).first()
        return user.name