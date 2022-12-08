from . import bp as app
from app import db
# from .models import Post
from flask import render_template, request, redirect, url_for

@app.route('/blog')
def blog():
    return render_template('blog.html')