import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'oracle://SANDBOX:pirad2@127.0.0.1:1521/XE'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



