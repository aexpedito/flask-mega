from flask import Blueprint

bp = Blueprint('errors', __name__)
#After the blueprint object is created, I import the handlers.py module
from app.errors import handlers
