import sqlite3

def cust_listfetch(custid):
    clfetch = sqlite3.connect(r'DBFA_CUSTCC.db')
    clfetchx = clfetch.cursor()
    clfetchx.execute("SELECT custid FROM custcc")
    rows = clfetchx.fetchall()
    custyes = 1
    custno = 2
    custcount = 0
    for row in rows:
        row = row[0]
        if custid == row:
            custcount += 1
        else:
            pass
    if custcount == 1:
        return custyes 
    else:
        return custno 

print(cust_listfetch(30))