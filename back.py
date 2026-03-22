from fastapi import FastAPI
from pymongo import MongoClient

#DataBase Connection:
client=MongoClient(url)

db=client["college"]
collection=db["student"]

#DataBase Connections Completed : Now Data Can Be Retreived From collection

# Backend Connections
app=FastAPI()


# HTTP GET REQUEST TO FECTH ALL DATA IN student COLLECTION stored in MONGO DB DataBase
@app.get("/alldata")
def alldataset():
    store=[]
    for data in collection.find():
        data['_id']=str(data['_id'])
        store.append(data)
    return store

@app.get("/top/{i}/{branch}")
def retrievetops(i:int,branch:str):
    toppers=[]
    for data in collection.find({"branch":branch}).sort('CGPA',-1).limit(i):
        data['_id']=str(data['_id'])
        toppers.append(data)
    return toppers
