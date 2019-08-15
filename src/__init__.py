from flask import Flask, Response, make_response, \
 redirect, render_template,abort, request
from datetime import datetime
from src.testdata.cars import cars
from collections import namedtuple
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)


@app.route('/index')
@app.route('/home')
@app.route('/')
def index():
    return "Welcome to Programming in Flask"


@app.route("/greeting/<name>")
def greeting(name: str):

    response = make_response(
        f"<h3>Welcome to coding with Flask, {name.capitalize()}")
    return response


@app.route('/error')
def create_error():
    resp = make_response("This is an error page!!", 404)
    return resp


#Creating a cookie
@app.route('/testcookie')
def return_message():
    response = make_response(
        "<h3>I am going to set the cookie for the session</h3>", 200)
    response.set_cookie("poll_interval", "42")
    return response


#Creating a redirect
@app.route('/youtube')
def gotoyoutube():
    return redirect("http://youtube.com")


def getCurrentTime():
    result = datetime.now().strftime("%I:%M:%S %p")
    return (result)


@app.route('/testtemplate/<name>')
def testname(name: str):
    data = cars()
    for x in data:
        print(x["name"])
    mytuple = namedtuple("data",
                         (["username", "mydatetime", "getmytime", "cars"]))
    currentTime = datetime.now().strftime("%I:%M:%S %p %m/%d/%Y")
    arg = mytuple(username=name,
                  mydatetime=currentTime,
                  getmytime=getCurrentTime,
                  cars=data)
    return render_template("greeting.html", arg=arg)


@app.route('/user/<name>')
def displayuserpage(name: str):
    return render_template("user.html", name=name)


@app.route('/generror/<error>')
def simulate_error(error):
    error = int(error,10)
    abort(error)


@app.route('/testpage/<name>')
def testpage(name:str):
    return render_template("testpage.html",name=name)


@app.route('/data/<name>')
def datapage(name:str):
    print("You just called the datapage!!")
    d1 = namedtuple("data",["name","version"])
    arg = d1(name=name,version=request.args.get("version"))
    return render_template("datapage.html",arg=arg)
    




# error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
