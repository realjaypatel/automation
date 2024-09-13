import pandas as pd
import pymongo
myArts = pymongo.MongoClient("mongodb+srv://user:user@cluster0.u3fdtma.mongodb.net/ArtDB")
mydb = myArts["ArtDB"]
mycol= mydb["Art"]
import requests
from bs4 import BeautifulSoup

def return_bio(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    soup = soup.find('p')
    return soup

for x in range(1,50000):
    data = mycol.find_one({"ArtId":x})
    url = data['URL']
    bio = return_bio(url)
    bio = str(bio)
    mycol.update_one({'ArtId' : x}, 
                     {'$set' : {'details' : bio }})
    print(x)


