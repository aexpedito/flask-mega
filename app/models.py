from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker


class TbUser(UserMixin, db.Model):
    user_id = db.Column(db.Integer)
    user_name = db.Column(db.String(255))
    user_email = db.Column(db.String(255), primary_key=True)
    user_password = db.Column(db.String(255))

    def set_password(self, password):
        self.user_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.user_password, password)

    def set_userid(self):
        max_user = db.session.query(func.max(TbUser.user_id))
        max_user_value = max_user.scalar()
        self.user_id = int(max_user_value) + 1

    def __repr__(self):
        return '<TbUser {}>'.format(self.user_name)

    def get_id(self):
        return self.user_email


#Because Flask-Login knows nothing about databases, it needs the application's help in loading a user. For that reason, the extension expects that the application will configure a user loader function, that can be called to load a user given the ID
@login.user_loader
def load_user(user_email):
    return TbUser.query.get(str(user_email))
