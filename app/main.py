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
    url = "https://sentracomputer.com/brand.php?brand=94"
    response = requests.request("GET", url)

    hasil = {}

    nama = []
    gambar = []
    desk = []

    data = BeautifulSoup(response.text, 'html.parser')
    data = data.find_all('td', attrs={'align': 'center'})

    for i in data:
      nama.append(i.find('b').text)
      try : 
        gambar.append(i.find('a')['href'])
      except :
        gambar.append(i.find('img')['src'])

    data = BeautifulSoup(response.text, 'html.parser')
    data = data.find_all('small')[83:]
    temp = []
    tmp = []

    j = 0
    for i in data:
      if i.text[:2] != 'Rp' :
        j += 1
        tmp.append(i.text)
      else :
        j = 0
        temp.append(tmp)
        tmp = []

    for i in temp :
      tulis = ""
      for j in i :
        tulis += j + '\n\n'
      desk.append(tulis)

    tampung = []

    for i in range(len(nama)) :
        tamp = {}
        tamp["id"] = i
        tamp["href"] = "https://sentracomputer.com/"+gambar[i]
        tamp["title"] = nama[i]
        tamp["deskripsi"] = desk[i]
        print(desk[i])
        tampung.append(tamp)
        
    hasil = {}
    hasil["laptop"] = tampung

    return hasil