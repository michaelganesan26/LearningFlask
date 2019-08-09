from flask import Flask, Response, make_response,redirect

app = Flask(__name__)


@app.route('/index')
@app.route('/home')
@app.route('/')
def index():
   return "Welcome to Programming in Flask"

@app.route("/greeting/<name>")
def greeting(name:str):
    
    response = make_response(f"<h3>Welcome to coding with Flask, {name.capitalize()}")
    return response

@app.route('/error')
def create_error():
   resp = make_response("This is an error page!!",404)
   return resp

#Creating a cookie
@app.route('/data')
def return_message():
   response = make_response("<h3>I am going to set the cookie for the session</h3>",200)
   response.set_cookie("poll_interval","42")
   return response

#Creating a redirect
@app.route('/youtube')
def gotoyoutube():
   return redirect("http://youtube.com")

