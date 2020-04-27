from flask import Flask, jsonify
import sys
import scraper
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



scraper.scrapeCovid()
@app.route('/corona-data')
def starting():
    with open('CoronaNepal.json',mode="r", encoding='utf-8') as ff:
        coronaData = json.load(ff)
    return jsonify(coronaData)