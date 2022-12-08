from . import bp as app
from flask import render_template, request, redirect, url_for
from .models import Post, Car
from app import db

# Home Section
@app.route('/')
def home():
    all_posts = Post.query.all()
    all_cars = Car.query.all()
    return render_template('home.html', post=all_posts, cars=all_cars)

# Post Section
@app.route('/main/<id>')
def single_post(id):
    post = Post.query.get(int(id))
    return render_template('single_post.html', post=post)

@app.route('/create-post', methods=["POST"])
def create_post():
    title = request.form['inputTitle']
    body = request.form['inputBody']
    new_post = Post(title=title, body=body, user_id=1)
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for('main.home'))

#Car_Data
# @app.route('/')
# def car_data():
#     all_cars = Car.query.all()
#     return render_template('home.html', cars=all_cars)

# About Section
@app.route('/about')
def about():
    return render_template('about.html')

