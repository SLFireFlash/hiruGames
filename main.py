from fun import *
from random import randint
mixAnsList =[]


qid=Idgen()
print(readQs(qid))
print("choose your answer:-")
mixans = randint(0,1)
mixAnsList.insert(0,getans(qid))
mixAnsList.insert(1,getWrongAns(qid))
print("\t1:", mixAnsList[mixans])
if (mixans == 0):
    print("\t2:",mixAnsList[1])
    ansid = 1
else:
    print("\t2:",mixAnsList[0])
    ansid = 2

uans =int(input("enter answer 1 or 2:-"))
if uans == ansid:
    print("ඔයාගෙ උත්තරය හරි කොමොලෝ")
else:
    print("ඔයාගෙ උත්තරය වැරදියි මචෝ")
    
    

