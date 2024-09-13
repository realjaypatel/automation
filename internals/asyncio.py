import asyncio
import pandas as pd
import pymongo
myArts = pymongo.MongoClient("mongodb+srv://user:user@cluster0.u3fdtma.mongodb.net/ArtDB")
mydb = myArts["ArtDB"]
mycol= mydb["Art"]
import requests
from bs4 import BeautifulSoup

def return_bio(x):
    data = mycol.find_one({"ArtId":x})
    url = data['URL']
    r =  requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    soup = soup.find('p')
    bio = soup
    # bio = str(soup)
    mycol.update_one({'ArtId' : x}, 
                     {'$set' : {'details' : bio }})
    

# for x in range(1,50000):
#     print(x)
#     m = return_bio(x)
#     print("-",m)
    
    
    
return_bio(113)

