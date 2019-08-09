from flask import Flask, Response, make_response

app = Flask(__name__)


@app.route('/index')
@app.route('/home')
@app.route('/')
def index():
   return "Welcome to Programming in Flask"



