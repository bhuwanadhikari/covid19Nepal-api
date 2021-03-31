from bs4 import BeautifulSoup
import requests
from flask import g
import json
import threading
from datetime import datetime



def is_ascii(s):
    try:
        s.decode('ascii')
        return True
    except UnicodeDecodeError:
        return False



def scrapeCovid():

    oldTime = datetime.now();

    threading.Timer(300.0, scrapeCovid).start()
    newTime = datetime.now();
    print(oldTime)
    pageLink = "https://covid-dataset-by-bikram.herokuapp.com/CoronaNepal.csv"

    pageResponse = requests.get(pageLink, timeout=50)
    pageContent = BeautifulSoup(pageResponse.content, "html.parser")

    arrayCsv = pageResponse.content.decode("utf-8").split("\n")[-78:-1]


    # print("here is the main therere ")

    cleanArr = list(map(lambda s: s.strip(), arrayCsv))
    #check if the list has histricts
    if len(cleanArr) == 77:
        with open("CoronaNepal.json", "w") as jsonFile:
            json.dump(cleanArr, jsonFile)

    oldTime = newTime

# scrapeCovid()
