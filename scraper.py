from bs4 import BeautifulSoup
import requests
from flask import g
import json
import threading
from datetime import datetime
import re


def is_ascii(s):
    try:
        s.decode('ascii')
        return True
    except UnicodeDecodeError:
        return False





districts_map = {
    "kathmandu": "Kathmandu",
    "lalitpur": "Lalitpur",
    "morang": "Morang",
    "rupandehi": "Rupandehi",
    "sunsari": "Sunsari",
    "bhaktapur": "Bhaktapur",
    "chitwan": "Chitwan",
    "kaski": "Kaski",
    "kailali": "Kailali",
    "jhapa": "Jhapa",
    "banke": "Banke",
    "makwanpur": "Makwanpur",
    "dang": "Dang",
    "kavrepalanchowk": "Kavrepalanchowk",
    "parsa": "Parsa",
    "dhanusa": "Dhanusa",
    "nawalparasieast": "Nawalpur",
    "surkhet": "Surkhet",
    "sarlahi": "Sarlahi",
    "rauthat": "Rautahat",
    "siraha": "Siraha",
    "kapilvastu": "Kapilvastu",
    "palpa": "Palpa",
    "bara": "Bara",
    "saptari": "Saptari",
    "mahottari": "Mahottari",
    "kanchanpur": "Kanchanpur",
    "bardiya": "Bardiya",
    "tanahun": "Tanahu",
    "achham": "Achham",
    "dhading": "Dhading",
    "dailekh": "Dailekh",
    "nawalparasiwest": "Parasi",
    "gorkha": "Gorkha",
    "nuwakot": "Nuwakot",
    "doti": "Doti",
    "baglung": "Baglung",
    "gulmi": "Gulmi",
    "syangja": "Syangja",
    "lamjung": "Lamjung",
    "pyuthan": "Pyuthan",
    "bajhang": "Bajhang",
    "arghakhanchi": "Arghakhanchi",
    "sindhupalchowk": "Sindhupalchok",
    "dadeldhura": "Dadeldhura",
    "dolkha": "Dolakha",
    "baitadi": "Baitadi",
    "bajura": "Bajura",
    "udayapur": "Udayapur",
    "salyan": "Salyan",
    "sindhuli": "Sindhuli",
    "ramechhap": "Ramechhap",
    "illam": "Ilam",
    "jumla": "Jumla",
    "parbat": "Parbat",
    "darchula": "Darchula",
    "sankhuwasabha": "Sankhuwasabha",
    "rolpa": "Rolpa",
    "kalikot": "Kalikot",
    "dhankuta": "Dhankuta",
    "okhaldhunga": "Okhaldhunga",
    "myagdi": "Myagdi",
    "rukumwest": "Western Rukum",
    "rasuwa": "Rasuwa",
    "khotang": "Khotang",
    "solukhumbu": "Solukhumbu",
    "panchthar": "Panchthar",
    "bhojpur": "Bhojpur",
    "taplejung": "Taplejung",
    "terhathum": "Tehrathum",
    "jajarkot": "Jajarkot",
    "rukumeast": "Eastern Rukum",
    "dolpa": "Dolpa",
    "mustang": "Mustang",
    "humla": "Humla",
    "mugu": "Mugu",
    "manang": "Manang",
}


def scrapeCovid():

    oldTime = datetime.now();

    threading.Timer(300.0, scrapeCovid).start()
    newTime = datetime.now();
    print(oldTime)
    # pageLink = "https://covid-dataset-by-bikram.herokuapp.com/CoronaNepal.csv"

  
    pageLink = "https://covid19.ekantipur.com/"
    pageResponse = requests.get(pageLink).text
    regex = r'\'({.*})\''
    json_string = re.findall(regex, pageResponse)[0]
    data = json.loads(json_string)

    date_today = datetime.today()
    date_today = date_today.strftime("%Y-%m-%d")
    data_array = []
    for district in json.loads(json_string):
        data_array.append(f'{date_today},{district},{districts_map[district]},{data[district]["total"]},{data[district]["deaths"]},{data[district]["recovered"]}')

    if len(data_array) == 77:
        with open("CoronaNepalNew.json", "w") as jsonFile:
            json.dump(data_array, jsonFile)

    oldTime = newTime

# scrapeCovid()
