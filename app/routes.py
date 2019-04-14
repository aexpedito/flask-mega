from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Homme', user=user)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign in', form=form)
