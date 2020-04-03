from app import DB as db
from app.mod_auth.models import Base, User

class Tweet(Base):

    __tablename__ = 'tweets'

    text = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def __init__(self, text, user):
        self.text = text
        self.user_id = user.id

    def __repr__(self):
        return '<Tweet %r>' % (self.text)