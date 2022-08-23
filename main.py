from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/<pagename>")
def get_post(pagename):
    return render_template(pagename)


if __name__ == "__main__":
    app.run(debug=True)