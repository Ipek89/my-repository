#Import Flask module.

# Create an object named `app` from imported Flask module.

# Create a function `hello` which returns a string `Hello World`.

# Assign a URL route the `hello` function with decorator `@app.route('/')`.

# Create a function `second` which returns a string `This is the second page` and assign a URL route the `second` function with decorator `@app.route('/second')`. 

# Create a function `third` which returns a string `This is the subpage of third page` and assign a URL route the `third` function with decorator `@app.route('/third/subthird')`. 

# Create a dynamic url which takes id number dynamically and return with a massage which show id of page.

#run the application in debug mode

from flask import Flask
app = Flask(__name__)
def hello():
    return "<h1>Hello World</h1>"

@app.route('/')
def hello():
    return "h1>Hello World</h1>"

if __name__ == '__main__':
    app.run(debug=False)
