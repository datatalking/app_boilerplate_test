# app.py
# SOURCE https://realpython.com/web-development-with-flask-fetching-data-with-requests/ ?


from flask import Flask, render_template, jsonify
from stock_scraper import get_data

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/data")
def data():
	return jsonify(get_data())
