def average(collection,branch):
    total=0
    count=0
    maxstudents=collection.count({"branch":branch})
    for data in collection.find({"branch":branch}):
        total+=data["CGPA"]
    return {"Average":round(total/maxstudents,2)}

def distribution(collections,branch):
    count0=0
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    count6=0
    distribution=dict()
    distcount=dict()
    for data in collections.find({"branch":branch}):
        if data["CGPA"]>=10:
            count0+=1
        elif data["CGPA"]>=9 and data["CGPA"]<10:
            count1+=1
        elif data["CGPA"]>=8 and data["CGPA"]<9:
            count2+=1
        elif data["CGPA"]>=7 and data["CGPA"]<8:
            count3+=1
        elif data["CGPA"]>=6 and data["CGPA"]<7:
            count4+=1
        elif data["CGPA"]>=5 and data["CGPA"]<6:
            count5+=1
        else:
            count6+=1
    distribution["CGPA:10"]="*"*count0
    distribution["CGPA:9-10"]="*"*count1
    distribution["CGPA:8-9"]="*"*count2
    distribution["CGPA:7-8"]="*"*count3
    distribution["CGPA:6-7"]="*"*count4
    distribution["CGPA:5-6"]="*"*count5
    distribution["CGPA:0"]="*"*count6

    distcount["CGPA:10"]=count0
    distcount["CGPA:9-10"]=count1
    distcount["CGPA:8-9"]=count2
    distcount["CGPA:7-8"]=count3
    distcount["CGPA:6-7"]=count4
    distcount["CGPA:5-6"]=count5
    distcount["CGPA:0"]=count6

    return {"bars:":distribution,"count:":distcount}
    
