from app import app
from flask import render_template

# Home Section
@app.route('/')
def home():
    return "Home"

# Login Section
@app.route('/login')
def login():
    return "Login"

# Register Section
@app.route('/register')
def register():
    return "Register"

# About Section
@app.route('/about')
def about():
    return "About"

# Blog Section
@app.route('/blog')
def blog():
    return "Blog"