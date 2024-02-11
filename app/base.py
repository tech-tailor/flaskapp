# flask app 
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    """
    view for homepage
    """
    return "Welcome to my Home page"

@app.route('/<my_name>')
def greet(my_name):
    """
    view to greet user"""

    return render_template("base.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)