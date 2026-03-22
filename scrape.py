from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
import random
from pymongo import MongoClient
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo.server_api import ServerApi

uri = "mongodb"

client = MongoClient(uri, server_api=ServerApi('1'))

db=client["college"]
collection=db["student"]


driver=webdriver.Edge()
driver.get("http://202.65.154.110/be-results-i-semester-12-02-2026/")
wait=WebDriverWait(driver,10)

result=[]
htno=""
topper=0
countmax=0
countmin=0
fail=0
total=0
start=time.perf_counter()
miss=0
i=0
while True:
    i+=1
    htno=f"1602-25-733-{i:03d}"
    input_box=driver.find_element(By.ID,'txtHTNO')
    input_box.clear()
    input_box.send_keys(htno)
    driver.find_element(By.ID,'btnResults').click()
    time.sleep(random.uniform(1,2))
    try:
        cgpa_element=wait.until(EC.presence_of_element_located((By.ID,'lblCGPA')))
        cgpa=cgpa_element.text
        old_name=wait.until(EC.presence_of_element_located((By.ID,'lblStudName')))
        name=old_name.text
        cgpa_float=float(cgpa.split(':')[-1].strip())
        total+=1
        if cgpa_float==10:
            topper+=1
        elif cgpa_float>9.00:
            countmax+=1
        elif 8.00<=cgpa_float<=9.00:
            countmin+=1
        elif cgpa_float==0.0:
            fail+=1
        data={"htno":htno,
              "name":name,
              "CGPA":cgpa_float
              }
        print(data)
        result.append(data)
        miss=0
    except Exception as e:
        print(f"{htno} -> Not Found | {e}")
        miss+=1
    if miss>=10:
        break
end=time.perf_counter()
print("Students with GPA 10:",topper)
print("Students with GPA (9-10):",countmax)
print("Students with GPA (8-9]:",countmin)
print("Students with GPA (5-8]:",total-topper-countmax-countmin-fail)
print("Students with GPA<5:",fail)
print("Time Consumed is:",end-start,"  Seconds")
try:
    collection.insert_many(result)
    print("Data Uploaded To Mongo DB")
except:
    print("Connection To Mongo DB FAil...")






