from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ahmad'}
    posts = [
        {
            'author': {'username': 'Ali'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Aous'},
            'body': 'The avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)