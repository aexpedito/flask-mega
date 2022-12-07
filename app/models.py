from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from sqlalchemy import func
from hashlib import md5
from datetime import datetime
from sqlalchemy.schema import Sequence, CreateSequence

followers = db.Table('followers',
    db.Column('follower_email', db.String, db.ForeignKey('tb_user.user_email')),
    db.Column('followed_email', db.String, db.ForeignKey('tb_user.user_email'))
)

class TbUser(UserMixin, db.Model):
    user_seq_id = Sequence('user_seq_id')
    user_id = db.Column(db.Integer, user_seq_id, server_default=user_seq_id.next_value())
    user_name = db.Column(db.String(255))
    user_email = db.Column(db.String(255), primary_key=True)
    user_password = db.Column(db.String(255))
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy='dynamic')


    def set_password(self, password):
        self.user_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.user_password, password)

    def set_userid(self):
        pass

    def __repr__(self):
        return '<TbUser {}>'.format(self.user_name)

    def get_id(self):
        return self.user_email

    def avatar(self, size):
        digest = md5(self.user_email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(followers.c.followed_email == user.user_email).count() > 0

    followed = db.relationship(
        'TbUser', secondary=followers,
        primaryjoin=(followers.c.follower_email == user_email),
        secondaryjoin=(followers.c.followed_email == user_email),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    def followed_posts(self):
        Post.query.join(followers, (followers.c.followed_email == Post.user_email)).filter(followers.c.follower_email == self.user_email).order_by(Post.timestamp.desc())
        
        own = Post.query.filter_by(user_email=self.user_email)
        
        return followed.union(own).order_by(Post.timestamp.desc())

class Post(db.Model):
    post_seq_id = Sequence('post_seq_id')
    id = db.Column(db.Integer, post_seq_id, server_default=post_seq_id.next_value(), primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_email = db.Column(db.String(140), db.ForeignKey('tb_user.user_email'))

    def set_body(self, comment):
        self.body = comment

    def set_user_email(self, user_email):
        self.user_email = user_email
    
    def __repr__(self):
        return '<Post {}>'.format(self.body)

#Because Flask-Login knows nothing about databases, it needs the application's help in loading a user. For that reason, the extension expects that the application will configure a user loader function, that can be called to load a user given the ID
@login.user_loader
def load_user(user_email):
    return TbUser.query.get(str(user_email))
