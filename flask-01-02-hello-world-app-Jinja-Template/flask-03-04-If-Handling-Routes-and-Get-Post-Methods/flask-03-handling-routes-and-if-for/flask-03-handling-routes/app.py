# Import Flask modules
from flask import Flask, render_template, redirect, url_for

# Create an object named app
app = Flask(__name__)

# Create a function named home which returns a string 'This is home page for no path, <h1> Welcome Home</h1>' 
# and assign route of no path ('/')
@app.route('/')
def home():
    return 'This is home page for no path, <h1> Welcome Home</h1>'

# Create a function named about which returns a formatted string '<h1>This is my about page </h1>' 
# and assign to the static route of ('about')
@app.route('/about')
def about():
    return '<h1>This is my about page </h1>'

# Create a function named error which returns a formatted string '<h1>Either you encountered an error or you are not authorized.</h1>' 
# and assign to the static route of ('error')
@app.route('/error')
def error():
    return '<h1>Either you encountered an error or you are not authorized.</h1>'