from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
from stats import distribution,average 
import os
import time

load_dotenv()
url=os.getenv("url")

#DataBase Connection:
client=MongoClient("url")

db=client["college"]
collection=db["student"]

#DataBase Connections Completed : Now Data Can Be Retreived From collection

# Backend Connections
app=FastAPI()

@app.get("/alldata")
def alldataset():
    store=[]
    rank=0
    for data in collection.find():
        rank+=1
        del(data['_id'])
        data['rank']=rank
        store.append(data)
    return store

@app.get("/top/{i}/{branch}")
def retrievetops(i:int,branch:str):
    start=time.time()
    toppers=[]
    rank=0
    prev=float('inf')
    excess=1
    for data in collection.find({"branch":branch}).sort([('CGPA',-1),('htno',1)]).limit(i):
        del(data['_id'])
        if (data['CGPA']==prev):
            data['rank']=rank
            excess+=1
        else:
            rank+=excess
            excess=1
            data['rank']=rank
        prev=data["CGPA"]
        toppers.append(data)
    end=time.time()
    print("Time=",end-start)
    return toppers

@app.get("/{branch}/average")
def avg(branch:str):
    return average(collection,branch)

@app.get("/{branch}/distribution")
def distrib(branch:str):
    return distribution(collection,branch)
        
