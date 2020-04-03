from werkzeug.security import generate_password_hash, check_password_hash
from app import DB as db


class Base(db.Model):
    """
    Base class as foundation/template to other class.
    """
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_delete = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime,
                             default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


class User(Base):
    """
    User class.
    """

    __tablename__ = 'users'

    name = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(192), nullable=False)

    # New instance instantiation procedure
    def __init__(self, name, password):

        self.name = name
        self.password = generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % (self.name)

    def check_password(self, password):
        return check_password_hash(self.password, password)
