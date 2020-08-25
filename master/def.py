import sqlite3, os, time

def salesdatefetch():  #defining a function to input data into the SQL database's table
    from datetime import date
    import datetime
    sales = sqlite3.connect(r'dbfasales.db')
    salesx = sales.cursor()
    salesx.execute("SELECT prof FROM sales WHERE date BETWEEN datetime('now', '-6 days') AND datetime('now', 'localtime')")
    sumer = 0
    for i in salesx.fetchall():
        sumer += int((i[0]))
    return sumer



def salestodayfetch():  #defining a function to input data into the SQL database's table
    from datetime import date
    import datetime
    sales = sqlite3.connect(r'dbfasales.db')
    salesx = sales.cursor()
    salesx.execute("SELECT prof FROM sales WHERE date = ?", (date.today(), ))
    sumerx = 0
    for i in salesx.fetchall():
        sumerx += int((i[0]))
    return sumerx

from tabularprint import table
sales = sqlite3.connect(r'dbfasales.db')
salesx = sales.cursor()
salesx.execute("SELECT * FROM sales")
salesrows = salesx.fetchall()
col_labels = ("SalesID", "CustomerID", "Product Codes Purchased", "Total", "Profit Earned", "Date of Purchase")
table(col_labels, salesrows)