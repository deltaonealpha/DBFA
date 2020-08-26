'''     ___ ______ ___   _____________    ____________     _______
       /  /_______/  /  /  /_______/  /  /  /________/    /  /_/ /
      /  /       /  /  /  /       /  /  /  /             /  /  / /
     /  /       /  /  /  /_______/  /  /  /             /  /   / /
    /  /       /  /  / // // // // /  /  /_________    /  /____/ / BILLING 
   /  /       /  /  /  /-------/  /  /  /_________/   /  /_____/ / FRAMEWORK 
  /  /       /  /  /  /       /  /  /  /             /  /      / /
 /  /_______/  /  /  /______ /  /  /  /             /  /       / /
/__/_______/__/  /__/_______/__/  /__/             /__/        /_/
'''
#vs

import getpass, time, pathlib, sqlite3, sys, os #sys, os for system-level ops
from tabularprint import table
from tqdm import tqdm 
import webbrowser

# HUGE credits to XanderMJ (https://github.com/XanderMJ/spotilib)
import spotilib

from SwSpotify import spotify


filedel = open('./DBFAdeliveries.txt', 'a+')
filedel.close()

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import math, random
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('MiLanProVF', r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\MiLanProVF.ttf'))
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from tabulate import tabulate
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import requests
import cv2

logox = ('''
   _____   ____    ____  ____  _____
  / /  // / /  \\ /___  /__||  |--// 
 / /  // / /===| ///// ////||    // 
/_/__// /_/__ / /     /    ||   // 
    ''')

global cccheck

#auth verification
if os.path.exists(r'userblock.zconf'):
    print("Verifying login...")
    print(" ")
if os.path.exists(r'userblock.txt'):
    userblock = open(r"userblock.txt","r") #Opening / creating (if it doesn't exist already) the .txt record file
    redflag = 1
else:
    redflag = 0
if os.path.exists(r'DBFA.zconf'):
    pass
else:
    print("Getting the database online.......")
    time.sleep(0.2)
    con = sqlite3.connect(r'DBFA.db')
    print("Rebuilding database..")
    c = con.cursor()
    #c.execute("DROP TABLE cust;")
    c.execute("""CREATE TABLE IF NOT EXISTS cust
        (custt INTEGER PRIMARY KEY,
        custname TEXT,
        email TEXT);""")
try:
    if os.path.exists(r'userblock.txt'):
        os.remove(r'userblock.txt')
    if os.path.exists(r'userblock.zconf'):
        os.remove(r'userblock.zconf')
except PermissionError:
    pass



#Stock Order Manager
xon = sqlite3.connect(r'DBFA_vend.db')
xbr7 = xon.cursor()
xbr7.execute("""CREATE TABLE IF NOT EXISTS stock
    (prodid INTEGER PRIMARY KEY,
    prodname CHAR,
    ordqty VARCHAR(500),
    delivered INT,
    delstat CHAR,
    vendor CHAR,
    vendcont CHAR,
    lowstock INT);""")
xon = sqlite3.connect(r'DBFA_vend.db')
xbr7 = xon.cursor()
if os.path.exists(r'DBFA_vend.db'):
    pass
else:
    xbr7.execute("""CREATE TABLE IF NOT EXISTS stock
    (prodid INTEGER PRIMARY KEY,
    prodname CHAR,
    ordqty VARCHAR(500),
    delivered INT,
    delstat CHAR,
    vendor CHAR,
    vendcont CHAR
    lowstock INT);""")

st = sqlite3.connect(r'DBFA_vend.db')
stx = st.cursor()
stockq = """UPDATE stock SET delstat = ? WHERE ordqty = 0"""
qans = ("DELIVERED", )
stx.execute(stockq, qans)
stockq = """UPDATE stock SET delstat = ? WHERE ordqty != 0"""
qans = ("TBD", )
stx.execute(stockq, qans)
st.commit()

#NEW Sales Report v2 DB Logger
sales = sqlite3.connect(r'dbfasales.db')
salesx = sales.cursor()
if os.path.exists(r'dbfasales.db'):
    pass
else:
    salesx.execute("""CREATE TABLE IF NOT EXISTS sales
    (sno INT PRIMARY KEY,
    custid INT,
    prodid INT,
    net INT,
    prof INT,
    date DATE);""")
    sales.commit()
    print("Table restructured! ")



class HiddenPrints:
            def __enter__(self):
                self._original_stdout = sys.stdout
                sys.stdout = open(os.devnull, 'w')
            def __exit__(self, exc_type, exc_val, exc_tb):
                sys.stdout.close()
                sys.stdout = self._original_stdout
                print()

# TG Communicator
def telegram_bot_sendtext(bot_message):
    
    with HiddenPrints():
        bot_token = '1215404401:AAEvVBwzogEhOvBaW5iSpHRbz3Tnc7fCZis'
        bot_chatID = '680917769'
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        return response.json()

def getOTP():
    global otp
    digits = "0123456789"
    otp = ""
    otp += (digits[math.floor(random.random() * 10)])
    otp += (digits[math.floor(random.random() * 10)])
    otp += (digits[math.floor(random.random() * 10)])
    otp += (digits[math.floor(random.random() * 10)])


# DBFA Logo Printer
def logoprintxrt():
            print("        ___ ______ ___   _____________    ____________     _______")
            time.sleep(0.05)
            print("       /  /_______/  /  /  /_______/  /  /  /________/    /  /_/ /")
            time.sleep(0.05)
            print("      /  /       /  /  /  /       /  /  /  /             /  /  / /")
            time.sleep(0.05)
            print("     /  /       /  /  /  /_______/  /  /  /  CLI        /  /   / /")
            time.sleep(0.05)
            print("    /  /       /  /  / // // // // /  /  /_________    /  /____/ /")
            time.sleep(0.05)
            print("   /  /       /  /  /  /-------/  /  /  /_________/   /  /_____/ /")
            time.sleep(0.05)
            print("  /  /       /  /  /  /       /  /  /  /             /  /      / /")
            time.sleep(0.05)
            print(" /  /_______/  /  /  /______ /  /  /  /             /  /       / /")
            time.sleep(0.05)
            print("/__/_______/__/  /__/_______/__/  /__/             /__/        /__/")
            print(" ")
            print(" ")



# Database section
# Stock Records Master DB
ssh = sqlite3.connect(r'DBFA_handler.db')
ssh7 = ssh.cursor()
#c.execute("DROP TABLE cust;")
ssh7.execute("""CREATE TABLE IF NOT EXISTS sshandler
    (prodid INTEGER,
    prodname CHAR,
    ssstock INTEGER);""")
ssh = sqlite3.connect('DBFA_handler.db')
ssh7 = ssh.cursor()
if os.path.exists(r'DBFA_handler.db'):
    pass
else:
    ssh7.execute("""CREATE TABLE IF NOT EXISTS sshandler
        (prodid INTEGER,
        prodname CHAR,
        ssstock INTEGER);""")


# Invoice Master DB
inmas = sqlite3.connect(r'invoicemaster.db')
inmascur = inmas.cursor()
#c.execute("DROP TABLE cust;")
inmascur.execute("""CREATE TABLE IF NOT EXISTS inmas
    (indid INTEGER);""")
inmas = sqlite3.connect('invoicemaster.db')
inmascur = inmas.cursor()
if os.path.exists(r'invoicemaster.db'):
    pass
else:
    inmascur.execute("""CREATE TABLE IF NOT EXISTS inmas
    (indid INTEGER);""")


# Voucher Records Master DB
isol = sqlite3.connect(r'cponmgmtsys.db')
isolx = isol.cursor()
isolx.execute("""CREATE TABLE IF NOT EXISTS cponmaster
    (cponid CHAR PRIMARY KEY,
    cponlim INTEGER,
    cponvalue INTEGER,
    cpondtb DATE);""")
isol = sqlite3.connect('cponmgmtsys.db')
isolx = isol.cursor()
if os.path.exists(r'cponmgmtsys.db'):
    pass
else:
    isolx.execute("""CREATE TABLE IF NOT EXISTS cponmaster
        (cponid CHAR PRIMARY KEY,
        cponlim INTEGER,
        cponvalue INTEGER,
        cpondtb DATE);""")


# Customer Records Master DB
xon = sqlite3.connect(r'DBFA_CUSTCC.db')
xbr7 = xon.cursor()
xbr7.execute("""CREATE TABLE IF NOT EXISTS custcc
    (custid INTEGER PRIMARY KEY,
    custname VARCHAR(500),
    purchasecount INTEGER,
    ptotalx INTEGER,
    points INTEGER);""")
xon = sqlite3.connect('DBFA_CUSTCC.db')
xbr7 = xon.cursor()
if os.path.exists(r'DBFA_CUSTCC.db'):
    pass
else:
    xbr7.execute("""CREATE TABLE IF NOT EXISTS custcc
    (custid INTEGER PRIMARY KEY,
    custname VARCHAR(500),
    purchasecount INTEGER,
    ptotalx INTEGER,
    points INTEGER);""")



 
conn = sqlite3.connect('DBFA.db')
if os.path.exists(r'DBFA.db'):
    pass
else:
    xbr7.execute("""CREATE TABLE IF NOT EXISTS custcc
        (custt INTEGER PRIMARY KEY,
        custname VARCHAR(500),
        purchasecount INTEGER,
        ptotalx INTEGER);""")



# Report Record Master
rec = sqlite3.connect(r'recmaster.db')
recx = rec.cursor()
recx.execute("""CREATE TABLE IF NOT EXISTS recmasterx
    (prodid INTEGER PRIMARY KEY,
    prodname CHAR,
    prodprofit INTEGER,
    prodsales INTEGER,
    netprof INTEGER);""")
rec = sqlite3.connect('recmaster.db')
recx = rec.cursor()
if os.path.exists(r'recmaster.db'):
    pass
else:
    recx.execute("""CREATE TABLE IF NOT EXISTS recmasterx
    (prodid INTEGER PRIMARY KEY,
    prodname CHAR,
    prodprofit INTEGER,
    prodsales INTEGER,
    netprof INTEGER);""")
    namiex = ["TV 4K OLED 50", "TV FHD OLED 50", "8K QLED 80", "Redmi K20 PRO", "Redmi K20", "Redmi Note 9 PRO", "POCOPHONE F1", "Mi MIX ALPHA", "Wireless Headphones", "Noise-Cancelling Wireless Headphones", "Essentials Headphones", "Gaming Headphones", "Truly-Wireless Eadphones", "Neckband-Style Wireless Earphones", "Essentials Earphones", "Gaming Earphones", "30W Bluetooth Speakers", "20W Bluetooth Speakers", "Essentials Bluetooth Speaker", "BOSE QC35", "Essentials Home Theatre", "Wired Speaker - 5.1", "Essentials Wired Speaker - STEREO", "Tactical Series Power Bank 30000mah", "Essentials Power Bank 10000mah", "Essentials Mouse", "Logitech G604 LightSpeed Wireless", "Tactical Essentials Keyboard", "DROP GS21k RGB Gaming Keyboard", "Polowski Tactical Flashlight", "OneFiber Wi-Fi Router AX7", "Mijia Mesh Wi-Fi Router", "lapcare 45W Laptop Adapter", "lapcare 60W Laptop Adapter","Spigen Phone Case(s)", "Essentials Phone Charger 15W", "HyperPower Type-C Gallium-Nitride Charger 120W", "ASUS Zephyrus G4 Gaming Laptop", "DELL XPS 5 Content Creator's Laptop", "Hewlett-Packard Essential's Student's Laptop (Chromebook)"]
    profitx = [2000, 4500, 5700, 2000, 2100, 1470, 300, 11000, 400, 2000, 100, 370, 450, 120, 50, 275, 649, 140, 50, 1050, 978, 150, 100, 320, 98, 75, 170, 60, 275, 90, 210, 780, 50, 35, 50, 30, 100, 8000, 9000, 1790]
    profitmarker = 0
    for crrt in namiex:
        profvalue = profitx[profitmarker]
        gg = (namiex.index(crrt)) + 1
        strx = "insert into recmasterx(prodid, prodname, prodprofit, prodsales, netprof) values(?, ?, ?, ?, ?)"
        io = (gg, crrt, profvalue, 0, 0)
        profitmarker += 1
        recx.execute(strx, io)
        rec.commit()
        print("Added record: ", crrt)









# Functions::

# DBFA Stock Master v1


def orderstock(prodid, qty):
    st = sqlite3.connect(r'DBFA_vend.db')
    stx = st.cursor()
    stockq = """UPDATE stock SET ordqty = ordqty + ? WHERE prodid = ?"""
    qans = (qty, prodid)
    stx.execute(stockq, qans)
    st.commit()
    print("Recieved order for product", prodid, "; qty", qty)
    st = sqlite3.connect(r'DBFA_vend.db')
    stx = st.cursor()
    stockq = """UPDATE stock SET delstat = ? WHERE ordqty = 0"""
    qans = ("DELIVERED", )
    stx.execute(stockq, qans)
    stockq = """UPDATE stock SET delstat = ? WHERE ordqty != 0"""
    qans = ("TBD", )
    stx.execute(stockq, qans)
    st.commit()


def delivered(qty, prodid):
    st = sqlite3.connect(r'DBFA_vend.db')
    stx = st.cursor()
    stockq = """SELECT ordqty FROM stock WHERE prodid = ?"""
    qans = (prodid, )
    stx.execute(stockq, qans)
    st.commit()
    aaa = (int(stx.fetchall()[0][0]))
    if aaa >= qty:
        st = sqlite3.connect(r'DBFA_vend.db')
        stx = st.cursor()
        xstockq = """UPDATE stock SET ordqty = ordqty - ? WHERE prodid = ?"""
        xqans = (qty, prodid, )
        stx.execute(xstockq, xqans)
        xstockq = """UPDATE stock SET delivered = delivered + ? WHERE prodid = ?"""
        xqans = (qty, prodid, )
        stx.execute(xstockq, xqans)
        st.commit()
        print("Quantity ", qty, "recieved.")
    else:
        print("Cannot set status for qty:", qty, "for prod:", prodid, "as the ordered qty is lower than the delivered qty being set.")
    st = sqlite3.connect(r'DBFA_vend.db')
    stx = st.cursor()
    stockq = """UPDATE stock SET delstat = ? WHERE ordqty = 0"""
    qans = ("DELIVERED", )
    stx.execute(stockq, qans)
    stockq = """UPDATE stock SET delstat = ? WHERE ordqty != 0"""
    qans = ("TBD", )
    stx.execute(stockq, qans)
    st.commit()
        

def delstatmass():
    isol = sqlite3.connect(r'DBFA_vend.db')
    isolx = isol.cursor()
    print("\n\nProduct stock yet to be recieved: \n")
    isolx = isol.cursor()
    isolx.execute(("SELECT * from stock WHERE delstat = ?"), ("TBD", ))
    rows = isolx.fetchall()
    col_labels = ("P. ID", "P. Name", "Qty. Ordered", "Delivered","Vendor", "Vendor", "Vendor Contact", "Lowstock Bar")
    table(col_labels, rows)
    print("\n\nProduct stock recieved: \n")
    isolx.execute(("SELECT * from stock WHERE delstat = ?"), ("DELIVERED", ))
    rows = isolx.fetchall()
    col_labels = ("P. ID", "P. Name", "Qty. Ordered", "Delivered","Vendor", "Vendor", "Vendor Contact", "Lowstock Bar")
    table(col_labels, rows)

def delstatindvl(prodid):
    isol = sqlite3.connect(r'DBFA_vend.db')
    isolx = isol.cursor()
    print("\n\nDetails for product ID", prodid, ": \n")
    isolx.execute(("SELECT * from stock WHERE prodid = ?"), (prodid, ))
    rows = isolx.fetchall()
    if rows in ([], (), "", " ", None):
        print("-------------------------------------------------------------")
        print("| Entered product ID could not be located in DBFA's records |")
        print("-------------------------------------------------------------\n\n")
    else:
        col_labels = ("P. ID", "P. Name", "Qty. Ordered", "Delivered","Vendor", "Vendor", "Vendor Contact", "Lowstock Bar")
        table(col_labels, rows)


def vendorfetch(prodid):
    isol = sqlite3.connect(r'DBFA_vend.db')
    isolx = isol.cursor()
    print("\n\nVendor details for product ID", prodid, ":")
    isolx.execute(("SELECT vendor from stock WHERE prodid = ?"), (prodid, ))
    rows = isolx.fetchall()
    if rows in ([], (), "", " ", None):
        print("-------------------------------------------------------------")
        print("| Entered product ID could not be located in DBFA's records |")
        print("-------------------------------------------------------------\n")
    else:
        print("Vendor:", rows[0][0])


def vendorcontact(prodid):
    isol = sqlite3.connect(r'DBFA_vend.db')
    isolx = isol.cursor()
    print("\n\nVendor contact for product ID", prodid, ":")
    isolx.execute(("SELECT vendcont from stock WHERE prodid = ?"), (prodid, ))
    rows = isolx.fetchall()
    if rows in ([], (), "", " ", None):
        print("-------------------------------------------------------------")
        print("| Entered product ID could not be located in DBFA's records |")
        print("-------------------------------------------------------------\n")
    else:
        print("Vendor contact:", rows[0][0])
        confac = input("Contact vendor? (y/n): ")                    
        if confac == "y":
            import webbrowser
            webbrowser.open(('mailto:'+'%s'%rows[0][0]), new=1)
        elif confac == "n":
            pass
        else:
            print("Invalid option entered. ")
            vendorcontact(prodid)


def lowbarmodif(prodid):
    isol = sqlite3.connect(r'DBFA_vend.db')
    isolx = isol.cursor()
    print("\n\nLow-stock bar for product ID", prodid, ":")
    isolx.execute(("SELECT lowstock from stock WHERE prodid = ?"), (prodid, ))
    rows = isolx.fetchall()
    if rows in ([], (), "", " ", None):
        print("-------------------------------------------------------------")
        print("| Entered product ID could not be located in DBFA's records |")
        print("-------------------------------------------------------------\n")
    else:
        print("Current low-stock bar:", rows[0][0])
        modifier = int(input("Enter the new limit: "))
        if modifier <=0:
            print("Cannot set a negative/ null value as low-stock warning limit! ")
            print("Try again: ")
            time.sleep(1)
            lowbarmodif(prodid)
            print("Modified. New limit:", rows[0][0])
        isol = sqlite3.connect(r'DBFA_vend.db')
        isolx = isol.cursor()
        isolx.execute(("UPDATE stock SET lowstock = ? WHERE prodid = ?"), (modifier, prodid, ))
        isol.commit()
        rows = isolx.fetchall()
        isolx.execute(("SELECT lowstock from stock WHERE prodid = ?"), (prodid, ))
        rows = isolx.fetchall()
        print("New limit set: ", rows[0][0])
        time.sleep(1)


def lowbar(prodid):
    isol = sqlite3.connect(r'DBFA_vend.db')
    isolx = isol.cursor()
    isolx.execute(("SELECT lowstock from stock WHERE prodid = ?"), (prodid, ))
    rows = isolx.fetchall()
    print(rows[0][0])


# Report Stock Fetcher
namiex = ["TV 4K OLED 50", "TV FHD OLED 50", "8K QLED 80", "Redmi K20 PRO", "Redmi K20", "Redmi Note 9 PRO", "POCOPHONE F1", "Mi MIX ALPHA", "Wireless Headphones", "Noise-Cancelling Wireless Headphones", "Essentials Headphones", "Gaming Headphones", "Truly-Wireless Eadphones", "Neckband-Style Wireless Earphones", "Essentials Earphones", "Gaming Earphones", "30W Bluetooth Speakers", "20W Bluetooth Speakers", "Essentials Bluetooth Speaker", "BOSE QC35", "Essentials Home Theatre", "Wired Speaker - 5.1", "Essentials Wired Speaker - STEREO", "Tactical Series Power Bank 30000mah", "Essentials Power Bank 10000mah", "Essentials Mouse", "Logitech G604 LightSpeed Wireless", "Tactical Essentials Keyboard", "DROP GS21k RGB Gaming Keyboard", "Polowski Tactical Flashlight", "OneFiber Wi-Fi Router AX7", "Mijia Mesh Wi-Fi Router", "lapcare 45W Laptop Adapter", "lapcare 60W Laptop Adapter","Spigen Phone Case(s)", "Essentials Phone Charger 15W", "HyperPower Type-C Gallium-Nitride Charger 120W", "ASUS Zephyrus G4 Gaming Laptop", "DELL XPS 5 Content Creator's Laptop", "Hewlett-Packard Essential's Student's Laptop (Chromebook)"]
def repstockfetch(): 
    global tabarter
    ssh = sqlite3.connect('DBFA_handler.db')
    ssh.row_factory = lambda cursor, row: row[0]
    ssh7 = ssh.cursor()
    ssh7.execute("SELECT DISTINCT prodid FROM sshandler WHERE ssstock < 5;")
    axrows = ssh7.fetchall()
    tabarter = []
    for i in axrows:
        ssh7.execute("SELECT DISTINCT ssstock FROM sshandler WHERE prodid = ?;", (i,))
        a = [('%s'%(i)), namiex[i], "Stock Remaining: ", '%s'%(ssh7.fetchall()[0])]
        tabarter.append(a)
    if tabarter == []:
        tabarter.append("--")

def repdatafetch():
    global charter, rows
    charter = ""
    charter += "DBFA STORE REPORT\n"
    rec = sqlite3.connect(r'recmaster.db')
    recx = rec.cursor()
    charter += "\nSales data:: \n\n"
    time.sleep(1)
    recx.execute("SELECT DISTINCT prodid, prodname, prodprofit, prodsales, netprof FROM recmasterx")
    rows = recx.fetchall()
    '''
    for row in rows:
        print(row)
    '''
    ll = [("P.ID","Prod. Name","Profit P.U.","Qty. Sold","Net Profit")]
    rows = ll + rows
    time.sleep(0.1)
    #print(" ") 
    

def repupdate(prodid):
    rec = sqlite3.connect(r'recmaster.db')
    recx = rec.cursor()
    # hidden prints here ig
    updatexr = ("UPDATE recmasterx SET prodsales = prodsales + 1 WHERE prodid = ?")
    updatexxr = ("UPDATE recmasterx SET netprof = prodsales*prodprofit WHERE prodid = ?")
    indicator = (prodid, )
    recx.execute(updatexr, indicator)
    recx.execute(updatexxr, indicator)
    rec.commit()
    recx.close()


# Feature not released
# Invoice Master Record Maintainer
def inmaintainer():
    inmas = sqlite3.connect('invoicemaster.db')
    inmascur = inmas.cursor()
    updatetrtt = """UPDATE inmas SET indid = indid + 1"""
    inmascur.execute(updatetrtt)
    inmas.commit()
    inmascur.close()
    #time.sleep(1)
    #toaster.show_toast+("DBFA QuickVend Service - Background Sync", duration = 0.4)

def infetch():
    global inval
    inmas = sqlite3.connect('invoicemaster.db')
    inmascur = inmas.cursor()
    inmascur.execute("SELECT DISTINCT indid FROM inmas")
    rows = inmascur.fetchall()
    inval = int(rows[0][0])


# Stock System
# Mass Stock Allocator
def massmaintainer(inxstock):  #defining a function to input data into the SQL database's table
    try:
        idList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
        ssxconn = sqlite3.connect(r"DBFA_handler.db")
        ssxsql = 'DELETE FROM sshandler'
        ssxcur = ssxconn.cursor()
        ssxcur.execute(ssxsql)
        ssxconn.commit()
    except sqlite3.Error as error:
        print("Failed to flush multiple records from sqlite table", error)
    
    ssh = sqlite3.connect(r'DBFA_handler.db')
    ssh7 = ssh.cursor()
    namiex = ["TV 4K OLED 50", "TV FHD OLED 50", "8K QLED 80", "Redmi K20 PRO", "Redmi K20", "Redmi Note 9 PRO", "POCOPHONE F1", "Mi MIX ALPHA", "Wireless Headphones", "Noise-Cancelling Wireless Headphones", "Essentials Headphones", "Gaming Headphones", "Truly-Wireless Eadphones", "Neckband-Style Wireless Earphones", "Essentials Earphones", "Gaming Earphones", "30W Bluetooth Speakers", "20W Bluetooth Speakers", "Essentials Bluetooth Speaker", "BOSE QC35", "Essentials Home Theatre", "Wired Speaker - 5.1", "Essentials Wired Speaker - STEREO", "Tactical Series Power Bank 30000mah", "Essentials Power Bank 10000mah", "Essentials Mouse", "Logitech G604 LightSpeed Wireless", "Tactical Essentials Keyboard", "DROP GS21k RGB Gaming Keyboard", "Polowski Tactical Flashlight", "OneFiber Wi-Fi Router AX7", "Mijia Mesh Wi-Fi Router", "lapcare 45W Laptop Adapter", "lapcare 60W Laptop Adapter","Spigen Phone Case(s)", "Essentials Phone Charger 15W", "HyperPower Type-C Gallium-Nitride Charger 120W", "ASUS Zephyrus G4 Gaming Laptop", "DELL XPS 5 Content Creator's Laptop", "Hewlett-Packard Essential's Student's Laptop (Chromebook)"]
    for crrt in namiex:
        gg = (namiex.index(crrt)) + 1
        str = "insert into sshandler(prodid, prodname, ssstock) values(?, ?, ?)"
        strxx = (gg, crrt, inxstock,)
        ssh7.execute(str, strxx)
        ssh.commit()
    ssh7.close()
    time.sleep(1)
    print("DBFA QuickVend service - Stock universally enforced to", inxstock)
    time.sleep(1)


# Induvidual Stock Allocator
def ssxupdatescript(inxssincremental, prodid):
    ssh = sqlite3.connect('DBFA_handler.db')
    ssh7 = ssh.cursor()
    updatetr = """UPDATE sshandler SET ssstock = ssstock + ? WHERE prodid = ?"""
    xrindicator = (inxssincremental, prodid)
    ssh7.execute(updatetr, xrindicator)
    ssh.commit()
    ssh7.close()
    time.sleep(1)
    print("DBFA QuickVend Service - Stock added for", prodid, "as", inxssincremental)

# Stock Data Fetcher
def ssxsuperfetch():
    ssh = sqlite3.connect('DBFA_handler.db')
    ssh7 = ssh.cursor()
    print("Connecting to QuickVend Service... ~~~")  #SQL connection prompt
    print("Store Stock:: ")
    time.sleep(1.5) 
    #Re-writing to refresh connection
    ssh7 = ssh.cursor()
    ssh7.execute("SELECT DISTINCT prodid, prodname, ssstock FROM sshandler")
    rows = ssh7.fetchall()
    col_labels = ("Product ID", "Product Name", "Product Stock")
    table(col_labels, rows)
    

# Purchase-time Stock Handler
def ssxstockmaintainer(prodid):
    ssh = sqlite3.connect('DBFA_handler.db')
    ssh7 = ssh.cursor()
    updatetrtt = """UPDATE sshandler SET ssstock = ssstock - 1 WHERE prodid = ?"""
    xrindicatortt = (prodid,)
    ssh7.execute(updatetrtt, xrindicatortt)
    ssh.commit()
    ssh7.close()
    #time.sleep(1)
    #toaster.show_toast("DBFA QuickVend Service - Background Sync", duration = 0.4)

# Induvidual Stock Fetcher
def ssxstockmaster(prodid): 
    global ssxvarscheck
    ssxvarscheck = 0
    ssh = sqlite3.connect('DBFA_handler.db')
    ssh.row_factory = lambda cursor, row: row[0]
    ssh7 = ssh.cursor()
    csrr = ("SELECT ssstock FROM sshandler WHERE prodid = (?);")
    csrrxt = (prodid,)
    ssh7.execute(csrr, csrrxt)
    rows = ssh7.fetchall()
    # print(rows) #debug point
    values = ','.join(str(v) for v in rows)
    ssxdsccheck = "1 2 3 4"
    isolx = sqlite3.connect(r'DBFA_vend.db')
    isolxx = isolx.cursor()
    isolxx.execute(("SELECT lowstock from stock WHERE prodid = ?"), (prodid, ))
    rowsr = isolxx.fetchall()
    limiterx = []
    for ix in range (1, int((rowsr[0][0]))+1):
        limiterx.append(ix)
    if int(values) in limiterx:
        print("[Stock running out] Currently in stock: ", values, "pieces. Restock ASAP...")
        ssxvarscheck = 1
    elif int(values) == 0:
        print("Current product stock: ", values)
        ssxvarscheck = 2
    elif int(values) < 1:
        print("Current product stock: ", values)
        ssxvarscheck = 2
    else:
        print("Current product stock: ", values)
        ssxvarscheck = 1
    time.sleep(0.2)
    #toaster.show_toast("DBFA QuickVend Service - Background Sync", duration = 0.3427)




# Voucher System
# Voucher User
def cponuse(cponid):
    isol = sqlite3.connect('cponmgmtsys.db')
    isolx = isol.cursor()
    mod = """UPDATE cponmaster SET cponlim = cponlim - 1 WHERE cponid = ?"""
    idler = (cponid, )
    isolx.execute(mod, idler)
    isol.commit()

# Single Voucher Data Fetcher
def cpon_singlefetch(cponid): 
    isol = sqlite3.connect('cponmgmtsys.db')
    isolx = isol.cursor()
    isol.row_factory = lambda cursor, row: row[0]
    csrr = ("SELECT cponid, cponlim, cponvalue FROM cponmaster WHERE cponid = (?);")
    csrrxt = (cponid, )
    isolx.execute(csrr, csrrxt)
    rows = isolx.fetchall()
    values = ','.join(str(v) for v in rows)
    print("DNSS Coupon ", values)


# Single Voucher Data Fetcher For Billing
def cpon_ssinglefetch(cponid): 
    isol = sqlite3.connect('cponmgmtsys.db')
    isolx = isol.cursor()
    isol.row_factory = lambda cursor, row: row[0]
    csrr = ("SELECT cponid FROM cponmaster WHERE cponid = (?);")
    csrrxt = (cponid, )
    isolx.execute(csrr, csrrxt)
    rows = isolx.fetchall()
    values = ','.join(str(v) for v in rows)
    global sfetch_values
    sfetch_values = values[2:-3]

# Voucher Issuer
def cponissuer(cponid, cponlim, cponvalue):
    isol = sqlite3.connect('cponmgmtsys.db')
    isolx = isol.cursor()
    #try:
    str = "insert into cponmaster(cponid, cponlim, cponvalue) values('%s', '%s', '%s')"
    iox = (cponid, cponlim, cponvalue)
    isolx.execute(str % iox)
    isol.commit()
    cpon_singlefetch(cponid)
    print("DSNN: Coupon", cponid, "having discount %", cponvalue, "created for", cponlim, "times of usage.")
    #except sqlite3.IntegrityError:
        #print("DNSS voucher already exists")
        #cpon_singlefetch(cponid)

# Single Voucher Value Fetcher
def cpon_valfetch(cponid): 
    global valdock
    isol = sqlite3.connect('cponmgmtsys.db')
    isolx = isol.cursor()
    isol.row_factory = lambda cursor, row: row[0]
    csrr = ("SELECT cponvalue FROM cponmaster WHERE cponid = (?);")
    csrrxt = (cponid, )
    isolx.execute(csrr, csrrxt)
    rows = isolx.fetchall()
    values = ''.join(str(v) for v in rows)
    #print(values[1:-2])
    valdock = values[1:-2]
    print(valdock)

#Voucher Limit Data Fetcher
def cpon_limfetch(cponid): 
    isol = sqlite3.connect('cponmgmtsys.db')
    isolx = isol.cursor()
    isol.row_factory = lambda cursor, row: row[0]
    csrr = ("SELECT cponlim FROM cponmaster WHERE cponid = (?);")
    csrrxt = (cponid, )
    isolx.execute(csrr, csrrxt)
    rows = isolx.fetchall()
    values = ''.join(str(v) for v in rows)
    limx = values[1:-2]
    if limx == 0:
        print("DNSSexemption: Coupon no longer valid. ")
    else:
        pass

# Mass Voucher Listing Fetcher
def cpon_masterfetch():
    isol = sqlite3.connect(r'cponmgmtsys.db')
    isolx = isol.cursor()
    isolx.execute("SELECT DISTINCT cponid, cponlim FROM cponmaster")
    rows = isolx.fetchall()
    col_labels = ("Coupon ID: ", "Usage Limit Left")
    table(col_labels, rows)




# Customer System
# Customer Record Creator
def inserter(custt, custname, email):  #defining a function to input data into the SQL database's table
    con = sqlite3.connect(r'DBFA.db')
    conn = con.cursor()
    str = "insert into cust(custt, custname, email) values('%s', '%s', '%s')"
    io = (custt, custname, email)
    conn.execute(str % io)
    con.commit()
    print("Customer", custname, "registered in store directory")

# Customer Purchase Updater
def custcc(custid, custname, purchasecount, ptotalx):  #defining a function to input data into the SQL database's table
    global xon
    xon = sqlite3.connect(r'DBFA_CUSTCC.db')
    xbr7 = xon.cursor()
    str = "insert into custcc(custid, custname, purchasecount, ptotalx, points) values(?, ?, ?, ?, 0)"
    io = (custid, custname, purchasecount, ptotalx)
    xbr7.execute(str, io)
    xon.commit()
    xbr7.close()
    print("FJHG")

# Customer Purchase Updater
def updatescript(custid, pincrement, billiemaster):
    try:
        xon = sqlite3.connect('DBFA_CUSTCC.db')
        xbr7 = xon.cursor()
        # hidden prints here ig
        points = (billiemaster/100)*1
        updatexr = """UPDATE custcc SET purchasecount = purchasecount + 1 WHERE custid = ?"""
        updatexxr = """UPDATE custcc SET ptotalx = ptotalx + ? WHERE custid = ?"""
        updatexxxr = """UPDATE custcc SET points = points + ? WHERE custid = ?"""
        indicator = (custid, )
        xrindicator = (pincrement, custid)
        pindicator = (points, custid)
        xbr7.execute(updatexr, indicator)
        xbr7.execute(updatexxr, xrindicator)
        xbr7.execute(updatexxxr, pindicator)
        xon.commit()
        xbr7.close()
    except sqlite3.Error as error:
        pass


def pointfetch(custid):
    global lylpoints
    lylpoints = 0
    xon = sqlite3.connect('DBFA_CUSTCC.db')
    xbr7 = xon.cursor()
    findinx = "select points from custcc WHERE custid = ?"
    findinxx = (custid, )
    xbr7.execute(findinx, findinxx)
    arterxout = xbr7.fetchall()
    lylpoints = int((arterxout[0])[0])


def pointmassfetch():
    xon = sqlite3.connect('DBFA_CUSTCC.db')
    xbr7 = xon.cursor()
    findinx = "select DISTINCT points from custcc"
    xbr7.execute(findinx)
    rows = xbr7.fetchall()
    for row in rows:
        print(row[0])

def pointsuse(custid, deduct):
    xon = sqlite3.connect('DBFA_CUSTCC.db')
    xbr7 = xon.cursor()
    updatexxxr = """UPDATE custcc SET points = points - ? WHERE custid = ?"""
    pindicator = (deduct, custid)
    xbr7.execute(updatexxxr, pindicator)
    xon.commit()
    xbr7.close()

def emailfetch(custid):
    global custmail
    con = sqlite3.connect(r'DBFA.db')
    conn = con.cursor()
    findinx = "select DISTINCT email from cust WHERE custt = ?"
    findinxx = (custid, )
    conn.execute(findinx, findinxx)
    rows = conn.fetchall()
    custmail = (rows[0][0])

global custcheckindic

global custt

def custcheck(custt):
    global cccheck, lylpoints
    if custt in ("", " ", 0, None , "0"):
        lylpoints = 0

    cccheck = 0
    custcheckindic = 0
    con = sqlite3.connect(r'DBFA.db')
    conn = con.cursor()
    conn.execute("SELECT custt FROM cust WHERE custt = ?", (custt,))
    data = conn.fetchall()
    if len(data)==0:
        custcheckindic = 0
        print("Customer", custt, "NOT found. ")
        print("- No customer selected -")
        custt = 0
        print("Using unregistered customer account")
        cccheck = 0
    else:
        ccustcheckindic = 1
        cccheck = 0
        pass


# Customer Validity Checker
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

def saleslogger(custid, prodid, netpay):  #defining a function to input data into the SQL database's table
    sales = sqlite3.connect(r'dbfasales.db')
    salesx = sales.cursor()

    netprof = 0
    from datetime import date
    datex = date.today()

    profer = [2000, 4500, 5700, 2000, 2100, 1470, 300, 11000, 400, 2000, 100, 370, 450, 120, 50, 275, 649, 140, 50, 1050, 978, 150, 100, 320, 98, 75, 170, 60, 275, 90, 210, 780, 50, 35, 50, 30, 100, 8000, 9000, 1790]
    for i in prodid:
        netprof += profer[int(i)]

    salesx.execute("SELECT MAX(sno) FROM SALES")
    sno = (int(salesx.fetchall()[0][0]) + 1)

    prodidxs = ""
    for i in prodid:
        prodidxs += '%s'%i + ", "

    str = "insert into sales(sno, custid, prodid, net, prof, date) values(?, ?, ?, ?, ?, ?)"
    io = (sno, custid, prodidxs, netpay, netprof, datex)
    salesx.execute(str, io)
    sales.commit()
    print("Sales activity logged. ")


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






def floodscreen():
    image = cv2.imread("imagepx.png")
    cv2.imshow("Loading.... ", image)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()


def floodpay():
    import cv2 
    image = cv2.imread("qr-code.png")
    cv2.imshow("Pay With UPI", image)
    cv2.waitKey(150000)
    cv2.destroyAllWindows()


# Main Menu
# New Main Menu
def mainmenu(): #defining a function for the main menu
    from colorama import init, Fore, Back, Style #color-settings for the partner/sponsor adverts
    init(convert = True)
    # Count pending deliveries
    delcount = 0
    netprof = sqlite3.connect('recmaster.db')
    netprofx = netprof.cursor()
    netprofx.execute("SELECT netprof FROM recmasterx")
    rows = netprofx.fetchall()
    netproffetchx = []
    for i in rows:
        netproffetchx.append(i[0])
    print(" ")
    filedel = open('./DBFAdeliveries.txt', 'r+')
    for line in filedel:
        delcount+=1
    filedel.close()
    pro7d = salesdatefetch()
    protd = salestodayfetch()
    if delcount != 0:
        print("-------------------------------------------------------------------------------------------------------------------------")
        lener1 = "Profit earned in the last 7 days: " + '%s'%pro7d
        print(lener1 + (86-len(lener1))*" ", "Profit earned today: ", protd)
        #pro7d, (56-len(str(pro7d)))*" ", "DONNAGER 8.01 RC-2 Test Beta")
        print(Back.BLACK + Fore.MAGENTA+ "Number of pending deliveries: " + str(delcount) + " "  + "            DBFA User: " + os.getlogin() + "                          "+ dt_string + Fore.CYAN)
        print("-------------------------------------------------------------------------------------------------------------------------")
    else:
        print("DONNAGER 8.01 RC-2 Test Beta")
        print(Fore.BLACK + Back.CYAN + "No deliveries pending! " + Back.BLACK + Fore.CYAN)

    logox = (Fore.CYAN+'''       _____   ____    ____  ____   ____    Options:
      / /  // / /  \\  /___  /__||   /   /     1: Issue a Bill                          4: Auto-Generate Store Report 
     / /  // / /===| ///// ////||  /////      2: Manage Customers                      
    /_/__// /_/__ / /     /    || /__ /            a: Register a Customer              5: Start DBFA Backup&Switch
'''+Fore.MAGENTA+'''             The OG Store Manager'''+Fore.CYAN+'''                   b: Customer Registry                         
                                                    c: Customer Purchase Records       6: View Software License\n'''
+ '      A word from our partner: ' + Fore.BLACK + Back.CYAN + 'HOTEL? Trivago!' + Back.BLACK + Fore.CYAN + '''      d: Find a Customer                                
                                                    e: Export Records as CSV           7: Manage Deliveries
                                              3: Store Options:                        
                                                    a: Manage Stock                    8: Development Changelog
                                                    b: DBFA Stock Master                    
    - enter CIT code to view more options -         c: Manage Vouchers                 9: DBFA Settings
                                                    d: Product Listing
                                                    e: Sales Log                       10: Quit
                                                    f: Export Sales Data as CSV     ''')
    # To underline What would you like to do?::                                                                            
    print(logox)
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("DBFA Music Controls:: *prev* - << previous | *pause* - <|> pause/play | *next* - >> next                                 ")
    time.sleep(0.2)
    try:
        if spotify.current() not in ("", " ", [], (), None):
            print("Currently playing:", Fore.MAGENTA , spotify.current()[0], Fore.CYAN, "by ", Fore.MAGENTA, spotify.current()[1], Fore.CYAN)
        else:
            print(Fore.MAGENTA, "No music playing. Use Spotify to play your favourite music and control it via DBFA", Fore.CYAN)
    except Exception as e:
        print(Fore.MAGENTA, "No music playing. Use Spotify to play your favourite music and control it via DBFA", Fore.CYAN)
    print("-------------------------------------------------------------------------------------------------------------------------", Fore.MAGENTA)
    #underline_byte = b'\xcc\xb2'
    #underline = str(underline_byte,'utf-8')
    #for x in ("What would you like to do?"):
    #    if x.isspace() == False:
    #        print(x+underline,end='')
    #    else:
    #        print(x,end='')     
    print("What would you like to do?", Fore.WHITE)
    print()

global netpay

def xpayboxie():
    command = "cls"
    os.system(command)
    global xrt, payindic
    xrt = 0
    from colorama import init, Fore, Back, Style #color-settings for the partner/sponsor adverts
    print("Amount to pay: ", netpay)
    print("Payment methods available: ")
    print("1. Credit/ Debit Card")
    print("2. Digital Wallet")
    print("3. UPI")
    print("4. Cash")
    print("*exit* to cancel this billing cycle")
    time.sleep(0.5)
    paycheck = input("Pay with: ")
    print(Fore.LIGHTBLUE_EX + "-----------------" + Fore.WHITE)
    if paycheck == "1":
        payindic = "Paid with credit/ debit Card"
    elif paycheck == "2":
        payindic = "Paid with a digital wallet"
    elif paycheck == "3":
        payindic = "Paid with UPI"
        floodpay()
    elif paycheck == "4":
        payindic = "Paid with cash"
    elif paycheck == "exit":
        print("Cancelling this billing cycle")
        xrt = 1
    else:
        xpayboxie()

global netpay

# Payments Handler
def payboxie(custid, total):
    global custcheckindic
    if custt not in (0, "0", "", " ", None) and cccheck == 0:
        command = "cls"
        os.system(command)
        global payindic, netpay, redeemindic, lylpoints
        xrt = 0
        redeemindic = 0
        payindic = 0
        from colorama import init, Fore, Back, Style #color-settings for the partner/sponsor adverts
        print(Fore.LIGHTBLUE_EX + "-----------------" + Fore.WHITE)
        init(convert = True)
        print("Amount to be paid: ₹","%.2f" % total)
        print(Fore.LIGHTBLUE_EX + "-----------------" + Fore.WHITE)
        pointfetch(custid)
        if lylpoints != 0:
            print("You have loyalty points: ", lylpoints, "worth: ", lylpoints)
            time.sleep(0.5)
            pointscheck = input("Use points (y/n)? ")
            print(Fore.LIGHTBLUE_EX + "-----------------" + Fore.WHITE)
            if pointscheck == "y":
                if total > lylpoints:
                    redeemam = lylpoints
                else:
                    redeemam = total
                getOTP()
                emailfetch(custid)
                print("Please wait..")
                email = 'billing.dbfa@gmail.com'
                password = 'dbfaidlepass'
                send_to_email = custmail
                subject = 'Redeem your DBFA loyalty points'
                messageHTML = ('''
                <h1><span style="color: #496dd0">Redeem your DBFA loyalty points?</span></h1>
                <h6> </h6>
                <h4>You are recieving this mail as we've recieved a request to use the loyalty points on your account for a purchase with DBFA. If this isn't you, contact support at the earrliest.</h4>
                <h6> </h6>
                <h4>One-time password: <span style="color: #496dd0">''' + "%s"%otp + '''</span></h4>
                <h6> </h6>
                <h6>Points in your account: ''' + "%s"%lylpoints + '''</h6>
                <h6>Points that will be redeemed: ''' + "%s"%redeemam + '''</h6>
                <h6>Each DBFA point is worth ₹1</h6>
                <h6>This purchase will give you: ''' + "%s"%((billiemaster/100)*1) + ''' points</h6>
                <h6></h6>
                <h6></h6>
                <h6> </h6>
                <h6> </h6>
                <h6> </h6>
                <h5>When you share this OTP with a DBFA-store, you authorize us to use your loyalty points to discount your purchase.</h5>
                <h6>Do not share this OTP with any third party.</h6>
                <h6>DBFA or any of its affiliates will not be resposible in anyway for any implications this OTP or any part of it might have on anyone in any way.</h6>
                <h6>Offering these reward points does not benefit DBFA in any immediate manner.</h6>
                ''')
                messagePlain = 'DBFA Security'
                msg = MIMEMultipart('alternative')
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject
                # Attach both plain and HTML versions
                msg.attach(MIMEText(messagePlain, 'plain'))
                msg.attach(MIMEText(messageHTML, 'html'))
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                otpverif = input("Enter the OTP recieved on " + "%s"%custmail + ": ")
                if otpverif == otp:
                    if total > lylpoints:
                        total = total - lylpoints
                        pointsuse(custid, lylpoints)
                        print("New total: ", total)
                        time.sleep(2)
                        redeemindic = 1
                        netpay = total
                        print("Points redeemed worth: ", lylpoints)

                    else:
                        redeemindic = 1
                        netpay = total
                        pointsuse(custid, total)
                        time.sleep(0.3)
                        total = 0
                        print("Points redeemed worth: ", lylpoints)
                    time.sleep(0.3)
                    
                else:
                    print("Wrong OTP. (1) attempt(s) remaining")
                    time.sleep(0.2)
                    otpverif = input("Enter the OTP recieved on " + "%s"%custmail + ": ")
                    if otpverif == otp:
                        if total > lylpoints:
                            total = total - lylpoints
                            pointsuse(custid, lylpoints)
                            print("New total: ", total)
                            time.sleep(2)
                            redeemindic = 1
                            netpay = total
                            print("Points redeemed worth: ", lylpoints)
                        else:
                            netpay = 0
                            pointsuse(custid, total)
                            time.sleep(0.3)
                            total = 0
                            print("Points redeemed worth: ", lylpoints)
                    else:
                        print("Wrong OTP. (0) attempt(s) remaining")
                        time.sleep(0.2)
            elif pointscheck == "n":
                redeemindic = 0
                netpay = total
            else:
                pass
            time.sleep(1)
            os.system(command)
        else:
            netpay = total
        
    else:
        redeemindic = 0
        netpay = total
        redeemindic = 0
        lylpoints = 0
        netpay = total




def del2a():
    try:
        if os.path.exists(r'userblock.txt'):
            os.remove(r'userblock.txt')
        if os.path.exists(r'userblock.zconf'):
            os.remove(r'userblock.zconf')
    except PermissionError:
            pass
    print("Connecting to server..")  #SQL connection prompt
    time.sleep(0.4)  #for a seamless experience
    #conn.execute("select * from cust")
    #takes values from the SQL database
    conn = sqlite3.connect('DBFA.db')
    cursor = conn.cursor()
    cursor.execute("select * from cust")
    results = cursor.fetchall()
    idd = len(results)+1
    print("Registering customer with ID: ", idd)
    custname = input("Customer Name: ")
    email = input("Customer's E-mail ID: ")
    inserter(idd, custname, email) #argumental function to insert values into the SQL database
    nullvalue = 0
    custcc(idd, custname, nullvalue, nullvalue)
    print(" ")
    
    print("Customer ID", idd, "registered in directory.")
    print("---------------------------------------")
    print(" ")
    print(" ")
    #conn.close()
    time.sleep(1) #for a seamless experience


def del2b():
    try:
        if os.path.exists(r'userblock.txt'):
            os.remove(r'userblock.txt')
        if os.path.exists(r'userblock.zconf'):
            os.remove(r'userblock.zconf')
    except PermissionError:
            pass
    print()
    print("Connecting to server..")  #SQL connection prompt
    time.sleep(0.7) #for a seamless experience
    print("Registered customers are: ")
    #Re-writing to refresh connection
    conn = sqlite3.connect('DBFA.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM cust")
    rows = cur.fetchall()
    col_labels = ("ID", "Customer NAME", "EMAIL")
    table(col_labels, rows)
    toaster.show_toast("DNSS QuickSync", "Database acessed", duration = 2)
    #takes values from the SQL database
    '''
    while row is not None:
        print(row)
        #row = conn.fetchone()
    '''
    
    conn.close()
    conn.close()
    print()
    print()
    time.sleep(2) #delay for easy-table viewing
    

def del2c():
    try:
        if os.path.exists(r'userblock.txt'):
            os.remove(r'userblock.txt')
        if os.path.exists(r'userblock.zconf'):
            os.remove(r'userblock.zconf')
    except PermissionError:
            pass
    xon = sqlite3.connect(r'DBFA_CUSTCC.db')
    xbr7 = xon.cursor()
    xbr7.execute("SELECT * FROM custcc")
    l = xbr7.fetchall()
    print("\nCustomer Purchase Records: ")

    import pandas as pd

    flat_list = []
    print("---------------------------------------------------------------")
    for sublist in l:
        flat_list.append(sublist)
    mydf = pd.DataFrame(flat_list, columns=['Customer ID', 'Name', 'Purchases Made', 'Total', 'Loyalty Points'])
    mydf.pivot(index='Customer ID', columns='Purchases Made', values='Total').fillna(value='-')
    print(mydf)
    print("---------------------------------------------------------------")
    time.sleep(2)
    
    '''
    for row in rows:
        print(row)
        print(" ")
    '''
    xbr7.close()
    toaster.show_toast("DFBA QuickSync", "Database acessed", duration = 0.5) 



def del2d():
    try:
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
            srtx = "%"
            for i in searchcon:
                srtx += '%s'%i+"%"
            conn.execute("SELECT custt FROM cust WHERE custname LIKE ?", ((srtx), ))
            searchdata = conn.fetchall()
            if len(searchdata) != 0:
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
            else:
                print("Customer not found.")
    except:
        print("Error encountered.  ")




def del2e():
    import sqlite3 as sql
    import os
    import csv
    from sqlite3 import Error

    try:
        csvex=sql.connect(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\DBFA.db')
        cursor = csvex.cursor()
        cursor.execute("select * from cust")
        print("Fetching data from database - I...")
        with open("DBFAcustrec.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter="\t")
            csv_writer.writerow([i[0] for i in cursor.description])
            csv_writer.writerows(cursor)
            csvexx=sql.connect(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\DBFA_CUSTCC.db')
            print("Fetching data from database - II...")
            cursorx = csvexx.cursor()
            cursorx.execute("select * from custcc")
            csv_writer = csv.writer(csv_file, delimiter="\t")
            csv_writer.writerow([i[0] for i in cursorx.description])
            csv_writer.writerows(cursorx)    
        dirpath = os.getcwd() + "/DBFAcustrec.csv"
        print("Data exported Successfully into {}".format(dirpath))
        time.sleep(2)
        os.startfile(r"DBFAcustrec.csv")

    except Error as e:
        print(e)

    finally:
        csvex.close()



def del3a():
    decsfacter = str(input("Enter 'a' to VIEW STOCK, 'b' to ADD STOCK and 'c' to ENFORCE MASS STOCK: "))
    if decsfacter == "a":
        ssxsuperfetch()
    elif decsfacter == "b":
        objid = int(input("Enter the product ID to add stock for: "))
        stockincrement = int(input("Enter the amount of stock to be added: "))
        ssxupdatescript(stockincrement, objid)
        print("Stock updated by", stockincrement, "for product ID:", objid)
    elif decsfacter == "c":
        ggrtrr = int(input("Enter stock to universally enforce: "))
        massmaintainer(ggrtrr)


def del3b():
    print("-------- DBFA Stock Master v1 ---------")
    print(" ")
    time.sleep(1)
    print("a: Order New Stock")
    print("b: Update Delivery Status")
    print("c: MASS - Fetch Current Status")
    print("d: INDVL - Fetch Current Status")
    print("e: View Vendor Details")
    print("f: Contact Vendor")
    print("g: Edit Vendor Contact")
    print("h: Modify Low-Stock Warning Bar")
    stkmaster = input("Select:: ")
    if stkmaster in ("a", "A"):
        idquery = int(input("Enter the product ID: "))
        qtyquery = int(input("Enter the amount to order: "))
        orderstock(idquery, qtyquery)
        print("\n--------------------------------------------------------")
    elif stkmaster in ("b", "B"):
        idquery = int(input("Product ID of the product recieved: "))
        qtyquery = int(input("Quantity recieved: "))
        delivered(qtyquery, idquery)
        ssxupdatescript(qtyquery, idquery)
        print("\nChanges made in all related databases. \n")
        print("\n--------------------------------------------------------")
    elif stkmaster in ("c", "C"):
        delstatmass()
        print("\n--------------------------------------------------------")
    elif stkmaster in ("d", "D"):
        idquery = int(input("Product ID to locate: "))
        delstatindvl(idquery)
        print("\n--------------------------------------------------------")
    elif stkmaster in ("e", "E"):
        idquery = int(input("Product ID to get vendor details for: "))
        vendorfetch(idquery)
        print("\n--------------------------------------------------------")
    elif stkmaster in ("f", "F"):
        idquery = int(input("Product ID to contact vendor for: "))
        vendorcontact(idquery)
        print("\n--------------------------------------------------------")
    elif stkmaster in ("g", "G"):
        print("-- Change Vendor Contact --")
        time.sleep(0.5)
        try:
            prodidvendc = int(input("Enter product ID to change vendor contact for: "))
            if prodidvendc > 40:
                print("Please enter a valid product ID")
                prodidvendc = input("Enter product ID to change vendor contact for: ")

        except:
            print("Please enter a valid product ID")
            time.sleep(0.3)
            prodidvendc = input("Enter product ID to change vendor contact for: ")
            if prodidvendc > 40:
                print("Please enter a valid product ID")
                prodidvendc = input("Enter product ID to change vendor contact for: ")
        while(1):
            vendorchange = input("Enter the new E-Mail ID: ")
            if "@" in vendorchange:
                if "." in vendorchange:
                    st = sqlite3.connect(r'DBFA_vend.db')
                    stx = st.cursor()
                    stx.execute("""UPDATE stock SET vendcont = ? WHERE prodid = ?""", (vendorchange, prodidvendc,))
                    st.commit()
                    print("Vendor contact changed for product ID: ", prodidvendc)
                    time.sleep(1.5)
                    break
                    mainmenu()
                else:
                    print("Please enter a valid E-Mail format! ")
            else:
                print("Please enter a valid E-Mail format! ")

    elif stkmaster in ("h", "H"):
        idquery = int(input("Product ID to alter bar for: "))
        lowbarmodif(idquery)
        print("\n--------------------------------------------------------")
    else:
        print("Please select a valid option! ")
        print("\n--------------------------------------------------------")
        time.sleep(1)
        mainmenu()



def del3c():
    print("Enter '1' to generate a voucher; ")
    descx = int(input("'2' to view generated vouchers: "))
    if descx == 1:
        print("DNSS CouponMaster: Issuer")
        print("NOTE: Reusing existing coupon codes may result in overwritten data.")
        cponid = input("Coupon ID: ")
        cponlim = input("Number of times to allow coupon usage: ")
        cponvalue = input("Coupon discount percentage: ")
        cponissuer(cponid, cponlim, cponvalue)
        time.sleep(0.4)
    elif descx == 2:
        print("DNSS CouponMaster: Viewer")
        cpon_masterfetch()
        time.sleep(0.4)



def del3d():
    try:
        if os.path.exists(r'userblock.txt'):
            os.remove(r'userblock.txt')
        if os.path.exists(r'userblock.zconf'):
            os.remove(r'userblock.zconf')
    except PermissionError:
            pass
    print("Store listing (as per updated records): ")
    print(tabulate(tablx, headers = titlex, floatfmt = ".4f"))



def del3e():
    try:
        if os.path.exists(r'userblock.txt'):
            os.remove(r'userblock.txt')
        if os.path.exists(r'userblock.zconf'):
            os.remove(r'userblock.zconf')
    except PermissionError:
            pass
    #password verification as sales record is not to be shown to all;
    print(" - Echo-supressed input - ")
    passw = getpass.getpass(prompt='Enter root password to view store activity registry: ', stream=None)
    if passw == "root":
            time.sleep(1) #for a seamless experience
            print("Hold on, moneybags.")
            with HiddenPrints():
                try:
                    sender = telegram_bot_sendtext(dt_string + "\n" + "Registry files and sales DB records accessed - DBFA SECURITY")
                    print(sender)
                except Exception:
                    pass
            time.sleep(0.2) #for a seamless experience 
            print()
            sales = sqlite3.connect(r'dbfasales.db')
            salesx = sales.cursor()
            salesx.execute("SELECT * FROM sales")
            salesrows = salesx.fetchall()
            col_labels = ("SalesID", "CustomerID", "Product Codes Purchased", "Total", "Profit Earned", "Date of Purchase")
            table(col_labels, salesrows)
            toaster.show_toast("DNSS QuickSync", "Database acessed", duration = 2)
            time.sleep(1.4) #for a seamless experience
            os.startfile('registry.txt') #to open the external notepad application
    else:
        print("Ehh that'd be wrong, sneaky-hat. Try again: ")
        print(" ")
        print(" - Echo-supressed input - ")
        passw = getpass.getpass(prompt='Enter root password to view store activity registry: ', stream=None)
        if passw == "root":
                time.sleep(1) #for a seamless experience
                print("Hold on, moneybags.")
                with HiddenPrints():
                    try:
                        sender = telegram_bot_sendtext(dt_string + "\n" + "Registry files and sales DB records accessed accessed - DBFA SECURITY: ATTEMPT 02")
                        print(sender)
                    except Exception:
                        pass
                print("There ya go:: ")
                print()
                sales = sqlite3.connect(r'dbfasales.db')
                salesx = sales.cursor()
                salesx.execute("SELECT * FROM sales")
                salesrows = salesx.fetchall()
                col_labels = ("SalesID", "CustomerID", "Product Codes Purchased", "Total", "Profit Earned", "Date of Purchase")
                table(col_labels, salesrows)
                toaster.show_toast("DNSS QuickSync", "Database acessed", duration = 2)
                time.sleep(0.6) #for a seamless experience
                # print(logger.read())
                # print()
                # print("Opening sales log externally now. ")
                time.sleep(1.4) #for a seamless experience
                os.startfile('registry.txt')
        else:
            with HiddenPrints():
                try:
                    sender = telegram_bot_sendtext(dt_string + "\n" + "[ACCESS DENIED!!] - Registry file  - DBFA SECURITY [ACCESS DENIED!!]")
                    print(sender)
                except Exception:
                    pass
            print("Multiple Unsuccesfull Attempts Detected. Re-run the program to login now. ")
            logger.write("(MULTIPLE ATTEMPTS!): Log file access attempt - AUTHORIZATION FAILED!!! \n")
            time.sleep(1.4) #for a seamless experience
            print()
            print()




def del3f():
    import sqlite3 as sql
    import os
    import csv
    from sqlite3 import Error

    try:
        csvex=sql.connect(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\recmaster.db')
        print("Exporting sales data to CSV....")
        cursor = csvex.cursor()
        cursor.execute("select * from recmasterx")
        with open("DBFAstorerec.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter="\t")
            csv_writer.writerow([i[0] for i in cursor.description])
            csv_writer.writerows(cursor)

        dirpath = os.getcwd() + "/DBFAcustrec.csv"
        print("Data exported Successfully into {}".format(dirpath))
        time.sleep(2)
        os.startfile(r"DBFAcustrec.csv")

    except Error as e:
        print(e)

    finally:
        pass




print("-----------------------------------------------------------------------------------------------------")

# Store listing::
data = {"1":40000, "2":55000, "3":67000, "4":25000, "5":21000, "6":14000, "7":13000, "8":220000, "9":4500, "10":17000, "11":1200, "12":3700, "13":4500, "14":2200, "15":700, "16":2750, "17":6499, "18":1499, "19":799, "20":27000, "21":6750, "22":2100, "23":1199, "24":3210, "25":989, "26":750, "27":1700, "28":600, "29":2175, "30":890, "31":2100, "32":7158, "33":597, "34":347, "35":500, "36":300, "37":1097, "38":80000, "39":87900, "40":23790}
namie = {"1":"TV 4K OLED 50", "2":"TV FHD OLED 50", "3":"8K QLED 80", "4":"Redmi K20 PRO", "5":"Redmi K20", "6":"Redmi Note 8 PRO", "7":"POCOPHONE F1", "8":"Mi MIX ALPHA", "9":"Wireless Headphones", "10":"Noise-Cancelling Wireless Headphones", "11":"Essentials Headphones", "12":"Gaming Headphones", "13":"Truly-Wireless Eadphones", "14":"Neckband-Style Wireless Earphones", "15":"Essentials Earphones", "16":"Gaming Earphones", "17":"30W Bluetooth Speakers", "18":"10W Bluetooth Speakers", "19":"Essentials Bluetooth Speaker", "20":"ULTRA Home Theatre", "21":"Essentials Home Theatre", "22":"  Wired Speaker - 5.1", "23":"  Essentials Wired Speaker - STEREO", "24":"Tactical Power Bank 30000mah", "25":"Essentials Power Bank 10000mah", "26":"Essentials Mouse", "27":"Logitech G604 LightSpeed Wireless", "28":"Tactical Essentials Keyboard", "29":"DROP GS21k RGB Gaming Keyboard", "30":"Polowski Tactical Flashlight", "31":"OneFiber Wi-Fi Router AX17", "32":"Mijia Mesh Wi-Fi Router", "33":"lapcare 120W Laptop Adapter", "34":"lapcare 60W Laptop Adapter", "35":"Spigen Phone Case(s)", "36":"Essentials Phone Charger 10W", "37":"HyperPower Type-C Gallium-Nitride Charger 100W", "38":"ASUS Zephyrus G14 Gaming Laptop", "39":"L XPS 15 Content Creator's Laptop", "40":"Hewlett-Packard Essential's Student's Laptop (Chromebook)"}
namiex = ["TV 4K OLED 50", "TV FHD OLED 50", "8K QLED 80", "Redmi K20 PRO", "Redmi K20", "Redmi Note 9 PRO", "POCOPHONE F1", "Mi MIX ALPHA", "Wireless Headphones", "Noise-Cancelling Wireless Headphones", "Essentials Headphones", "Gaming Headphones", "Truly-Wireless Eadphones", "Neckband-Style Wireless Earphones", "Essentials Earphones", "Gaming Earphones", "30W Bluetooth Speakers", "20W Bluetooth Speakers", "Essentials Bluetooth Speaker", "BOSE QC35", "Essentials Home Theatre", "Wired Speaker - 5.1", "Essentials Wired Speaker - STEREO", "Tactical Series Power Bank 30000mah", "Essentials Power Bank 10000mah", "Essentials Mouse", "Logitech G604 LightSpeed Wireless", "Tactical Essentials Keyboard", "DROP GS21k RGB Gaming Keyboard", "Polowski Tactical Flashlight", "OneFiber Wi-Fi Router AX7", "Mijia Mesh Wi-Fi Router", "lapcare 45W Laptop Adapter", "lapcare 60W Laptop Adapter","Spigen Phone Case(s)", "Essentials Phone Charger 15W", "HyperPower Type-C Gallium-Nitride Charger 120W", "ASUS Zephyrus G4 Gaming Laptop", "DELL XPS 5 Content Creator's Laptop", "Hewlett-Packard Essential's Student's Laptop (Chromebook)"]
datax = [40000, 55000, 67000, 25000, 21000, 14000, 3000, 220000, 4500, 17000, 1200, 3700, 4500, 2200, 700, 2750, 6499, 1499, 799, 27000, 6750, 2100, 1199, 3210, 989, 750, 1700, 600, 2175, 890, 2100, 7158, 597, 347, 500, 300, 1097, 80000, 87900, 23790]

# dataxr is currently redundant
dataxr = []
for i in datax:
    i = "₹" + '%d' % i
    dataxr.append(i)
tablx = zip(namiex, dataxr)
titlex = ["Product:", "Pricing:"]

print('''
DBFA Billing Framework 7 [Bellaire] (stable)
<GNU Public License> Copyright (C) 2020 Pranav Balaji and Sushant Gupta
View the license file in the installation dir for more info.
\n\n
Fetching Windows login details..
Fetching Windows login details....
\n''')

logoprintxrt()
time.sleep(0.3)
command = "cls"
os.system(command)
 

#vs2
from datetime import datetime  #for reporting the billing time and date
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")  #datetime object containing current date and time
logger = open(r"registry.txt", "a+")  #Opening / creating (if it doesn't exist already) the .txt record file
logger.write("----------------------------------------- \n")
logger.write('ed')
logger.write("\n")
logger.write("Automated Store Registry:\n")


floodscreen() #comment to disable boot-flash screen
from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("DFBA System","Read documentation prior to use.", duration = 1)
print("Heyy there,", os.getlogin()) #enable parts in the auth script to enable user detection
time.sleep(0.5)
if redflag == 0:
    logger.write("Auth bypass - registering for security") 
    time.sleep(1)
    print("------- !!!!!!! -------")
    print("We highly value the security of our code and our customers.")
    toaster.show_toast("DBFA Security","Terminating Session!")
    print("It has been detected that you have bypassed the login process.")
    time.sleep(1)
    print("Please obtain a genuine version of this program and/ or provide proper authenication.")
    time.sleep(1)
    print("The program shall now exit. Error code:013")
    time.sleep(2)
    print("------------------------------------------")
    time.sleep(5)
    exit()


# Main Program Starts Here
while(1): #while (always) true
    mainmenu() #mainmenu
    writer = ""
    telethon = ""
    time.sleep(0.037)  #for a seamless experience
    decfac = input("Select option: ")

    #DBFA Music Controls v1.2
    #All possible case-combinations; found using recursion
    if decfac in ('prev', 'preV', 'prEv', 'prEV', 'pRev', 'pReV', 'pREv', 'pREV', 'Prev', 'PreV', 'PrEv', 'PrEV', 'PRev', 'PReV', 'PREv', 'PREV'):
        try:
            spotilib.previous()
        except Exception as e:
            pass
    elif decfac in ('pause', 'pausE', 'pauSe', 'pauSE', 'paUse', 'paUsE', 'paUSe', 'paUSE', 'pAuse', 'pAusE', 'pAuSe', 'pAuSE', 'pAUse', 'pAUsE', 'pAUSe', 'pAUSE', 'Pause', 'PausE', 'PauSe', 'PauSE', 'PaUse', 'PaUsE', 'PaUSe', 'PaUSE', 'PAuse', 'PAusE', 'PAuSe', 'PAuSE', 'PAUse', 'PAUsE', 'PAUSe', 'PAUSE'):
        try:
            spotilib.pause()
        except Exception as e:
            pass

    elif decfac in ('next', 'nexT', 'neXt', 'neXT', 'nExt', 'nExT', 'nEXt', 'nEXT', 'Next', 'NexT', 'NeXt', 'NeXT', 'NExt', 'NExT', 'NEXt', 'NEXT'):
        try:
            spotilib.next()
        except Exception as e:
            pass

    #Billing Mode
    elif decfac == "1":
        print()
        try:
            if os.path.exists(r'userblock.txt'):
                os.remove(r'userblock.txt')
            if os.path.exists(r'userblock.zconf'):
                os.remove(r'userblock.zconf')
        except PermissionError:
                pass
        print("--- BIlling ---")
        print()
        custt = input("Customer ID (optional): ")
        if custt in ("0", 0, "", " "):
            print("Unregistered Customer")
            custt = "0"
            custcheck(custt)
            cccheck = 0
        try:
            if (cust_listfetch(int(custt))) == 1:
                print("Customer found")
                custcheck(custt)
            else:
                print("Unregistered Customer")
                cccheck = 0
        except:
            custt = "0"
            print("Unregistered Customer")

        #print(cccheck)
        logger.write("-----------------  ") #writing to log file
        logger.write("Cust. ID: \n")
        logger.write(custt)
        logger.write("  \n")
        logger.write("Date and time: \n") #including the date and time of billing (as taken from the system)
        logger.write(dt_string)
        logger.write(" \n")
        abcd1 = 1
        infetch()
        purcheck = ""
        profer = []
        time.sleep(0.3) #for a seamless experience
        telethon = "DBFA Billing System" + "\n" + dt_string + "\n" + "Customer: " + custt + "\n" + "Invoice ID:" + '%s'%inval
        writer = writer + "DBFA Billing Framework" + "\n" + "One-stop solution for all your billing needs!" + "\n" + "\n" + "Billing time: " + dt_string + "\n" + "Customer ID: " + custt + "\n" + "-----------------------------" + "\n" + "\n"
        global billiemaster
        billiemaster = 0 #variable for totalling the price
        time.sleep(0.0247) #for a seamless experience
        afac = 0
        while(1):
            item = input("Enter product code: ")
            if item == "0":
                break
            elif item in data:
                ssxstockmaster(item)
                if ssxvarscheck == 1:
                    billiemaster+=data[item]
                    print("Purchased: ", namie[item], " for: ", data[item])
                    repupdate(item)
                    lenxr = len(namie[item])
                    costlenxr = len(str(data[item]))        
                    cj = 10 - costlenxr
                    pi = 60 - lenxr
                    idlerxx = namie[item] + " "*pi + "₹"+'%d'%data[item] + " "*cj + "1 qty. ~"
                    purcheck += idlerxx
                    print("---")
                    priceprod = "₹" + '%d' % data[item]
                    logger.write("Appending product to order: \n")  #writing to file
                    profer.append(item)
                    logger.write(namie[item])
                    ssxstockmaintainer(item)
                    logger.write(" \n")
                    writer = writer + "\n Purchased: " + "\n" + namie[item] + "\n" + priceprod + "\n"
                    afac+=1
                else:
                    print("Product currently out-of-stock. The inconvenience is regretted..\n")
                    print("---")
                    continue
            else:
                print("Product not found. Please retry ")
                print("---")

        #tax = int(input("Enter the net tax %: "))  #comment and uncomment tkinter lines to use GUI-based input
        time.sleep(0.15)  #for a seamless experience
        try:
            cponid = str(input("Enter voucher code (if any): "))
        except (EOFError, ValueError):
            pass                   #When no input is given by the user, control moves to this section as "EOFError or End Of File Error is detected"
        if cponid != "":
            cpon_limfetch(cponid)
            print("")
            print("----")
            cpon_valfetch(cponid)
            discount = int(valdock)
            #print(valdock)
            idler = "\nUsed DNSS voucher:\n" + str(cponid) + "\n \n"
            writer = writer + idler
            telethon = telethon + idler
            cponuse(cponid)
        else:
            try:
                discount = int(input("Enter discount % (if any): "))
            except:
                discount = 0
        print(discount, "% net discount")
        time.sleep(0.15)  #for a seamless experience
        print("-----------------")
        time.sleep(0.15)  #for a seamless experience
        tota = ((billiemaster)-(((discount)/100)*billiemaster))
        global total
        total = (tota + ((tota/100)*18))
        if total != 0:
            discountx = '%d' % discount
            telethon = telethon + "\n" + "Tax amount: 18%" + "\n"  + "Discount: " + discountx + "%" + "\n" + "\n"
            writer = writer + "\n" + "\n" + "-----------------------------" + "\n" + "Tax amount: 18%"  + "\n"  + discountx + "\n"  + "\n" 
            delxfac = input("Enter *d* for delivery; skip for in-store purchase: ")
            if delxfac != "d":
                payboxie(custt, total)
                xpayboxie()
            else:
                # Add a delivery
                print("---- DBFA Deliveries ----")
                delname = input("Customer's Name: ")
                time.sleep(0.1)
                print("Customer's Address:")
                def getaddress():
                    print("         Enter/paste the address. Press Ctrl-Z ( windows ) to save it.")
                    contents = []
                    while True:
                        try:
                            line = input()
                        except EOFError:
                            break
                        contents.append(line)
                    address = ""
                    for i in contents:
                        address += i+", "
                    return address
                addressx = getaddress()
                print("Address entered: ", addressx)
                addressfac = input("Confirm address or change? (y/n): ")
                if addressfac == "y":
                    # Count pending deliveries
                    delcount = 0
                    filedel = open('./DBFAdeliveries.txt', 'r')
                    for line in filedel:
                        delcount+=1
                    filedel = open('./DBFAdeliveries.txt', 'a+')
                    filedel.write("\ndel"+str(delcount+1) + "    " + addressx)
                    filedel.close()
                if addressfac == "n":
                    getaddress()
                elif addressfac not in ("y", "n"):
                    print("Invalid option! ")
                    pass
                time.sleep(0.5)
                time.sleep(0.5)
                sfetch_values = ""
                redeemindic = 0
                writer += "\n\nDBFA Delivery\n\n"
                payindic = "DBFA Delivery: PAY ON DELIVERY"
                print("-----DBFA Delivery Ticket-----")
                print("Customer: ", delname)
                print("Delivery Address: ", addressx)
                print("------------------------------")
                telethon += "\n\nDBFA Delivery\n\n"
                time.sleep(0.5)    
                print("Deliveries only support pay-on-delivery.")
                time.sleep(0.5)
                xrt = 0
                netpay = total
                lylpoints = 0

            if xrt == 1:
                writer = writer + "----------------- BILLING CYCLE CANCELLED -------------------"    
                break
            else:
                rupeesymbol = "₹".encode("utf-8")
                if delxfac != "d":
                    saleslogger(custt, profer, netpay)
                else:
                    saleslogger(custt, profer, total)
                inmaintainer()
                #infetch()
                print("\n\n--------------------------------------------------------------------------------")
                print("Invoice ID: ", inval, "| Time: ",dt_string, "| No. of items: ", afac)
                print(payindic)
                print("--------------------------------------------------------------------------------")
                printobj = purcheck.split("~")
                for i in printobj:
                    print(i)
                print("--------------------------------------------------------------------------------")
                print("Sub total        : ₹",billiemaster)
                cpon_ssinglefetch(cponid)
                if sfetch_values not in (None, " ", ""):
                    print("Voucher used     :",sfetch_values)
                discountstr = "Discount "+"("+'%d'%discount+"%)    :"
                print(discountstr, "₹","%.2f" % (((discount)/100)*billiemaster))
                print("IGST             : ₹","%.2f" % ((9/100)*billiemaster))
                print("CGST             : ₹","%.2f" % ((9/100)*billiemaster))
                if redeemindic == 1:
                    print("Redeemed loyalty points worth: ₹",lylpoints)
                print("--------------------------------------------------------------------------------")
                print("Amount to be paid: ₹","%.2f" % netpay)
                print("--------------------------------------------------------------------------------")
                toaster.show_toast("DFBA Billing:  Total billed for-",str(total), duration = 1)
                logger.write("Total amount billed for: \n") #writing to file
                if custt in ("", " ", 0, None) and cccheck == 0:
                    pass
                else:
                    writer += "Used DBFA loyalty points worth: " + '%s'%lylpoints + "\n"
                #regin.write("NET TOTAL: \n") #writing to file
                telethon = telethon + "NET TOTAL: \n" + "₹" + str(netpay) + "\n" 
                writer = writer + "NET TOTAL: \n" + str(netpay) + "\n" 
                logger.write(str(total))
                logger.write("\n")
                #regin.write(str(total))
                #regin.write("\n")
                updatescript(custt, total, billiemaster) #adds billed amount to the customer's record
                abcd1+=1
                afac+=1
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")  #datetime object containing current date and time
                daterey = (dt_string.replace("/","")).replace(":", "")
                namer = 'DBFAinvid'+'%s'%inval+"-"+daterey+'.pdf'
                can = SimpleDocTemplate(namer, pagesize=A4,
                                        rightMargin=2*cm,leftMargin=2*cm,
                                        topMargin=2*cm,bottomMargin=2*cm)
                #can.setFont("MiLanProVF", 24)
                can.build([Paragraph(writer.replace("\n", "<br />"), getSampleStyleSheet()['Normal']),])

                import shutil
                source = namer
                destination = r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\Generated_invoices'
                dest = shutil.move(source, destination)  
                time.sleep(1.5) #for a seamless experience


                if custt not in ("", " ", 0, "0") and cccheck == 0:
                    emailfetch(custt)
                    print("Please wait..")
                    fromaddr = "billing.dbfa@gmail.com"
                    toaddr = custmail
                    msg = MIMEMultipart() 
                    msg['From'] = fromaddr 
                    msg['To'] = toaddr 
                    msg['Subject'] = "Your DBFA Purchase Invoice"
                    body = """Thanks for making your purchase at DBFA!\n\nPlease find your invoice attached herewith.\n\nRegards\nThe DBFA Team"""
                    msg.attach(MIMEText(body, 'plain')) 
                    filename = namer
                    attachment = open(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\\Generated_invoices\\'+'%s'%namer, "rb") 
                    attac= MIMEBase('application', 'octet-stream') 
                    attac.set_payload((attachment).read()) 
                    encoders.encode_base64(attac) 
                    attac.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
                    msg.attach(attac) 
                    email = smtplib.SMTP('smtp.gmail.com', 587)  
                    email.starttls() 
                    email.login(fromaddr, "dbfaidlepass") 
                    message = msg.as_string() 
                    email.sendmail(fromaddr, toaddr, message) 
                    print("Invoice mailed. ")
                    print("-------------------------------------------------------------------------\n\n")
                #regin.close()
                with HiddenPrints():
                    try:
                        sender = telegram_bot_sendtext(telethon)
                        print(sender)
                    except Exception:
                        pass
                        
                print()

        else:
            print("\n\n-------------------------------------------------------------------------")
            print("No purchase made.")
            print("-------------------------------------------------------------------------")
            print("Amount           : ₹",billiemaster)
            print("-------------------------------------------------------------------------")
            print("Amount to be paid: ₹","%.2f" % total)
            print("-------------------------------------------------------------------------")
            toaster.show_toast("DBFA: No purchase made  ",str(total), duration = 1)
            logger.write("Billing cancelled: Reason: Net amount null\n") #writing to file
            #regin.write("NET TOTAL: \n") #writing to file
            telethon = telethon + "Billing cancelled. Net amount null." + "\n" 
            writer = writer + "BILLING CALCELLED. No purchase made." + "\n" 
            logger.write(str(total))
            logger.write("\n")
            abcd1+=1
            afac+=1
            now = datetime.now()

            #regin.close()
            with HiddenPrints():
                try:
                    sender = telegram_bot_sendtext(telethon)
                    print(sender)
                except Exception:
                    pass


    #Manage Customers
    elif decfac == "2":
        print("Select: ")
        print("    a: Register a Customer ")
        print("    b: Customer Registry ")
        print("    c: Customer Purchase Records ")    
        print("    d: Find a Customer ")
        print("    e: Export Records as CSV \n")
        selected = input("What would you like to do? ")
        print("\n")
        if selected in ("a", "A"):
            del2a()
            logger.write("--------------------------------------- \n")
            logger.write("  \n")
            logger.write("Date and time: ") #including the date and time of billing (as taken from the system)
            logger.write(dt_string)
            logger.write(" \n")
            logger.write("New customer registered: ")
            x = " custname: " + custname + " custemail: " + email + "\n"
            logger.write(x)
            logger.write("--------------------------------------- \n")

        if selected in ("b", "B"):
            del2b()
            logger.write("--------------------------------------- \n")
            logger.write("  \n")
            logger.write("Date and time: ") #including the date and time of billing (as taken from the system)
            logger.write(dt_string)
            logger.write(" \n")
            logger.write("Customer registry accessed! \n")
            logger.write("--------------------------------------- \n")

        if selected in ("c", "C"):
            del2c()
            logger.write("--------------------------------------- \n")
            logger.write("\nDBFA Customer Purchase Records accessed! \n")

        elif selected in ("d", "D"):
            del2d()
            logger.write("--------------------------------------- \n")
            logger.write("\nCustomer search used. \n")

        elif selected in ("e", "E"):
            del2e()
            logger.write("\n\n--------------------------------------- \n")
            logger.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n")
            logger.write("Customer data exported to CSV! ")
            with HiddenPrints():
                try:
                    sender = telegram_bot_sendtext(dt_string + "\n" + "Sales data exported to CSV- REDFLAG Urgent Security Notice!")
                    print(sender)
                except Exception:
                    pass
            logger.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n")
            logger.write("--------------------------------------- \n\n\n")

        elif selected not in ("a", "b", "c", "d", "e", "A", "B", "C", "D", "E"):
            print("Please chose a valid option!")
            time.sleep(1)

    #Store Options:
    elif decfac == "3":
        print("Select: ")
        print("    a: Manage Stock ")
        print("    b: DBFA Stock Master ")
        print("    c: Manage Vouchers ")
        print("    d: Product Listing ")
        print("    e: Sales Log ")
        print("    f: Export Sales Data as CSV \n")
        storeselected = input("What would you like to do? ")
        print("\n")

        if storeselected in ("a", "A"):
            del3a()
            
        elif storeselected in ("b", "B"):
            del3b()

        elif storeselected in ("c", "C"):
            del3c()

        elif storeselected in ("d", "D"):
            del3d()            

        elif storeselected in ("e", "E"):
            del3e()
            logger.write("\n--------------------------------------- \n")
            logger.write("Sales log accessed! ")

        elif storeselected in ("f", "F"):
            del3f()
            logger.write("\n\n--------------------------------------- \n")
            logger.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n")
            with HiddenPrints():
                try:
                    sender = telegram_bot_sendtext(dt_string + "\n" + "Customer data exported to CSV- REDFLAG Urgent Security Notice!")
                    print(sender)
                except Exception:
                    pass
            logger.write("Sales data exported to CSV! ")
            logger.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n")
            logger.write("--------------------------------------- \n\n\n")

        elif storeselected not in ("a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"):
            print("Please select a valid option! ")
            time.sleep(1)
            mainmenu()



    #Reports
    elif decfac == "4":
        command = "cls"
        os.system(command)
        print("-- Generating store report --")
        repstockfetch()
        print("Please wait...")
        repdatafetch()
        findMaximum = "select max(prodsales) from recmasterx"
        recx.execute(findMaximum)
        # Print the maximum score
        netr = recx.fetchone()[0]
        findin = "select prodid, prodname, prodprofit, prodsales, netprof from recmasterx WHERE prodsales = ?"
        arterx = (str(int(netr)),)
        recx.execute(findin, arterx)
        arterxout = recx.fetchall()

        findMaximumProf = "select max(netprof) from recmasterx"
        recx.execute(findMaximumProf)
        xnetr = recx.fetchone()[0]
        findin = "select prodid, prodname, prodprofit, prodsales, netprof from recmasterx WHERE netprof = ?"
        xarterx = str(int(xnetr))
        xxarterx = (xarterx,)
        recx.execute(findin, xxarterx)
        xarterxout = recx.fetchall()

        isol = sqlite3.connect(r'DBFA_vend.db')
        isolx = isol.cursor()
        isolx = isol.cursor()
        isolx.execute(("SELECT * from stock WHERE delstat = ?"), ("TBD", ))
        rowsrec = isolx.fetchall()
        col_labels = [("P. ID", "P. Name", "Qty. Ordered", "Delivered","Vendor", "Vendor", "Vendor Contact", "Lowstock Bar")]
        rowsxtb = col_labels + rowsrec

        def add_page_number(canvas, doc):
            canvas.saveState()
            canvas.setFont('Times-Roman', 10)
            page_number_text = "%d" % (doc.page)
            canvas.drawCentredString(
                0.75 * inch,
                0.75 * inch,
                page_number_text
            )
            canvas.restoreState()

        import sqlite3 as sql
        csvexx=sql.connect(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\DBFA_CUSTCC.db')
        print("Fetching data from database - II...")
        cursorx = csvexx.cursor()
        axct = cursorx.execute("select * from custcc")
        axctx = []
        for i in axct:
            axctx.append(i)
        axctx = [("C. ID","C. Name","Purchases Made","Total Amount","Loyalty Points")] + axctx
        doc = SimpleDocTemplate("dbfastorerep.pdf", pagesize=A4,
                                            rightMargin=2*cm,leftMargin=1.5*cm,
                                            topMargin=1*cm,bottomMargin=2*cm)
        # container for the 'Flowable' objects
        elements = []
        t1dot = ("<b>DBFA Automatic Store Report: </b> <br />This report has been automatically generated. This lists the profit earned, stock analytics and customer records as logged by DBFA.<br /><br />")
        t2dot = ("DBFA synchronously updates its database alongwith algorithmic data interpretation to deliver these reports. <br />This report contains information from the start of using DBFA on this system.<br /><br />")
        t6dot = ("Report generated on: " + dt_string)
        t3dot = ("<br /><br /><b>Most sold listing: </b><br />")
        t4dot = ("<br /><br /><b>Total profit per listing: </b><br /><br />")
        t5dot = ("<br /><br /><b>Most profit making listing: </b><br /><br />")
        t8dot = ("<br /><br /><b>Customer purchases: </b><br /><br />")
        t10dot = ("<br /><br /><b>DBFA Stock Orders Report: </b><br /><br /><br /><br /><b>Product stock yet to be recieved: </b><br /><br />")
        colas = (30, 300, 60, 50, 50)
        rowheights = (20, 20, 20, 20, 20,  20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20,20,20,20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20 )
        text1=Paragraph(t1dot)
        text2=Paragraph(t2dot)
        text3=Paragraph(t3dot)
        text4=Paragraph(t4dot)
        text5=Paragraph(t5dot)
        text6=Paragraph(t6dot)
        text8=Paragraph(t8dot)
        text10=Paragraph(t10dot)
        x=Table(rows, colas, rowheights)
        t=Table(arterxout)
        t2=Table(xarterxout)
        t4=Table(axctx)
        t5=Table(rowsxtb)
        if tabarter == ['--']:
            t7dot = ("<br /><br /><b>All listings currently in stock!</b><br /><br />")
        else:
            t7dot = ("<br /><br /><b>Products running low on stock: </b><br /><br />")
        
        
        tblStyle = TableStyle([('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                            ('VALIGN',(0,0),(-1,-1),'TOP'),
                            ('LINEBELOW',(0,0),(-1,-1),1,colors.black),
                            ('BOX',(0,0),(-1,-1),1,colors.black),
                            ('BOX',(0,0),(0,-1),1,colors.black)])
        tblStyle.add('BACKGROUND',(0,0),(1,0),colors.lightblue)
        tblStyle.add('BACKGROUND',(0,1),(-1,-1),colors.lightblue)
        GRID_STYLE = TableStyle(
            [('GRID', (0,0), (-1,-1), 0.25, colors.black),
            ('ALIGN', (1,1), (-1,-1), 'LEFT')]
            )
        text7=Paragraph(t7dot)
        t3=Table(tabarter)
        t.setStyle(GRID_STYLE)
        t2.setStyle(GRID_STYLE)
        t3.setStyle(GRID_STYLE)
        t4.setStyle(GRID_STYLE)
        t5.setStyle(GRID_STYLE)
        x.setStyle(GRID_STYLE)
        
        elements.append(text1)
        elements.append(text2)
        elements.append(text6)
        elements.append(text3)
        elements.append(t)
        elements.append(text5)
        elements.append(t2)
        elements.append(text7)
        elements.append(t3)
        elements.append(text4)
        elements.append(x)
        elements.append(text8)
        elements.append(t4)
        elements.append(text10)
        elements.append(t5)
        # write the document to disk
        doc.build(elements,
            onFirstPage=add_page_number,
            onLaterPages=add_page_number,)
        print("Report Created. ")
        for i in tqdm (range (100), desc="Publishing Report: "):
            time.sleep(0.00001)
        print("Opening store report now")
        os.startfile('dbfastorerep.pdf')
        time.sleep(2)


    #DBFA Backup&Switch
    elif decfac == "5":
        os.startfile(r'delauth.py')
        time.sleep(0.3)
        os._exit(0)

    
    #License        
    elif decfac == "6":
        print("Fetching latest licensing information.......")
        print(" ")
        print(" ")
        logoprintxrt()
        time.sleep(1.5)
        print(" ")
        print(" ")
        print("DBFA by Pranav Balaji, 2020")
        print(" ")
        print("_______ Licensing _______")
        print("           GNU PUBLIC LICENSE - TERMS AND CONDITIONS")
        print("    <deltaBillingFramework>  Copyright (C) 2020 Pranav Balaji and Sushant Gupta")
        print("    This program comes with ABSOLUTELY NO WARRANTY; for details type *show w*.")
        print("    This is free software, and you are welcome to redistribute it")
        print("    under certain conditions; type *show c* for details. ")
        toaster.show_toast("DFBA Framework Runtime Broker", "©2020: DBFA by Pranav Balaji and Sushant Gupta", duration = 1.5)
        print(" ")
        print(" ")
        print("Visit: www.github.com/deltaonealpha/deltaBillingFramework for complete licensing terms. ")
        print(" ")
        print(" ")
        time.sleep(2)
        webbrowser.open('https://telegra.ph/DBFA-Licensing-Information-08-16')
        print("--------------------------------------------------")
    

    #Stock Ordering Option
    elif decfac == "7":
        print("------------------ DBFA DELIVERY MANAGER ------------------")
        time.sleep(2)
        print("For issuing new delivery orders, use the invoicing option")
        print("-----------------------------------------------------------")
        print("a: View existing deliveries")
        print("b: Show delivery count")
        print("c: Confirm a delivery")
        delfacx = input("Select: ")
        if delfacx in ("a", "A"):
            # Fetch Data
            print("Currently pending deliveries::  \n")
            filedel = open('./DBFAdeliveries.txt', 'r')
            for line in filedel:
                print(line)
            print("\n\n")
            time.sleep(2)
        if delfacx in ("b", "B"):
            # Pending Delivery Count
            delcount = 0
            filedel = open('./DBFAdeliveries.txt', 'r+')
            for line in filedel:
                delcount+=1
            filedel.close()
            if delcount != 0:
                print("Number of pending deliveries: ", delcount)
            else:
                print("No deliveries pending! ")
            time.sleep(2)
        if delfacx in ("c", "C"):
            # Show data and Remove delivery record
            print("Current delivery data::  \n")
            filedel = open('./DBFAdeliveries.txt', 'r')
            for line in filedel:
                print(line)
            print("\n\n")
            cleanstr = ""
            deledid = input("Enter the delivery ID to remove (EXAMPLE: *del2*): ")
            delcount = 0
            filedel = open('./DBFAdeliveries.txt', 'r')
            for line in filedel:
                if deledid in line:
                    line = ""
                else:
                    delcount+=1
                cleanstr+=line
            filedel.close()
            filedel = open('./DBFAdeliveries.txt', 'w+')
            filedel.write(cleanstr)
            filedel.close()
            filedel = open('./DBFAdeliveries.txt', 'r')
            print("Delivery", deledid, "completed! ")
            time.sleep(2)

        elif delfacx not in ("a", "b", "c", "A", "B", "C"):
            print("Invalid option selected! \n\n")
            time.sleep(2)
            mainmenu()

    #DevChangelog Option
    elif decfac == "8":
        print("\n\nLatest Development Changelog: \n")
        webbrowser.open('https://telegra.ph/DBFA-8-RC2-Highlights-08-17')
        webbrowser.open('https://telegra.ph/DBFA-8-Release-Candidate---1-08-16')
        print("--------------------------------------------------")
        time.sleep(2)

    #DBFA Settings - Currently in development
    elif decfac == "9":
        command = "cls"
        os.system(command)
        time.sleep(1.2)
        print("-------------------------")
        time.sleep(0.4)
        print("------DBFA Settings------")
        time.sleep(0.2)
        print("    1: Open CSV post export?")
        print("    2: Add shortcut to desktop")
        print("This option is currently being developed. More would be added soon!")
        settfac = input("What would you like to do? ")
        if settfac == 1:
            print("CSV files once generated are auto-opened in your default worksheet app")
            print("Example: Microsoft Excel, LibreOffice Calc, Google Docs, et cetera.")
            print(" ")
            print("Open file after export? ")
            print("    y: Yes.")
            settfac1x = input("    n: No.")
            if settfac1x == "y":
                print("Option coming soon!")
            elif settfac1x == "n":
                print("Option coming soon!")
            else:
                print("Option coming soon!")


        if settfac == 2:
            import shutil
            import os
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive\Desktop')
            # Prints: C:\Users\sdkca\Desktop
            print("Shortcut will be created at: " + desktop)
            try:
                original = r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\Assets\run_DBFA.lnk'
                shutil.copy(original, desktop)
                print("Executed. ")
            except:
                print("DBFA Permission Error: Can't get perms to execute in directory! ")
            


    #Exit System
    elif decfac == "10":
        if os.path.exists(r'userblock.txt'):
            userblock.close()
            os.remove(r'userblock.txt')
        if os.path.exists(r'userblock.zconf'):
            userblock.close()
            os.remove(r'userblock.zconf')
        toaster.show_toast("DFBA Framework Runtime Broker", "Obsufcating program...", duration = 1)
        logoprintxrt()
        floodscreen()
        #os.close('securepack.pyw')
        os._exit(0)
    
        
    #CIT
    elif decfac == "113":
        print("INTERNAL TESTING MODE")
        ffxfac = str(input("Enter CIT Testing Mode? (y/n):: "))
        if ffxfac == "y":
            ffrxfac = str(input("Entering CIT may lead to data loss. Confirm entering CIT? (y/n):: "))
            if ffrxfac == "y":
                print("DNSS CIT MODE")
                print(" ")
                print(" ")
                print("NOTE: DBFA will restart to execute CIT options. ")
                print("CIT Options::")
                print("Enter '1' to CLEAR ALL CUSTOMER RECORDS")
                print("Enter '2' to CLEAR ALL VOUCHERS/ COUPONS")
                print("Enter '3' to exit CIT")
                citfacin = int(input("Waiting for input:: "))
                if citfacin == 1:
                    # window.close()
                    os.startfile(r'securepack.py')
                    time.sleep(1)
                    os._exit(0)
                if citfacin == 2:
                    # window.close()
                    os.startfile(r'securepackxvc.py')
                    time.sleep(1)
                    os._exit(0)
                else:
                    continue
        
            else:
                continue
        
        elif ffxfac == "3":
            print("Exiting CIT")
            time.sleep(1)
            continue
        else:
            print("Invalid input. . . . ")
            time.sleep(1)


    # Direct Calls Section - 2
    elif decfac in ("2a", "2A", "2 a", "2 A"):
        del2a()
        logger.write("--------------------------------------- \n")
        logger.write("  \n")
        logger.write("Date and time: ") #including the date and time of billing (as taken from the system)
        logger.write(dt_string)
        logger.write(" \n")
        logger.write("New customer registered: ")
        x = " custname: " + custname + " custemail: " + email + "\n"
        logger.write(x)
        logger.write("--------------------------------------- \n")

    elif decfac in ("2b", "2B", "2 b", "2 B"):
        del2b()
        logger.write("--------------------------------------- \n")
        logger.write("  \n")
        logger.write("Date and time: ") #including the date and time of billing (as taken from the system)
        logger.write(dt_string)
        logger.write(" \n")
        logger.write("Customer registry accessed! \n")
        logger.write("--------------------------------------- \n")

    elif decfac in ("2c", "2C", "2 c", "2 C"):
        del2c()
        logger.write("--------------------------------------- \n")
        logger.write("\nDBFA Customer Purchase Records accessed! \n")

    elif decfac in ("2d", "2D", "2 d", "2 D"):
        del2d()
        logger.write("--------------------------------------- \n")
        logger.write("\nCustomer search used. \n")

    elif decfac in ("2e", "2E", "2 e", "2 E"):
        del2e()
        logger.write("\n\n--------------------------------------- \n")
        logger.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n")
        logger.write("Customer data exported to CSV! ")
        with HiddenPrints():
            try:
                sender = telegram_bot_sendtext(dt_string + "\n" + "Sales data exported to CSV- REDFLAG Urgent Security Notice!")
                print(sender)
            except Exception:
                pass
        logger.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n")
        logger.write("--------------------------------------- \n\n\n")



    # Direct Calls Section - 3
    elif decfac in ("3a", "3A", "3 a", "3 A"):
        del3a()

    elif decfac in ("3b", "3B", "3 b", "3 B"):
        del3b()

    elif decfac in ("3c", "3C", "3 c", "3 C"):
        del3c()

    elif decfac in ("3d", "3D", "3 d", "3 D"):
        del3d()

    elif decfac in ("3e", "3E", "3 e", "3 E"):
        del3e()
        logger.write("\n--------------------------------------- \n")
        logger.write("Sales log accessed! ")


    elif decfac in ("3f", "3F", "3 f", "3 F"):
        del3f()
        logger.write("\n\n--------------------------------------- \n")
        logger.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n")
        with HiddenPrints():
            try:
                sender = telegram_bot_sendtext(dt_string + "\n" + "Customer data exported to CSV- REDFLAG Urgent Security Notice!")
                print(sender)
            except Exception:
                pass
        logger.write("Sales data exported to CSV! ")
        logger.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n")
        logger.write("--------------------------------------- \n\n\n")



    elif decfac in (None, "", " "):
        print("Please select a valid main-menu option. erc101\n\n")
        time.sleep(0.8)
        continue

    else:
        print("Please select a valid main-menu option. erc101\n\n")
        time.sleep(0.8)
        continue

# End of program
# Available on github: www.github.com/deltaonealpha/DBFA
# https://deltaonealpha.github.io/DBFA/