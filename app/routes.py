from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    # return "hello, world!"
    user = {'username': 'Felix_Yanghui'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Too cold today in Dallas!'
        },
        {
            'author': {'username': 'Tony'},
            'body': 'SKO will be hold tomorrow in Olando!'

        }
    ]
    return render_template('index.html', user=user, posts=posts)