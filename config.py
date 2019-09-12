import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'oracle://SANDBOX:pirad3@127.0.0.1:1521/XE'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT=False



