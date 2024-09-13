import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from concurrent.futures import ThreadPoolExecutor, as_completed
import pymongo
myArts = pymongo.MongoClient("mongodb+srv://user:user@cluster0.u3fdtma.mongodb.net/ArtDB")
mydb = myArts["ArtDB"]
mycol= mydb["Art"]

def return_bio(x):
    data = mycol.find_one({"ArtId": x})
    url = data['URL']
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    bio = soup.find('p')
    mycol.update_one({'ArtId': x}, {'$set': {'details': str(bio)}})
    return x

def main():
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(return_bio, x) for x in range(1, 50000)]
        for future in as_completed(futures):
            x = future.result()
            print(f"Processed ArtId: {x}")

main()