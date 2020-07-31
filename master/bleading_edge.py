'''     ___ ______ ___   _____________    ____________     _______
       /  /_______/  /  /  /_______/  /  /  /________/    /  /_/ /
      /  /       /  /  /  /       /  /  /  /             /  /  / /
     /  /       /  /  /  /_______/  /  /  /             /  /   / /
    /  /       /  /  / // // // // /  /  /_________    /  /____/ / BILLING 
   /  /       /  /  /  /-------/  /  /  /_________/   /  /_____/ / FRAMEWORK
  /  /       /  /  /  /       /  /  /  /             /  /      / /
 /  /_______/  /  /  /______ /  /  /  /             /  /       / /
/__/_______/__/  /__/_______/__/  /__/             /__/        /_/

    www.github.com/deltaonealpha/
    Program repo: https://deltaonealpha.github.io/DBFA/
'''
#vs

import getpass, time, pathlib, sqlite3, sys, os #sys, os for system-level ops
from tabularprint import table

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


#auth verification
if os.path.exists(r'userblock.zconf'):
    print("Verifying login...")
    print(" ")
if os.path.exists(r'userblock.txt'):
    userblock = open(r"userblock.txt","r") #Opening / creating (if it doesn't exist already) the .txt record file
    valfn = 1
else:
    valfn = 0
if os.path.exists(r'DBFA.zconf'):
    pass
else:
    print("Getting the database online.......")
    time.sleep(0.5)
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
    import requests
    with HiddenPrints():
        bot_token = '1215404401:AAEvVBwzogEhOvBaW5iSpHRbz3Tnc7fCZis'
        bot_chatID = '680917769'
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        return response.json()

# DBFA Logo Printer
def logoprintxrt():
            print("        ___ ______ ___   _____________    ____________     _______")
            time.sleep(0.1)
            print("       /  /_______/  /  /  /_______/  /  /  /________/    /  /_/ /")
            time.sleep(0.1)
            print("      /  /       /  /  /  /       /  /  /  /             /  /  / /")
            time.sleep(0.1)
            print("     /  /       /  /  /  /_______/  /  /  /  CLI        /  /   / /")
            time.sleep(0.1)
            print("    /  /       /  /  / // // // // /  /  /_________    /  /____/ /")
            time.sleep(0.1)
            print("   /  /       /  /  /  /-------/  /  /  /_________/   /  /_____/ /")
            time.sleep(0.1)
            print("  /  /       /  /  /  /       /  /  /  /             /  /      / /")
            time.sleep(0.1)
            print(" /  /_______/  /  /  /______ /  /  /  /             /  /       / /")
            time.sleep(0.1)
            print("/__/_______/__/  /__/_______/__/  /__/             /__/        /__/")
            print(" ")
            print(" ")



# Database builder
# Stock Records Master DB
ssh = sqlite3.connect(r'DBFA_handler.db')
ssh7 = ssh.cursor()
#c.execute("DROP TABLE cust;")
ssh7.execute("""CREATE TABLE IF NOT EXISTS sshandler
    (prodid INTEGER,
    ssstock INTEGER);""")
ssh = sqlite3.connect('DBFA_handler.db')
ssh7 = ssh.cursor()
if os.path.exists(r'DBFA_handler.db'):
    pass
else:
    ssh7.execute("""CREATE TABLE IF NOT EXISTS sshandler
        (prodid INTEGER,
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
#c.execute("DROP TABLE cust;")
xbr7.execute("""CREATE TABLE IF NOT EXISTS custcc
    (custt INTEGER PRIMARY KEY,
    custname VARCHAR(500),
    purchasecount INTEGER,
    ptotalx INTEGER);""")
xon = sqlite3.connect('DBFA_CUSTCC.db')
xbr7 = xon.cursor()
if os.path.exists(r'DBFA_CUSTCC.db'):
    pass
else:
    xbr7.execute("""CREATE TABLE IF NOT EXISTS custcc
        (custt INTEGER PRIMARY KEY,
        custname VARCHAR(500),
        purchasecount INTEGER,
        ptotalx INTEGER);""")
 
conn = sqlite3.connect('DBFA.db')
if os.path.exists(r'DBFA.db'):
    pass
else:
    conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')


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
    namiex = ["TV 4K OLED 50", "TV FHD OLED 50", "8K QLED 80", "Redmi K20 PRO", "Redmi K20", "Redmi Note 9 PRO", "POCOPHONE F", "Mi MIX ALPHA", "Wireless Headphones", "Noise-Cancelling Wireless Headphones", "Essentials Headphones", "Gaming Headphones", "Truly-Wireless Eadphones", "Neckband-Style Wireless Earphones", "Essentials Earphones", "Gaming Earphones", "30W Bluetooth Speakers", "20W Bluetooth Speakers", "9""Essentials Bluetooth Speaker", "BOSE QC35", "Essentials Home Theatre", "Wired Speaker - 5.", "Essentials Wired Speaker - STEREO", "Tactical Power Bank 30000mah", "5""Essentials Power Bank 0000mah", "Essentials Mouse", "Logitech G604 LightSpeed Wireless", "Tactical Essentials Keyboard", "DROP GS21k RGB Gaming Keyboard", "Polowski Tactical Flashlight", "OneFiber Wi-Fi Router AX7", "Mijia Mesh Wi-Fi Router", "lapcare 0W Laptop Adapter", "lapcare 60W Laptop Adapter", "Spigen Phone Case(s)", "Essentials Phone Charger 150W", "HyperPower Type-C Gallium-Nitride Charger 100W", "ASUS Zephyrus G4 Gaming Laptop", "L XPS 5 Content Creator's Laptop", "Hewlett-Packard Essential's Student's Laptop (Chromebook)"]
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

# Record Master


def repproffetch():
    global rowsx
    rec = sqlite3.connect(r'recmaster.db')
    recx = rec.cursor()
    recx.execute("SELECT DISTINCT prodprofit FROM recmasterx")
    rowsx = recx.fetchall()
    print(rowsx)





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
    namiex = ["TV 4K OLED 50", "TV FHD OLED 50", "8K QLED 80", "Redmi K20 PRO", "Redmi K20", "Redmi Note 9 PRO", "POCOPHONE F", "Mi MIX ALPHA", "Wireless Headphones", "Noise-Cancelling Wireless Headphones", "Essentials Headphones", "Gaming Headphones", "Truly-Wireless Eadphones", "Neckband-Style Wireless Earphones", "Essentials Earphones", "Gaming Earphones", "30W Bluetooth Speakers", "20W Bluetooth Speakers", "9""Essentials Bluetooth Speaker", "BOSE QC35", "Essentials Home Theatre", "Wired Speaker - 5.", "Essentials Wired Speaker - STEREO", "Tactical Power Bank 30000mah", "5""Essentials Power Bank 0000mah", "Essentials Mouse", "Logitech RGB Gaming Mouse with Traction & Weight Adjustment", "Tactical Essentials Keyboard", "Mechanical Cherry MX (Red) RGB Gaming Keyboard", "Polowski Tactical Flashlight", "OneFiber Wi-Fi Router AX7", "Mijia Mesh Wi-Fi Router", "lapcare 0W Laptop Adapter", "lapcare 60W Laptop Adapter", "Spigen Phone Case(s)", "Essentials Phone Charger 150W", "HyperPower Type-C Gallium-Nitride Charger 100W", "ASUS Zephyrus G4 Gaming Laptop", "L XPS 5 Content Creator's Laptop", "Hewlett-Packard Essential's Student's Laptop (Chromebook)"]
    for crrt in namiex:
        gg = (namiex.index(crrt)) + 1
        str = "insert into sshandler(prodid, ssstock) values({}, {})"
        # io = (gg)
        ssh7.execute(str.format(gg, inxstock))
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
    ssh7.execute("SELECT DISTINCT prodid, ssstock FROM sshandler")
    rows = ssh7.fetchall()
    col_labels = ("Product ID", "Product Stock")
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
    global conn
    str = "insert into cust(custt, custname, email) values('%s', '%s', '%s')"
    io = (custt, custname, email)
    conn.execute(str % io)
    conn.commit()
    print("Customer", custname, "registered in store directory")

# Customer Purchase Updater
def custcc(custt, purchasecount, ptotalx):  #defining a function to input data into the SQL database's table
    global xon
    xon = sqlite3.connect(r'DBFA_CUSTCC.db')
    xbr7 = xon.cursor()
    str = "insert into custcc(custt, purchasecount, ptotalx) values('%s', '%s', '%s')"
    io = (custt, purchasecount, ptotalx)
    xbr7.execute(str % io)
    xon.commit()
    xbr7.close()
    print("FJHG")

# Customer Purchase Updater
def updatescript(custt, pincrement):
    try:
        xon = sqlite3.connect('DBFA_CUSTCC.db')
        xbr7 = xon.cursor()
        # hidden prints here ig
        updatexr = """UPDATE custcc SET purchasecount = purchasecount + 1 WHERE custt = ?"""
        updatexxr = """UPDATE custcc SET ptotalx = ptotalx + ? WHERE custt = ?"""
        indicator = (custt)
        xrindicator = (pincrement, custt)
        xbr7.execute(updatexr, indicator)
        xbr7.execute(updatexxr, xrindicator)
        xon.commit()
        xbr7.close()
    except sqlite3.Error as error:
        pass


def floodscreen():
    import cv2 
    image = cv2.imread("imagepx.png")
    cv2.imshow("Initializing... ", image)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()


# Main Menu
def mainmenu(): #defining a function for the main menu
    from colorama import init, Fore, Back, Style #color-settings for the partner/sponsor adverts
    init(convert = True)
    print(Fore.RED) #red-line to indicate program start
    print("---------------------------------------------")
    print(Fore.WHITE)
    print('A word from our partner: ' + Fore.BLACK + Back.CYAN + 'HOTEL? Trivago!') #Text over here #Custom advert
    print(Style.RESET_ALL) 
    print("DBFA Store Listing:")
    print("Enter: ") 
    print("'1' for INVOICING")
    print("'2' for REGISTERING NEW CUSTOMERS,")
    print("'3' to VIEW REGISTERED CUSTOMERS,")
    print("'4' to VIEW CUSTOMER PURCHASE RECORDS")
    print("'5' to VIEW GENERATED INVOICES,")
    print("'6' to REVIEW STORE LISTING,")
    print("'7' to REVIEW LICENSING INFORMATION,")
    print("'8' to VIEW OR UPDATE STOCK,")
    print("'9' to ISSUE COUPONS,")
    print("'10' to VIEW THE STORE REPORT,")
    print("and '11' to exit the framework.")
    print("~ enter the administrator code to enter CIT mode ~")
    print("---------------------------------------------")
    print()
    print()
 

def floodpay():
    import cv2 
    image = cv2.imread("qr-code.png")
    cv2.imshow("Pay With UPI", image)
    cv2.waitKey(150000)
    cv2.destroyAllWindows()

# Payments Handler
def payboxie():
    command = "cls"
    os.system(command)
    global payindic
    global xrt
    xrt = 0
    payindic = 0
    from colorama import init, Fore, Back, Style #color-settings for the partner/sponsor adverts
    print(Fore.LIGHTBLUE_EX + "-----------------" + Fore.WHITE)
    init(convert = True)
    print("Amount to be paid: \u20B9","%.2f" % total)
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





# Store listing::
data = {"1":40000, "2":55000, "3":67000, "4":25000, "5":21000, "6":14000, "7":13000, "8":220000, "9":4500, "10":17000, "11":1200, "12":3700, "13":4500, "14":2200, "15":700, "16":2750, "17":6499, "18":1499, "19":799, "20":27000, "21":6750, "22":2100, "23":1199, "24":3210, "25":989, "26":750, "27":1700, "28":600, "29":2175, "30":890, "31":2100, "32":7158, "33":597, "34":347, "35":500, "36":300, "37":1097, "38":80000, "39":87900, "40":23790}
namie = {"1":"TV 4K OLED 50", "2":"TV FHD OLED 50", "3":"8K QLED 80", "4":"Redmi K20 PRO", "5":"Redmi K20", "6":"Redmi Note 8 PRO", "7":"POCOPHONE F1", "8":"Mi MIX ALPHA", "9":"Wireless Headphones", "10":"Noise-Cancelling Wireless Headphones", "11":"Essentials Headphones", "12":"Gaming Headphones", "13":"Truly-Wireless Eadphones", "14":"Neckband-Style Wireless Earphones", "15":"Essentials Earphones", "16":"Gaming Earphones", "17":"30W Bluetooth Speakers", "18":"10W Bluetooth Speakers", "19":"Essentials Bluetooth Speaker", "20":"ULTRA Home Theatre", "21":"Essentials Home Theatre", "22":"  Wired Speaker - 5.1", "23":"  Essentials Wired Speaker - STEREO", "24":"Tactical Power Bank 30000mah", "25":"Essentials Power Bank 10000mah", "26":"Essentials Mouse", "27":"Logitech G604 LightSpeed Wireless", "28":"Tactical Essentials Keyboard", "29":"DROP GS21k RGB Gaming Keyboard", "30":"Polowski Tactical Flashlight", "31":"OneFiber Wi-Fi Router AX17", "32":"Mijia Mesh Wi-Fi Router", "33":"lapcare 120W Laptop Adapter", "34":"lapcare 60W Laptop Adapter", "35":"Spigen Phone Case(s)", "36":"Essentials Phone Charger 10W", "37":"HyperPower Type-C Gallium-Nitride Charger 100W", "38":"ASUS Zephyrus G14 Gaming Laptop", "39":"L XPS 15 Content Creator's Laptop", "40":"Hewlett-Packard Essential's Student's Laptop (Chromebook)"}
namiex = ["TV 4K OLED 50", "TV FHD OLED 50", "8K QLED 80", "Redmi K20 PRO", "Redmi K20", "Redmi Note 9 PRO", "POCOPHONE F", "Mi MIX ALPHA", "Wireless Headphones", "Noise-Cancelling Wireless Headphones", "Essentials Headphones", "Gaming Headphones", "Truly-Wireless Eadphones", "Neckband-Style Wireless Earphones", "Essentials Earphones", "Gaming Earphones", "30W Bluetooth Speakers", "20W Bluetooth Speakers", "9""Essentials Bluetooth Speaker", "BOSE QC35", "Essentials Home Theatre", "Wired Speaker - 5.", "Essentials Wired Speaker - STEREO", "Tactical Power Bank 30000mah", "5""Essentials Power Bank 0000mah", "Essentials Mouse", "Logitech G604 LightSpeed Wireless", "Tactical Essentials Keyboard", "DROP GS21k RGB Gaming Keyboard", "Polowski Tactical Flashlight", "OneFiber Wi-Fi Router AX7", "Mijia Mesh Wi-Fi Router", "lapcare 0W Laptop Adapter", "lapcare 60W Laptop Adapter", "Spigen Phone Case(s)", "Essentials Phone Charger 150W", "HyperPower Type-C Gallium-Nitride Charger 100W", "ASUS Zephyrus G4 Gaming Laptop", "L XPS 5 Content Creator's Laptop", "Hewlett-Packard Essential's Student's Laptop (Chromebook)"]
datax = [40000, 55000, 67000, 25000, 21000, 14000, 3000, 220000, 4500, 17000, 1200, 3700, 4500, 2200, 700, 2750, 6499, 1499, 799, 27000, 6750, 2100, 1199, 3210, 989, 750, 1700, 600, 2175, 890, 2100, 7158, 597, 347, 500, 300, 1097, 80000, 87900, 23790]
dataxr = []
for i in datax:
    i = "₹" + '%d' % i
    dataxr.append(i)
tablx = zip(namiex, dataxr)
titlex = ["Product:", "Pricing:"]

print("DBFA Billing Framework: Version 2.227 (alpha) ")
print("Licensed under the GNU PUBLIC LICENSE")
print("<DBFA>  Copyright (C) 2020 Pranav Balaji and Sushant Gupta")
print(" ")
print("Visit: www.github.com/deltaonealpha/deltaBillingFramework for complete licensing terms. ")
print(" ")
print(" ")
logoprintxrt()
time.sleep(1.3)
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
toaster.show_toast("DFBA Runtime Manager","Read documentation prior to use.", duration = 2)
print("Heyy there!",  'ed') #enable parts in the auth script to enable user detection
time.sleep(1.34)
if valfn == 0:
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
        custt = input("Customer ID (optional)): ")
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
        discountx = '%d' % discount
        telethon = telethon + "\n" + "Tax amount: 18%" + "\n"  + "Discount: " + discountx + "%" + "\n" + "\n"
        writer = writer + "\n" + "\n" + "-----------------------------" + "\n" + "Tax amount: 18%"  + "\n"  + discountx + "\n"  + "\n" 
        payboxie()
        if xrt == 1:
            writer = writer + "----------------- BILLING CYCLE CANCELLED -------------------"    
            break
        else:
            rupeesymbol = "\u20B9".encode("utf-8")
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
            print("Amount           : \u20B9",billiemaster)
            cpon_ssinglefetch(cponid)
            print("Voucher used     :",sfetch_values)
            discountstr = "Discount "+"("+'%d'%discount+"%)    :"
            print(discountstr, "\u20B9","%.2f" % (((discount)/100)*billiemaster))
            print("IGST             : \u20B9","%.2f" % ((9/100)*billiemaster))
            print("CGST             : \u20B9","%.2f" % ((9/100)*billiemaster))
            print("-------------------------------------------------------------------------")
            print("Amount to be paid: \u20B9","%.2f" % total)
            print("-------------------------------------------------------------------------")
            toaster.show_toast("DFBA Billing:  Total billed for-",str(total), duration = 1)
            logger.write("Total amount billed for: \n") #writing to file
            #regin.write("NET TOTAL: \n") #writing to file
            telethon = telethon + "NET TOTAL: \n" + "\u20B9" + str(total) + "\n" 
            writer = writer + "NET TOTAL: \n" + str(total) + "\n" 
            logger.write(str(total))
            logger.write("\n")
            #regin.write(str(total))
            #regin.write("\n")
            updatescript(custt, total) #adds billed amount to the customer's record
            abcd1+=1
            afac+=1
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")  #datetime object containing current date and time
            daterey = (dt_string.replace("/","")).replace(":", "")
            namer = 'invoice'+ daterey+'.pdf'
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

            #regin.close()
            with HiddenPrints():
                try:
                    sender = telegram_bot_sendtext(telethon)
                    print(sender)
                except Exception:
                    pass
                    
            print()
    #Register Customer
    elif decfac == 2:
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
        cursor = conn.cursor()
        cursor.execute("select * from cust")
        results = cursor.fetchall()
        idd = len(results)+1
        print("Registering customer with ID: ", idd)
        custname = input("Customer Name: ")
        email = input("Customer's E-mail ID: ")
        inserter(idd, custname, email) #argumental function to insert values into the SQL database
        nullvalue = 0
        custcc(idd, nullvalue, nullvalue)
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
    #VIEW ALL CUSTOMERS
    elif decfac == 3:
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

    #View Customer Purchase Records
    elif decfac == 4:
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
        print("Customer Purchase Records: ")

        import pandas as pd

        flat_list = []
        for sublist in l:
            flat_list.append(sublist)
        mydf = pd.DataFrame(flat_list, columns=['Customer ID', 'Name', 'Purchases Made', 'Total'])
        mydf.pivot(index='Customer ID', columns='Purchases Made', values='Total').fillna(value='-')
        print(mydf)
        time.sleep(2)
        
        '''
        for row in rows:
            print(row)
            print(" ")
        '''
        xbr7.close()
        toaster.show_toast("DFBA QuickSync", "Database acessed", duration = 0.5) 
    
    #View Generated Bills
    elif decfac == 5:
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
                    logger = open("log.txt","r+")  
                    # print(logger.read())
                    # print()
                    # print("Opening sales log externally now. ")
                    time.sleep(1.4) #for a seamless experience
                    os.startfile('log.txt')
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
    #View Listing Option
    elif decfac == 6:
        try:
            if os.path.exists(r'userblock.txt'):
                os.remove(r'userblock.txt')
            if os.path.exists(r'userblock.zconf'):
                os.remove(r'userblock.zconf')
        except PermissionError:
                pass
        print("Store listing (as per updated records): ")
        print(tabulate(tablx, headers = titlex, floatfmt = ".4f"))

    #Stock Master
    elif decfac == 8:
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

    #Coupon Master
    elif decfac == 9:
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

    #Reports
    elif decfac == 10:
        command = "cls"
        os.system(command)
        print("-- Generating store report --")
        print("Please wait...")
        repdatafetch()
        findMaximum = "select max(prodsales) from recmasterx"
        recx.execute(findMaximum)
        # Print the maximum score
        netr = recx.fetchone()[0]
        findin = "select prodid, prodname, prodprofit, prodsales, netprof from recmasterx WHERE prodsales = ?"
        arterx = str(int(netr))
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
        t1dot = "<b>DBFA Automatic Store Report: </b> <br />This report has been automatically generated. This lists profits earned per listing.<br /><br />"
        t2dot = "DBFA uses synchronous database updation alongwith algorithmic data interpretation to deliver these reports. <br /><br />"
        t3dot = "<br /><br /><b>Product most sold: </b><br />"
        t4dot = "<br /><br /><b>Total profit per product: </b><br /><br />"
        t5dot = "<br /><br /><b>Most profit making product: </b><br /><br />"
        colas = (30, 300, 60, 50, 50)
        rowheights = (20, 20, 20, 20, 20,  20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20,20,20,20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20 )
        x=Table(rows, colas, rowheights)
        text1=Paragraph(t1dot)
        text2=Paragraph(t2dot)
        text3=Paragraph(t3dot)
        text4=Paragraph(t4dot)
        text5=Paragraph(t5dot)
        t=Table(arterxout)
        t2=Table(xarterxout)
        tblStyle = TableStyle([('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                            ('VALIGN',(0,0),(-1,-1),'TOP'),
                            ('LINEBELOW',(0,0),(-1,-1),1,colors.black),
                            ('BOX',(0,0),(-1,-1),1,colors.black),
                            ('BOX',(0,0),(0,-1),1,colors.black)])
        tblStyle.add('BACKGROUND',(0,0),(1,0),colors.lightblue)
        tblStyle.add('BACKGROUND',(0,1),(-1,-1),colors.white)
        GRID_STYLE = TableStyle(
            [('GRID', (0,0), (-1,-1), 0.25, colors.black),
            ('ALIGN', (1,1), (-1,-1), 'RIGHT')]
            )
        t.setStyle(GRID_STYLE)
        t2.setStyle(GRID_STYLE)
        x.setStyle(GRID_STYLE)
        elements.append(text1)
        elements.append(text2)
        elements.append(text3)
        elements.append(t)
        elements.append(text5)
        elements.append(t2)
        elements.append(text4)
        elements.append(x)
        # write the document to disk
        doc.build(elements,
            onFirstPage=add_page_number,
            onLaterPages=add_page_number,)
        print("Moved. ")
        time.sleep(1)
        print("Opening store report now")
        os.startfile('dbfastorerep.pdf')































    #Exit System
    elif decfac == 11:
        if os.path.exists(r'userblock.txt'):
            userblock.close()
            os.remove(r'userblock.txt')
        if os.path.exists(r'userblock.zconf'):
            userblock.close()
            os.remove(r'userblock.zconf')
        toaster.show_toast("DFBA Framework Runtime Broker", "Obsufcating program...", duration = 2)
        logoprintxrt()
        floodscreen()
        time.sleep(2)
        break
        os.close('securepack.pyw')
    elif decfac == 7:
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
        print("CIT INTERNAL TESTING MODE")
        ffxfac = str(input("Enter CIT Testing Mode? (y/n):: "))
        if ffxfac == "y":
            ffrxfac = str(input("Entering CIT may lead to data loss. Confirm entering CIT? (y/n):: "))
            if ffrxfac == "y":
                print("DNSS CIT MODE")
                print(" ")
                print(" ")
                print("CIT Options::")
                print("Enter '1' to CLEAR ALL CUSTOMER RECORDS")
                print("Enter '2' to CLEAR ALL VOUCHERS/ COUPONS")
                print("Enter '3' to exit CIT")
                citfacin = int(input("Waiting for input:: "))
                if citfacin == 1:
                    # window.close()
                    os.startfile(r'securepack.py')
                if citfacin == 2:
                    # window.close()
                    os.startfile(r'securepackxvc.py')
                else:
                    continue
        
            else:
                continue
        
        elif ffxfac == "n":
            print("Exiting CIT")
            time.sleep(1)
            continue
        else:
            print("Invalid input. . . . ")
            time.sleep(1)
        
    else:
        print("Critical Error! DNSS error code: ninp01279; Option doesn't exist")
        time.sleep(5)
        continue

# End of program
# Available on github: www.github.com/deltaonealpha/DBFA
# https://deltaonealpha.github.io/DBFA/
