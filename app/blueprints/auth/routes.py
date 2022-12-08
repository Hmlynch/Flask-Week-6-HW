from . import bp as app
from flask import render_template
from app import db

# Login Section
@app.route('/login')
def login():
    return render_template('login.html')

# Register Section
@app.route('/register')
def register():
    return render_template('register.html')