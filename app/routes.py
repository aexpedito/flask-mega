from flask import render_template, redirect, url_for, flash, request
from app import app
from app.forms import LoginForm
from app import db
from app.forms import RegistrationForm
from app.models import TbUser
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Homme', user=current_user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = TbUser.query.filter_by(user_name=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalide username or password...')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        #next page logic
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign in', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = TbUser(user_name=form.username.data, user_email=form.email.data)
        user.set_password(form.password.data)
        #TODO user.set_userid()
        db.session.add(user)
        db.session.commit()
        flash('You are registered now')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)
