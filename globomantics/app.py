from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "home"

# 127.0.0.1:5000
