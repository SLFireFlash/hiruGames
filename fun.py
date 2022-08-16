import json


def readqs():
    with open("data/qs.json","r")as openfile:
        qaData =json.load(openfile)
    return qaData

def addDataToQs():
    x=1
    fw={}
    fh = open('data/dataans.txt','r',encoding="utf8")
    read_lines = fh.readlines()
    for line in read_lines:
        fw[x]=x
        x+=1
    fh.close()
    print(fw.items)
    with open("data/ans.json","w") as outfile:
        json.dump(fw,outfile,indent=2)

addDataToQs()
