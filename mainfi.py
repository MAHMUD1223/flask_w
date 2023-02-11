#created on 9/2/2023 at 6p.m
from flask import Flask, render_template
app = Flask(__name__)
'''
#sqllight db
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)


class user(db.Model):
    name = db.Column(db.String(length=20), nullable=False, unique=True)
'''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ad')
def adam():
    return render_template('adam.html')

@app.route('/admin/<alpha>')
def user(alpha):
    if alpha=='12345':
        return 'welcome'
    else:
        return f"hell{alpha}"

#@app.route('/about/<username>')
#def about(username):
#    return f'<h1>This page is about {username}</h1>

# app.run()
