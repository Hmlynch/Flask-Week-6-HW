from . import bp as app
from flask import render_template, request, redirect, url_for, flash
from .models import Post, Car
from app import db
from flask_login import current_user, login_required

# Home Section
@app.route('/')
def home():
    all_posts = Post.query.all()
    all_cars = Car.query.all()
    return render_template('home.html', post=all_posts, cars=all_cars, user=current_user)

# Post Section
@app.route('/main/<id>')
@login_required
def single_post(id):
    post = Post.query.get(int(id))
    return render_template('single_post.html', post=post)

@app.route('/create-post', methods=["POST"])
@login_required
def create_post():
    title = request.form['inputTitle']
    body = request.form['inputBody']
    new_post = Post(title=title, body=body, user_id=1)
    db.session.add(new_post)
    db.session.commit()
    flash('You have successfully created a post!', 'success')
    return redirect(url_for('main.home'))

# About Section
@app.route('/about')
def about():
    return render_template('about.html')

