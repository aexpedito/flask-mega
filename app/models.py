from app import db

class TbUser(db.Model):
    user_id = db.Column(db.Integer)
    user_name = db.Column(db.String(255))
    user_email = db.Column(db.String(255), primary_key=True)
    user_password = db.Column(db.String(255))

    def __repr__(self):
        return '<TbUser {}>'.format(self.user_name)

