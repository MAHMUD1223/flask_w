#created on 9/2/2023 at 6p.m
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
# @app.route('/home')
def index():
    return render_template('index.html') #"Mahmud"



'''@app.route('/about/<username>')
def about(username):
    return f'<h1>This page is about {username}</h1>'''
