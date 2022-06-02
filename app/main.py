from flask import Flask
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
import json

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world() :
    return "hello, world!!"

@app.route("/sentracomputer")
def sentraComputer() :
    url = "https://sentracomputer.com/product.php?category=21&subcat=2"
    response = requests.request("GET", url)

    data = BeautifulSoup(response.text, 'html.parser')
    nameIs = data.find_all('span', attrs={'class': 'bigtitle'})
    descIs = data.find_all('small')
    descIs = descIs[82:]

    descript = []

    for i in descIs :
        if i.text[0:2] != 'Pr' and i.text[0:2] != 'Rp' :  
            descript.append(i.text)

    temp = []

    for i in range(len(descript)) :
        tampung = nameIs[i].find('a')
        tmp = {}
        tmp["href"] = "https://sentracomputer.com/"+tampung["href"]
        tmp["title"] = tampung["title"]
        tmp["deskripsi"] = descript[i]
        temp.append(tmp)
        
    hasil = {}
    hasil["laptop"] = temp

    return hasil