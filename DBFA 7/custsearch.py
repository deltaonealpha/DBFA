import sqlite3
from tabulate import tabulate

con = sqlite3.connect(r'DBFA.db')
conn = con.cursor()

conx = sqlite3.connect(r'DBFA_CUSTCC.db')
connx = conx.cursor()

searchcon = str(input("Customer Name: "))
if " " in searchcon:  
    for i in searchcon:
        sconsplit = searchcon.split(" ")
        for j in sconsplit:
            conn.execute("SELECT custt FROM cust WHERE custname LIKE ?", (("%"+searchcon+"%"), ))
            searchdata = conn.fetchall()
        else:
            searchcon = searchcon.replace(" ", "")
            conn.execute("SELECT custt FROM cust WHERE custname LIKE ?", (("%"+searchcon+"%"), ))
            searchdata = conn.fetchall()
            if len(searchdata) != 0:
                pass
            else:
                searchdata = "No such customer found."
else:      
    conn.execute("SELECT custt FROM cust WHERE custname LIKE ?", (("%"+searchcon+"%"), ))
    searchdata = conn.fetchall()

if len(searchdata) != 0:
    if len(searchdata) > 1:
        for i in searchdata:
            conn.execute("SELECT * FROM cust WHERE custt = ?", (i[0], ))
            custdata = conn.fetchall()
            #col_labels = ("ID", "Customer NAME", "EMAIL")
            #table(col_labels, custdata)

            connx.execute("SELECT * FROM custcc WHERE custid = ?", (i[0], ))
            custdatax = connx.fetchall()
            ccrt = []            
            for jk in custdata:
                for jkx in jk:
                    ccrt.append(str(jkx))
            for jk in custdatax:
                for jkx in jk:
                    ccrt.append(str(jkx))

            col_labels = ('ID', 'Customer NAME', 'EMAIL', 'ID', 'Name', 'Purchases Made', 'Total', 'Loyalty Points')
            print(tabulate(zip(col_labels, ccrt), floatfmt = ".4f"))

            print(" ")
    else:
        conn.execute("SELECT * FROM cust WHERE custt = ?", (searchdata[0][0], ))
        custdata = conn.fetchall()

        connx.execute("SELECT * FROM custcc WHERE custid = ?", (searchdata[0][0], ))
        custdatax = connx.fetchall()
        ccrt = []            
        for jk in custdata:
            for jkx in jk:
                ccrt.append(str(jkx))
        for jk in custdatax:
            for jkx in jk:
                ccrt.append(str(jkx))

        col_labels = ('ID', 'Customer NAME', 'EMAIL', 'ID', 'Name', 'Purchases Made', 'Total', 'Loyalty Points')
        print(tabulate(zip(col_labels, ccrt), floatfmt = ".4f"))
else:
    print("Customer not found.")
