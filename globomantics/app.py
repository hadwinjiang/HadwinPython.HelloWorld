from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")
    # return "home"

# 127.0.0.1:5000
