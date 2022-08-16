import json
from random import randint



def Idgen():
    with open("data/qs.json","r",encoding="utf8")as openfile:
        qsData =json.load(openfile)
        qsDataSize = len(qsData)
        qsId =str(randint(0,qsDataSize))
        return qsId

def readQs(qsId):
    with open("data/qs.json","r",encoding="utf8")as openfile:
        qsData =json.load(openfile)
        qsDataSize = len(qsData)
        return qsData[qsId]

def getans(qsId):
    with open("data/ans.json","r",encoding="utf8")as openfile:
        ansData =json.load(openfile)      
        return ansData[qsId]

def getWrongAns(qsId):
    with open("data/wrongAns.json","r",encoding="utf8")as openfile:
        wrongAns =json.load(openfile)
        return wrongAns[qsId]



