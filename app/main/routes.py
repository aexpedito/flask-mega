from app.main import bp
from app.models import TbUser, Post
from app.main.forms import EditProfileForm, PostComment
from app import db
from flask_login import current_user, login_required
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, current_app
from app.main.forms import EmptyForm


@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    form = PostComment()
    # TODO show all posts from current user and followed users

    return render_template('main/index.html', title='Hommme', user=current_user, form=form)


@bp.route('/user/<username>', methods=['GET'])
@login_required
def user(username):
    user = TbUser.query.filter_by(user_name=username).first_or_404()
    # TODO get current user posts only
    posts = [
        {'author': username, 'body': 'Post 1'},
        {'author': username, 'body': 'Post 2'}
    ]

    return render_template('main/user.html', user=user, posts=posts)


@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.user_name)
    if form.validate_on_submit():
        current_user.user_name = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved...')
    elif request.method == 'GET':
        form.username.data = current_user.user_name
        form.about_me.data = current_user.about_me
    return render_template('main/edit_profile.html', title='Edit Profile', form=form)

@bp.route('/index', methods=['POST'])
@login_required
def submit_post():
    form = PostComment()

    if form.validate_on_submit():
        post = Post()
        post.set_body(form.comment.data)
        post.set_user_email(current_user.user_email)
        db.session.add(post)
        db.session.commit()
    
    return render_template('main/index.html', title='Hommme', user=current_user, form=form)


@bp.route('/follow/<user_email>', methods=['POST'])
@login_required
def follow(user_email):
    form = EmptyForm()

    if form.validate_on_submit():
        user = User.query.filter_by(user_email=user_email).first()
        if user is None:
            flash('User {} not found'.format(user_email))
            return redirect(url_for('main.index'))
        if user == current_user:
            flash('you cant follow yourself')
            return redirect(url_for('main.user'))
        current_user.follow(user)
        db.session.commit()
        return redirect(url_for('main.user',user=current_user))
    else:
        return redirect(url_for('main.index'))
        
