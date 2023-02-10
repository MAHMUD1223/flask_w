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

#route
@app.route('/')
# @app.route('/home')
def index():
    return render_template('index.html') #"Mahmud"


'''@app.route('/admin/<pass>')
def admin(pass):
    if pass=='12345':
        return "welcome admin"
    else:
        return 'worng password try again'
'''

'''@app.route('/about/<username>')
def about(username):
    return f'<h1>This page is about {username}</h1>'''

#app.run()
