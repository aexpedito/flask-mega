import unittest
from app import db, create_app
from app.models import TbUser, Post
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/flask_m'
    ELASTICSEARCH_URL = None


class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hash(self):
        user = TbUser(user_name='Some Name', user_email='email@email.com')
        user.set_password('somepassword')
        self.assertFalse(user.check_password('dfad'))
        self.assertTrue(user.check_password('somepassword'))


if __name__ == '__main__':
    unittest.main(warnings=None)