from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! Nicole is learning Python and this is her first web page."
   
