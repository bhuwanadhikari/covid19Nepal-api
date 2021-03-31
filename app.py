from flask import Flask, jsonify
import sys
import scraper
import json
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

app = Flask(__name__)
CORS(app)

# run scraping code regularly
scraper.scrapeCovid()



print("inside the scarping phase")
print('laoding')
pageLink = "https://kathmandupost.com/covid19"


# pageResponse = requests.get(pageLink, timeout=50)
pageResponse = requests.get(pageLink)
soup = BeautifulSoup(pageResponse.content, "html.parser")
print('page content here')


json_string = re.findall("kathmandu.*?kathmandu", soup)
print (json_string)

print('finished')


# pattern = re.compile(r"window.Rent.data\s+=\s+(\{.*?\});\n")
# script = soup.find("script", text=pattern)

# data = pattern.search(script.text).group(1)
# data = json.loads(data)
# print(data)



@app.route("/corona-data")
def districtsApi():
    with open("CoronaNepal.json", mode="r", encoding="utf-8") as ff:
        coronaData = json.load(ff)
    return jsonify(coronaData)


@app.route("/corona-data-test")
def districtsApiTest():


   

    return jsonify({"test": "fuck asdf "})


@app.route("/")
def home():
    return jsonify({"msg": "working"})



if __name__ == "__main__":
    app.run(debug=True)
