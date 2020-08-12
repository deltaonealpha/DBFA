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
    rows = ssh7.fetchall()
    inval = rows


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
    print("Current product stock: ", values)
    ssxdsccheck = "1 2 3 4"
    if values in ssxdsccheck:
        print("[Stock running out] Currently in stock: ", values, "pieces. Restock ASAP...")
        ssxvarscheck = 1
    elif values == "0":
        ssxvarscheck = 2
    elif values != "0":
        ssxvarscheck = 1
    time.sleep(1)
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
    global cccheck
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
    logox = (Fore.CYAN+'''\n       _____   ____    ____  ____   ____    Options:
      / /  // / /  \\  /___  /__||  |--//      1: Issue a Bill                          4: Auto-Generate Store Report 
     / /  // / /===| ///// ////||    //       2: Manage Customers                      
    /_/__// /_/__ / /     /    ||   //              a: Register a Customer             5: Start DBFA Backup&Switch
            '''+Fore.MAGENTA+'''The OG Store Manager'''+Fore.CYAN+'''                    b: Customer Registry                         
    ''' + 'A word from our partner: ' + Fore.BLACK + Back.CYAN + 'HOTEL? Trivago!' + Back.BLACK + Fore.CYAN + '''        c: Customer Purchase Records       6: View Software License
                                                    d: Find a Customer                                
                                              3: Store Options:                        7: Quit
                                                    a: Manage Stock
    - enter CIT code to view more options -         b: Manage Vouchers                 
                                                    c: Product Listing
                                                    d: Sales Log

                                              
    ''' + Fore.WHITE)                                                                       
    print(logox)
    print()
    print()



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
        payboxie()


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
    elif cccheck == 1:
        redeemindic = 0
        lylpoints = 0
        netpay = total

    else:
        redeemindic = 0
        netpay = total


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
\n
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
print("Heyy there,",  'Binod!') #enable parts in the auth script to enable user detection
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
    time.sleep(0.3)  #for a seamless experience
    decfac = int(input("Select option: "))

    #Billing Mode
    if decfac == 1:
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
        else:
            custcheck(custt)
        #print(cccheck)
        logger.write("-----------------  ") #writing to log file
        logger.write("Cust. ID: \n")
        logger.write(custt)
        logger.write("  \n")
        logger.write("Date and time: \n") #including the date and time of billing (as taken from the system)
        logger.write(dt_string)
        logger.write(" \n")
        abcd1 = 1
        purcheck = ""
        time.sleep(0.3) #for a seamless experience
        telethon = "DBFA Billing System" + "\n" + dt_string + "\n" + "Customer: " + custt + "\n"
        writer = writer + "DBFA Billing Framework" + "\n" + "One-stop solution for all your billing needs!" + "\n" + "\n" + "Billing time: " + dt_string + "\n" + "Customer ID: " + custt + "\n" + "-----------------------------" + "\n" + "\n"
        global billiemaster
        billiemaster = 0 #variable for totalling the price
        time.sleep(0.2) #for a seamless experience
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
                    pi = 50 - lenxr
                    idlerxx = namie[item] + " "*pi + "₹"+'%d'%data[item] + " "*cj + "1 qty. ~"
                    purcheck += idlerxx
                    print("---")
                    priceprod = "₹" + '%d' % data[item]
                    logger.write("Appending product to order: \n")  #writing to file
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
            payboxie(custt, total)
            xpayboxie()
            if xrt == 1:
                writer = writer + "----------------- BILLING CYCLE CANCELLED -------------------"    
                break
            else:
                rupeesymbol = "₹".encode("utf-8")
                inmaintainer()
                infetch()
                print("\n\n-------------------------------------------------------------------------")
                print("Invoice ID: ", inval, "| Time: ",dt_string, "| No. of items: ", afac)
                print(payindic)
                print("-------------------------------------------------------------------------")
                printobj = purcheck.split("~")
                for i in printobj:
                    print(i)
                print("-------------------------------------------------------------------------")
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
                print("-------------------------------------------------------------------------")
                print("Amount to be paid: ₹","%.2f" % netpay)
                print("-------------------------------------------------------------------------")
                toaster.show_toast("DFBA Billing:  Total billed for-",str(total), duration = 1)
                logger.write("Total amount billed for: \n") #writing to file
                if custt not in ("", " ", 0) and cccheck == 0:
                    writer += "Used DBFA loyalty points worth: " + '%s'%lylpoints + "\n"
                #regin.write("NET TOTAL: \n") #writing to file
                telethon = telethon + "NET TOTAL: \n" + "₹" + str(total) + "\n" 
                writer = writer + "NET TOTAL: \n" + str(total) + "\n" 
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
                namer = 'DBFAinvoice '+ daterey+'.pdf'
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
    elif decfac == 2:
        print("Select: ")
        print("    a: Register a Customer ")
        print("    b: Customer Registry ")
        print("    c: Customer Purchase Records ")    
        print("    d: Find a Customer \n")
        selected = input("Choose your option: ")
        print("\n")
        if selected in ("a", "A"):
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
            logger.write("--------------------------------------- \n")
            logger.write("  \n")
            logger.write("Date and time: ") #including the date and time of billing (as taken from the system)
            logger.write(dt_string)
            logger.write(" \n")
            logger.write("New customer registered: ")
            x = " custname: " + custname + " custemail: " + email + "\n"
            logger.write(x)
            logger.write("--------------------------------------- \n")
            print("Customer ID", idd, "registered in directory.")
            print("---------------------------------------")
            print(" ")
            print(" ")
            #conn.close()
            time.sleep(1) #for a seamless experience

        if selected in ("b", "B"):
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
            logger.write("--------------------------------------- \n")
            logger.write("  \n")
            logger.write("Date and time: ") #including the date and time of billing (as taken from the system)
            logger.write(dt_string)
            logger.write(" \n")
            logger.write("Customer registry accessed! \n")
            logger.write("--------------------------------------- \n")
            conn.close()
            conn.close()
            print()
            print()
            time.sleep(2) #delay for easy-table viewing


        if selected in ("c", "C"):
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

        elif selected in ("d", "D"):
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
                    print("Customer not found.")
            except:
                print("Error encountered.  ")



        elif selected not in ("a", "b", "c", "d", "A", "B", "C", "D"):
            print("Please chose a valid option!")
            time.sleep(1)
        

    #Store Options:
    elif decfac == 3:
        print("Select: ")
        print("    a: Manage Stock ")
        print("    b: Manage Vouchers ")
        print("    c: Product Listing ")
        print("    d: Sales Log: \n")
        storeselected = input("Choose your option: ")
        print("\n")

        if storeselected in ("a", "A"):
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
            
        
        if storeselected in ("b", "B"):
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

        if storeselected in ("c", "C"):
            try:
                if os.path.exists(r'userblock.txt'):
                    os.remove(r'userblock.txt')
                if os.path.exists(r'userblock.zconf'):
                    os.remove(r'userblock.zconf')
            except PermissionError:
                    pass
            print("Store listing (as per updated records): ")
            print(tabulate(tablx, headers = titlex, floatfmt = ".4f"))

        if storeselected in ("d", "D"):
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
            logger.write("  \n")
            logger.write("Date and time: ") #including the date and time of billing (as taken from the system)
            logger.write(dt_string)
            logger.write(" \n")
            if passw == "root":
                    time.sleep(1) #for a seamless experience
                    print("Hold on, moneybags.")
                    with HiddenPrints():
                        try:
                            sender = telegram_bot_sendtext(dt_string + "\n" + "Registry files accessed - DBFA SECURITY")
                            print(sender)
                        except Exception:
                            pass
                    time.sleep(0.4)
                    print("Here:: ")
                    time.sleep(0.2) #for a seamless experience 
                    logger.write("Log file access attempt - Oauth complete \n")
                    logger.close() #to change file access modes 
                    logger = open("registry.txt", "r+")
                    # Uncomment the below lines if the program has to be modified to show the records in the shell itself and not externally
                    # print(logger.read())
                    # print()
                    # print("Opening sales log externally now. ")
                    time.sleep(1.4) #for a seamless experience
                    os.startfile('registry.txt') #to open the external notepad application
            else:
                
                logger.write("  \n")
                logger.write("Date and time: ")  #including the date and time of billing (as taken from the system)
                logger.write(dt_string)
                logger.write(" \n")
                time.sleep(1) #for a seamless experience
                logger.write("Log file access attempt - Oauth failiure!!! \n")
                print("Ehh that'd be wrong, sneaky-hat. Try again: ")
                print(" ")
                print(" - Echo-supressed input - ")
                passw = getpass.getpass(prompt='Enter root password to view store activity registry: ', stream=None)
                if passw == "root":
                        time.sleep(1) #for a seamless experience
                        print("Hold on, moneybags.")
                        with HiddenPrints():
                            try:
                                sender = telegram_bot_sendtext(dt_string + "\n" + "Registry files accessed - DBFA SECURITY: ATTEMPT 02")
                                print(sender)
                            except Exception:
                                pass
                        print("There ya go:: ")
                        time.sleep(0.6) #for a seamless experience
                        logger.write("  \n")
                        logger.write("Date and time: \n") #including the date and time of billing (as taken from the system)
                        logger.write(dt_string)
                        logger.write(" \n")
                        logger.write("Log file access attempt - AUTHORIZATION SUCCESS \n")
                        logger.close() #to change file access modes 
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

        elif storeselected not in ("a", "b", "c", "d", "A", "B", "C", "D"):
            print("Please select a valid option! ")
            time.sleep(1)
            mainmenu()



    #Reports
    elif decfac == 4:
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

        
        doc = SimpleDocTemplate("dbfastorerep.pdf", pagesize=A4,
                                            rightMargin=2*cm,leftMargin=1.5*cm,
                                            topMargin=1*cm,bottomMargin=2*cm)
        # container for the 'Flowable' objects
        elements = []
        t1dot = ("<b>DBFA Automatic Store Report: </b> <br />This report has been automatically generated. This lists profit and stock analytics as logged by DBFA.<br /><br />")
        t2dot = ("DBFA synchronously updates its database alongwith algorithmic data interpretation to deliver these reports. <br />This report contains information from the start of using DBFA on this system.<br /><br />")
        t6dot = ("Report generated on: " + dt_string)
        t3dot = ("<br /><br /><b>Most sold listing: </b><br />")
        t4dot = ("<br /><br /><b>Total profit per listing: </b><br /><br />")
        t5dot = ("<br /><br /><b>Most profit making listing: </b><br /><br />")
        colas = (30, 300, 60, 50, 50)
        rowheights = (20, 20, 20, 20, 20,  20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20,20,20,20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20 )
        text1=Paragraph(t1dot)
        text2=Paragraph(t2dot)
        text3=Paragraph(t3dot)
        text4=Paragraph(t4dot)
        text5=Paragraph(t5dot)
        text6=Paragraph(t6dot)
        x=Table(rows, colas, rowheights)
        t=Table(arterxout)
        t2=Table(xarterxout)
        if tabarter == ['--']:
            t7dot = ("<br /><br /><b>All listings currently in stock!</b><br /><br />")
        else:
            t7dot = ("<br /><br /><b>Products running low on stock: </b><br /><br />")
        text7=Paragraph(t7dot)
        t3=Table(tabarter)
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
        t.setStyle(GRID_STYLE)
        t2.setStyle(GRID_STYLE)
        t3.setStyle(GRID_STYLE)
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
    elif decfac == 5:
        os.startfile(r'delauth.py')
        time.sleep(0.3)
        os._exit(0)

    #Exit System
    elif decfac == 7:
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
        
    elif decfac == 6:
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
        aacsbcfac = int(input("Enter '1' to view complete licensing stuff or '2' to return: "))
        if aacsbcfac == 1:
            print(" ")
            print("Please select to open with your prefered text viewer/ edittor.")
            os.startfile(r"‪C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\LICENSE")
            print(" ")
            print(" ")
            print("--------------------------------------------------")
        
    #CIT
    elif decfac == 113:
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