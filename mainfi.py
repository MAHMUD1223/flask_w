#created on 9/2/2023 at 6p.m
from flask import Flask, render_template
app = Flask(__name__)

#sqllight db
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=20), unique=True)
    pasd = db.Column(db.String(length=4))

    def __repr__(self):
        return f'User {self.name}'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin/<alpha>')
def user(alpha):
    if alpha=='12345':
        user = User.query.all()
        return render_template('adam.html', user=user)
    else:
        return f"ah ah a you didn't say the magic word insted said {alpha}"

#@app.route('/about/<username>')
#def about(username):
#    return f'<h1>This page is about {username}</h1>

# app.run()
