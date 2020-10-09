import sqlite3
print("Apply for leave ~") #UDRN
OiD = input("Enter your Employee ID (O-ID): ")
#make db confo here
from datetime import datetime, timedelta
now = datetime.now()
now = now + timedelta(days=1)
dt_string = now.strftime("%Y-%m-%d")
empmas = sqlite3.connect(r'dbfaempmaster.db')
empmascur = empmas.cursor()
empmascur.execute("SELECT Name, Oid FROM emp WHERE Oid = ?", ('%s'%OiD,))
datastream = empmascur.fetchall()
print(datastream[0][1])
if int(OiD) == int(datastream[0][1]):
    confo = input(datastream[0][0] + OiD + ": Confirm leave application? for " + '%s'%dt_string + "(y/n): ")
    if confo in ("y", "Y"):
        print("DOne")
        empmas = sqlite3.connect(r'dbfaempmaster.db')
        empmascur = empmas.cursor()
        empmascur.execute("INSERT INTO leave(Oid, Date) VALUES (?, ?)", ('%s'%OiD, '%s'%dt_string, ))
        empmas.commit()
    else:
        print("Oof. Now get to work ;) ")
else:
    print("Invalid OiD identifier. Please try again ~")