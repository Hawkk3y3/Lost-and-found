from datetime import datetime

from run import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(50))
    email = db.Column('email', db.String(100))
    password = db.Column('password', db.String(100))
    verified = db.Column('verified', db.Boolean)
    date_created = db.Column('date_created', db.DateTime, default=datetime.now)

    def __init__(self, username, email, password, verified=False):
        self.username = username
        self.email = email
        self.password = password
        self.verified = verified

    @property
    def serialize(self):
        return {'id': self.id, 'username': self.username, 'email': self.email, 'password': self.password,
                'verified': self.verified, 'date_created': self.date_created}

    @staticmethod
    def confirm_email(database, email):
        result_user = database.session.query(User).filter(User.email == email).one()
        result_user.verified = True
