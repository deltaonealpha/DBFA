'''
██▀▀ ██  ██▀▀▀██   ██▀▀▀▀  ██▀▀▀██  ██▀▀▀▀██ 
██   ██  ██   ██   ██      ██   ██  ██    ██ CLI
██   ██  ██▀▀▀▀██  ██▀▀    ██▬▬▬██           Store
██___██  ██    ██  ██      ██   ██  ████████ Manager

by deltaonealpha and sushimuncher

package dbfafartingspider
* The program FartingSpider implements an application that
* houses a solution for complete store management.
*
* @author deltaonealpha
'''
###########################################################################
# vs                                                                      #
# Administrator == all                                                    #
# Sales = ['1', "2a", '2b', '2c', '2d', '3a', '3b', '3d', 5, 9, 10, 12 ]  #
###########################################################################

import traceback
import json, requests, time, urllib, sys

import os, time
global curdir, parentdir, fontsdir
currdir = str(os.getcwd())
from pathlib import Path
path = Path(os.getcwd())
parentdir = str(Path(path.parent))
userdir = os.path.expanduser('~')
fontsdir = str(os.path.join(userdir, 'AppData\Local\Microsoft\Windows\Fonts\MiLanProVF.ttf')) 

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout
        print()

def settingscommonfetch(SettingsType):
    import sqlite3
    settings = sqlite3.connect(r'dbfasettings.db')
    settingsx = settings.cursor()
    settingsx.execute(("SELECT Value from settings WHERE SettingsType = ?"), (SettingsType,))
    settingsfetch = (settingsx.fetchall()[0][0])
    return settingsfetch

def settingsdatafetch(SettingsType):
    import sqlite3
    settings = sqlite3.connect(r'dbfasettings.db')
    settingsx = settings.cursor()
    settingsx.execute(("SELECT Notes from settings WHERE SettingsType = ?"), (SettingsType,))
    settingsfetch = (settingsx.fetchall()[0][0])
    return settingsfetch

def securedatafetch(SettingsType):
    import sqlite3
    settings = sqlite3.connect(r'dbfasettings.db')
    settingsx = settings.cursor()
    settingsx.execute(("SELECT Col1 from passkeyhandler WHERE Sno = ?"), (SettingsType,))
    settingsfetch = (settingsx.fetchall()[0][0])
    return settingsfetch

def telegram_bot_sendtext(bot_message):
    with HiddenPrints():
        bot_token = str(securedatafetch(2))
        bot_chatID = str(securedatafetch(3))
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        return response.json()

URL = "https://api.telegram.org/bot{}/".format('1215404401:AAEvVBwzogEhOvBaW5iSpHRbz3Tnc7fCZis')

def settingsmodifier(SettingsType, NewValue):
    import sqlite3
    settings = sqlite3.connect(r'dbfasettings.db')
    settingsx = settings.cursor()
    settingsx.execute(("UPDATE settings SET Value = ? WHERE SettingsType = ?"), (NewValue, SettingsType))
    settings.commit()

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def echo_all(updates):
    for update in updates["result"]:
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        send_message(text, chat)

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = '680917769'
    return (text, chat_id)


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, '680917769')
    get_url(url)


def dmain():
    #print(settingscommonfetch(9))
    #get_url('https://api.telegram.org/bot/deleteWebhook')
    with open('lastupdateid2.txt', 'a+') as file:
        file.close()
    with open('lastupdateid2.txt', 'r+') as file:
        xid = file.read()
    #print(xid)
    last_update_id = int(xid)
    #print(last_update_id)
    import webbrowser
    updates = get_updates(last_update_id)
    #print(updates)
    #time.sleep(5)
    #print(len(updates["result"]))
    if len(updates["result"]) > 0:
        #print("ddcc")
        last_update_id = get_last_update_id(updates)
        #print(last_update_id)
        for update in updates["result"]:
            #print(update["message"]["text"])
            try:
                if (update["message"]["text"]).replace(" ", "") == "disableDBFA":
                    settingsmodifier(9, 0)
                    time.sleep(0.5)
                    telegram_bot_sendtext("delta Webhook Services\nUsage permissions have been revoked from your installation of DBFA.\n\nExpect access to be stopped from the next boot/ menu cycle.\nhttps://dashboard.deltaone.tech/dbfa.html")
                    print("delta Webhook Prompt: ")
                    print("A webbrowser window will shortly open ~")
                    webbrowser.open('https://dashboard.deltaone.tech/dbfa.html')
                    with open('lastupdateid2.txt', 'a+') as file:
                        file.close()
                    with open('lastupdateid2.txt', 'r+') as file:
                        settingsmodifier(9, 0)
                        time.sleep(0.5)
                        file.truncate(0)
                        file.write('%d'%last_update_id)
                    time.sleep(5)
                    settingsmodifier(9, 0)
                    print("DBFA will now exit.")
                    time.sleep(0.5)
                    os._exit(0)
                    os._exit(1)
                    os._exit(0)
                elif (update["message"]["text"]).replace(" ", "") == "enableDBFA":
                    if settingscommonfetch(9) == 0:
                        settingsmodifier(9, 1)
                        print("delta Webhook Prompt: ")
                        telegram_bot_sendtext("delta Webhook Services\n\nAccess has been re-granted on your installation of DBFA.")
                        print("The administrator of this DBFA installation has re-allowed access to DBFA on this device!")
                        time.sleep(3)
                else:
                    if settingscommonfetch(9) == 0:
                        with open('lastupdateid2.txt', 'a+') as file:
                            file.close()
                        with open('lastupdateid2.txt', 'r+') as file:
                            file.truncate(0)
                            file.write('%d'%last_update_id)
                        print("A webbrowser window will shortly open ~")
                        print("delta Webhook Prompt: ")
                        webbrowser.open('https://dashboard.deltaone.tech/dbfa.html')
                        print("DBFA will now exit.")
                        time.sleep(5)
                        os._exit(0)
                        os._exit(1)
                        os._exit(0)
                    else:
                        pass
            except KeyError:
                print("Do not send images to DBFA communicator on Telegram!")
        with open('lastupdateid2.txt', 'a+') as file:
            file.close()
        with open('lastupdateid2.txt', 'r+') as file:
            file.truncate(0)
            file.write('%d'%last_update_id)
        #echo_all(updates)

    else:
        if settingscommonfetch(9) == 0:
            with open('lastupdateid2.txt', 'a+') as file:
                file.close()
            with open('lastupdateid2.txt', 'r+') as file:
                file.truncate(0)
                file.write('%d'%last_update_id)
            print("A webbrowser window will shortly open ~")
            print("delta Webhook Prompt: ")
            webbrowser.open('https://dashboard.deltaone.tech/dbfa.html')
            print("DBFA will now exit.")
            time.sleep(5)
            os._exit(0)
            os._exit(1)
            os._exit(0)

try:
    import getpass, time, pathlib, sqlite3, sys, os #sys, os for system-level ops
    from tabularprint import table
    from tqdm import tqdm 
    import webbrowser
    dmain()
    # Credits to XanderMJ (https://github.com/XanderMJ/spotilib) for Spotify controls
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
    pdfmetrics.registerFont(TTFont('MiLanProVF', str(currdir+r'\\MiLanProVF.ttf')))
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


    def settingscommonfetch(SettingsType):
        import sqlite3
        settings = sqlite3.connect(r'dbfasettings.db')
        settingsx = settings.cursor()
        settingsx.execute(("SELECT Value from settings WHERE SettingsType = ?"), (SettingsType,))
        settingsfetch = (settingsx.fetchall()[0][0])
        return settingsfetch

    def settingscommondumpfetch(SettingsType):
        import sqlite3
        settings = sqlite3.connect(r'dbfasettings.db')
        settingsx = settings.cursor()
        settingsx.execute(("SELECT Notes from settings WHERE SettingsType = ?"), (SettingsType,))
        settingsfetch = (settingsx.fetchall()[0][0])
        return settingsfetch

    def settingsmodifier(SettingsType, NewValue):
        import sqlite3
        settings = sqlite3.connect(r'dbfasettings.db')
        settingsx = settings.cursor()
        settingsx.execute(("UPDATE settings SET Value = ? WHERE SettingsType = ?"), (NewValue, SettingsType))
        settings.commit()

    def permssetter(NewValue):
        import sqlite3
        settings = sqlite3.connect(r'dbfasettings.db')
        settingsx = settings.cursor()
        settingsx.execute(("UPDATE settings SET Notes = ? WHERE SettingsType = 10"), (NewValue, ))
        settings.commit()



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

    import sqlite3
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
            bot_token = str(securedatafetch(2))
            bot_chatID = str(securedatafetch(3))
            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
            response = requests.get(send_text)
            return response.json()
        
    def telegram_bot_grouptext(bot_message):    
        with HiddenPrints():
            bot_token = str(securedatafetch(2))
            bot_chatID = str(securedatafetch(4))
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
        #VID: DBFA Inception 1.0
        print("        ___ ______ ___   _____________    ____________     _______")
        time.sleep(0.01)
        print("       /  /_______/  /  /  /_______/  /  /  /________/    /  /_/ /")
        time.sleep(0.01)
        print("      /  /       /  /  /  /       /  /  /  /             /  /  / /")
        time.sleep(0.01)
        print("     /  /       /  /  /  /_______/  /  /  /  CLI        /  /   / /")
        time.sleep(0.01)
        print("    /  /       /  /  / // // // // /  /  /_________    /  /____/ /")
        time.sleep(0.01)
        print("   /  /       /  /  /  /-------/  /  /  /_________/   /  /_____/ /")
        time.sleep(0.01)
        print("  /  /       /  /  /  /       /  /  /  /             /  /      / /")
        time.sleep(0.01)
        print(" /  /_______/  /  /  /______ /  /  /  /             /  /       / /")
        time.sleep(0.01)
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


    os.system('cls')



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
        import sqlite3, time, random, requests
        start = time.time()
        from datetime import datetime, timedelta

        from datetime import datetime, timedelta
        now = datetime.now()
        now = now + timedelta(days=1)
        dt_string = now.strftime("%Y-%m-%d")
        empmas = sqlite3.connect(r'dbfaempmaster.db')
        empmascur = empmas.cursor()
        empmascur.execute("SELECT MAX(Date) FROM scheddelivery")
        datie = empmascur.fetchall()[0][0]
        if datie != dt_string:
            def telegram_bot_sendtext(bot_message):
                bot_token = str(securedatafetch(2))
                bot_chatID = str(securedatafetch(3))
                send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
                response = requests.get(send_text)
                return response.json()

            today = datetime.now().date()
            start = today + timedelta(days=1)

            def leaveget(Oid):
                today = datetime.now().date()
                empmas = sqlite3.connect(r'dbfaempmaster.db')
                empmascur = empmas.cursor()
                empmascur.execute("SELECT * FROM leave WHERE Oid = ? AND Date = ?", ('%s'%Oid, '%s'%start, ))
                datastream = empmascur.fetchall()
                if len(datastream) != 0:
                    return(datastream[0][0])
                else:
                    return None

            def gethoursavg(Oid):
                empmas = sqlite3.connect(r'dbfaempmaster.db')
                empmascur = empmas.cursor()
                empmascur.execute("SELECT * FROM attendance WHERE OiD = ? ORDER BY Date ASC, Time", ('%s'%Oid,))
                count = 0
                rows = empmascur.fetchall()
                datelist = []
                for i in rows:
                    datelist.append(i[0])
                a = [i for i in rows if datelist.count(i[0])>1]
                netr = (len(datelist) - len(a)) * 8
                ini_list = [i[2] for i in a]
                from datetime import timedelta   
                diff_list = [] 
                for x, y in zip(ini_list[0::], ini_list[1::]): 
                    t1 = str((timedelta(hours=int(y.split(':')[0]), minutes=int(y.split(':')[1])) - timedelta(hours=int(x.split(':')[0]), minutes=int(x.split(':')[1])))).split(':')[0]
                    diff_list.append(t1)
                del diff_list[1::2]
                for i in range(0, len(diff_list)): 
                    diff_list[i] = int(diff_list[i]) 
                if int(netr) > 0:
                    diff_list.append(netr) 
                return (sum(diff_list)/len(diff_list))


            def autospacer(word):
                #print(((17-len(word))//2))
                if len(word) % 2 == 0:
                    return (((17-len(word))//2)*" " + str(word) + ((17-len(word))//2)*" " + " ")
                else:
                    #print(word)
                    return ((17-len(word))//2)*" " + str(word) + ((17-len(word))//2)*" "


            def getschedvals(Oid):
                empmas = sqlite3.connect(r'dbfaempmaster.db')
                empmascur = empmas.cursor()
                empmascur.execute("SELECT Name, Post FROM emp WHERE OiD = ?", ('%s'%Oid,))
                daysrt = empmascur.fetchall()
                return daysrt[0][0]


            def getSales():
                empmas = sqlite3.connect(r'dbfaempmaster.db')
                empmascur = empmas.cursor()
                empmascur.execute("SELECT OiD FROM emp WHERE Post = ?", ('Sales',))
                daysrt = empmascur.fetchall()
                return [daysrt[0][0], daysrt[1][0],  daysrt[2][0]]

            def getMaintanence():
                empmas = sqlite3.connect(r'dbfaempmaster.db')
                empmascur = empmas.cursor()
                empmascur.execute("SELECT OiD FROM emp WHERE Post = ?", ('Maintanence',))
                daysrt = empmascur.fetchall()
                return [daysrt[0][0], daysrt[1][0]]

            def getLogistics():
                empmas = sqlite3.connect(r'dbfaempmaster.db')
                empmascur = empmas.cursor()
                empmascur.execute("SELECT OiD FROM emp WHERE Post = ?", ('Logistics',))
                daysrt = empmascur.fetchall()
                return [daysrt[0][0], daysrt[1][0]]

            def timex(Oid):
                if gethoursavg(1) < 8:
                    return ((8-gethoursavg(1))/10)*600
                else:
                    return 0

            rand = (random.randint(1, 4))

            if rand == 1:
                if leaveget(getSales()[0]) is None:
                    r11 = getschedvals(getSales()[0])
                else:
                    r11 = getschedvals(getSales()[2])+ " & " +getschedvals(getSales()[1])
                t11 = str((int(1400+timex(3))))
                
                if leaveget(getSales()[1]) is None:
                    r12 = getschedvals(getSales()[1])
                else:
                    r12 = getschedvals(getSales()[0]) + " & " + getschedvals(getSales()[2])
                t12 = str(int(2200+timex(4)))

                if leaveget(getSales()[2]) is None:
                    r13 = getschedvals(getSales()[2])
                else:
                    r13 = getschedvals(getSales()[1]) + " & " + getschedvals(getSales()[0])
                t13 = str("0"+str(int(600+timex(5))))

                if leaveget(getMaintanence()[0]) is None:
                    r21 = getschedvals(getMaintanence()[0])
                else:
                    r21 = getschedvals(getMaintanence()[1])
                t21 = str((int(1400+timex(6))))

                if leaveget(getMaintanence()[1]) is None:
                    r22 = getschedvals(getMaintanence()[1])
                else:
                    r22 = getschedvals(getMaintanence()[0])
                t22 = str(int(2200+timex(7)))
                
                if leaveget(getLogistics()[0]) is None:
                    r31 = getschedvals(getLogistics()[0])
                else:
                    r31 = getschedvals(getLogistics()[1])
                t31 = str((int(1400+timex(8))))
                
                if leaveget(getLogistics()[1]) is None:
                    r33 = getschedvals(getLogistics()[1])
                else:
                    r31 = getschedvals(getLogistics()[0])
                t33 = str("0"+str((int(600+timex(9)))))


            if rand == 2:
                if leaveget(getSales()[2]) is None:
                    r11 = getschedvals(getSales()[2])
                else:
                    r11 = getschedvals(getSales()[0])+ " & " +getschedvals(getSales()[1])
                t11 = str((int(1400+timex(3))))
                
                if leaveget(getSales()[1]) is None:
                    r12 = getschedvals(getSales()[1])
                else:
                    r12 = getschedvals(getSales()[0]) + " & " + getschedvals(getSales()[2])
                t12 = str(int(2200+timex(4)))

                if leaveget(getSales()[0]) is None:
                    r13 = getschedvals(getSales()[0])
                else:
                    r13 = getschedvals(getSales()[2]) + " & " + getschedvals(getSales()[1])
                t13 = str("0"+str(int(600+timex(5))))

                if leaveget(getMaintanence()[1]) is None:
                    r21 = getschedvals(getMaintanence()[1])
                else:
                    r21 = getschedvals(getMaintanence()[0])
                t21 = str((int(1400+timex(6))))

                if leaveget(getMaintanence()[0]) is None:
                    r22 = getschedvals(getMaintanence()[0])
                else:
                    r22 = getschedvals(getMaintanence()[1])
                t22 = str(int(2200+timex(7)))
                
                if leaveget(getLogistics()[0]) is None:
                    r31 = getschedvals(getLogistics()[0])
                else:
                    r31 = getschedvals(getLogistics()[1])
                t31 = str((int(1400+timex(8))))
                
                if leaveget(getLogistics()[1]) is None:
                    r33 = getschedvals(getLogistics()[1])
                else:
                    r31 = getschedvals(getLogistics()[0])
                t33 = str("0"+str((int(600+timex(9)))))


            if rand == 3:
                if leaveget(getSales()[1]) is None:
                    r11 = getschedvals(getSales()[1])
                else:
                    r11 = getschedvals(getSales()[0])+ " & " +getschedvals(getSales()[2])
                t11 = str((int(1400+timex(3))))
                
                if leaveget(getSales()[0]) is None:
                    r12 = getschedvals(getSales()[0])
                else:
                    r12 = getschedvals(getSales()[2]) + " & " + getschedvals(getSales()[1])
                t12 = str(int(2200+timex(4)))

                if leaveget(getSales()[2]) is None:
                    r13 = getschedvals(getSales()[2])
                else:
                    r13 = getschedvals(getSales()[1]) + " & " + getschedvals(getSales()[0])
                t13 = str("0"+str(int(600+timex(5))))

                if leaveget(getMaintanence()[1]) is None:
                    r21 = getschedvals(getMaintanence()[1])
                else:
                    r21 = getschedvals(getMaintanence()[0])
                t21 = str((int(1400+timex(6))))

                if leaveget(getMaintanence()[0]) is None:
                    r22 = getschedvals(getMaintanence()[0])
                else:
                    r22 = getschedvals(getMaintanence()[1])
                t22 = str(int(2200+timex(7)))
                
                if leaveget(getLogistics()[1]) is None:
                    r31 = getschedvals(getLogistics()[1])
                else:
                    r31 = getschedvals(getLogistics()[0])
                t31 = str((int(1400+timex(8))))
                
                if leaveget(getLogistics()[0]) is None:
                    r33 = getschedvals(getLogistics()[0])
                else:
                    r31 = getschedvals(getLogistics()[1])
                t33 = str("0"+str((int(600+timex(9)))))


            if rand == 4:
                if leaveget(getSales()[2]) is None:
                    r11 = getschedvals(getSales()[2])
                else:
                    r11 = getschedvals(getSales()[0])+ " & " +getschedvals(getSales()[1])
                t11 = str((int(1400+timex(3))))
                
                if leaveget(getSales()[0]) is None:
                    r12 = getschedvals(getSales()[0])
                else:
                    r12 = getschedvals(getSales()[1]) + " & " + getschedvals(getSales()[2])
                t12 = str(int(2200+timex(4)))

                if leaveget(getSales()[1]) is None:
                    r13 = getschedvals(getSales()[1])
                else:
                    r13 = getschedvals(getSales()[2]) + " & " + getschedvals(getSales()[0])
                t13 = str("0"+str(int(600+timex(5))))

                if leaveget(getMaintanence()[0]) is None:
                    r21 = getschedvals(getMaintanence()[0])
                else:
                    r21 = getschedvals(getMaintanence()[1])
                t21 = str((int(1400+timex(6))))

                if leaveget(getMaintanence()[1]) is None:
                    r22 = getschedvals(getMaintanence()[1])
                else:
                    r22 = getschedvals(getMaintanence()[0])
                t22 = str(int(2200+timex(7)))
                
                if leaveget(getLogistics()[1]) is None:
                    r31 = getschedvals(getLogistics()[1])
                else:
                    r31 = getschedvals(getLogistics()[0])
                t31 = str((int(1400+timex(8))))
                
                if leaveget(getLogistics()[0]) is None:
                    r33 = getschedvals(getLogistics()[0])
                else:
                    r31 = getschedvals(getLogistics()[1])
                t33 = str("0"+str((int(600+timex(9)))))

            sched = ('''                Schedule for ''' + str(start) + '''
delta           █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ ▀
Scheduler       █   0600 - '''+t11+'''   █   1400 - '''+t12+'''   █   2200 - '''+t13+'''   █ ▀
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ ▀
SALES           █'''+autospacer(r11)+'''█'''+autospacer(r12)+'''█'''+autospacer(r13)+'''█ ▀
                ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ▀

delta           █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ ▀                
Scheduler       █   0600 - '''+t21+'''   █   1400 - '''+t22+'''   █   2200 - 0600   █ ▀
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ ▀
MAINTANENCE     █'''+autospacer(r21)+'''█'''+autospacer(r22)+'''█ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ █ ▀
                ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ▀

delta           █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ ▀                
Scheduler       █   0600 - '''+t31+'''   █   1400 - 2200   █   2200 - '''+t33+'''   █ ▀
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ ▀                
LOGISTICS       █'''+autospacer(r31)+'''█ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ █'''+autospacer(r33)+'''█ ▀
                ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ▀
            ''')

            print("Tomorrow's shift schedule:: \n")
            bot_message = '''DBFA Automated Scheduler
Schedule for tomorrow (''' + str(start) + ''')

Sales Staff
0600 - '''+t11+''': '''+r11+'''
1400 - '''+t12+''': '''+r12+'''
2200 - '''+t13+''': '''+r13+'''
    
Maintanence Staff
0600 - '''+t21+''': '''+r21+'''
1400 - '''+t22+''': '''+r22+'''

Logistics Staff
0600 - '''+t31+''': '''+r31+'''
2200 - '''+t33+''': '''+r33+'''

You are recieving this shift schedule as your store is serviced by DBFA.

This is a dynamically generated schedule with alternating shifts. Employees on leave are taken care of and adjusted accordingly.'''

            from datetime import datetime, timedelta
            now = datetime.now()
            now = now + timedelta(days=1)
            dt_string = now.strftime("%Y-%m-%d")
            empmas = sqlite3.connect(r'dbfaempmaster.db')
            empmascur = empmas.cursor()
            empmascur.execute("INSERT INTO scheddelivery(Date) VALUES (?)", (dt_string,))
            empmas.commit()

            telegram_bot_grouptext(bot_message.replace("&", "and"))
            time.sleep(0.5)
            telegram_bot_sendtext(bot_message.replace("&", "and"))            
            print(sched)
            contfac = input("Enter a button to continue ~ : ")
            with open('lastsched.txt', 'a+') as file:
                file.close()
            with open('lastsched.txt', 'w+', encoding="utf-8") as file:
                file.truncate(0)
                file.write(sched)
                file.close()

        else:
            pass        


        dmain()
        
        from datetime import datetime, date
        now = datetime.now()
        dt_string = now.strftime("%d")  #datetime object containing current date and time 
        #print(dt_string)
        if dt_string in ("01", "02", "03", "04", "05"):
            print("Salary days: Pay salaries between 01st - 05th of every month. Open DBFA Employee Manager to pay ~")
        from colorama import init, Fore, Back, Style #color-settings for the partner/sponsor adverts
        init(convert = True)
        url = "https://raw.githubusercontent.com/deltaonealpha/DBFA_UpdateHandler/master/updates.txt"
        r = requests.get(url)
        dbfaver = ((str(r.content.decode('utf-8'))))[4:]
        xdbfaver = ((str(r.content.decode('utf-8'))))
        with open(str(parentdir+'\\updates.txt'), 'r+') as upread:
            upread = (str(upread.read())).strip()
        #print("Server: ", dbfaver, "\nLocal: ", upread[4: ])
        spass1 = []
        spass2 = []
        for i in dbfaver:
            spass1.append(i)
        for j in upread[4: ]:
            spass2.append(j)
        try:
            if float(upread[4: ]) > float(dbfaver):
                pass
        except:
            print("Error with updater. Error code : *bckshln12* ༼ つ ◕_◕ ༽つ  つ ༽ ◕_◕ つ༼")
        else:
            if spass1 != spass2:
                print("A new DBFA update is available: DBFA", dbfaver)
            #elif spass1 == spass2:
                #print("DBFA is up-to-date")
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
        logoxold = (Fore.CYAN+''' 
                            Options:  
█▀▀█ █▀█  █▀▀ █▀█  █▀▀█   1  - Issue a Bill                                              4  - Store Report
█__█ █▀▀█ █▀  █▬█  ▄▄▄▄   2  - Manage Customers:                                         5  - Manage Deliveries
CLIENT Inception 1.0                a: Register a Customer    c: Purchase Records        6  - DBFA Options 
'''+Fore.MAGENTA+'''  The OG Store Manager'''+Fore.CYAN+'''              b: Customer Registry      d: Find a Customer         7  - Start DBFA Backup & Switch 
                                    e: Export data as CSV                                8  - Analyse Sales
                          3  - Store Options:                                          '''+Fore.MAGENTA+'''emp/EMP - DBFA Employee Manager'''+Fore.CYAN+'''
                                           a: Manage Stock           c: Manage Vouchers         9 - About DBFA
                                    b: DBFA Stock Master      d: Product Listing         10 - Check for updates
                                    e: Sales Log              f: Export data as CSV      11 - Quit
                                    g: Invoice Deep Archive                              
- 'mark'/'MARK': to mark attendance                                                                                                                            
'''+Fore.MAGENTA+'''                          
DBFA Music Controls:: *prev* - << previous | *pause* - <|> pause/play | *next* - >> next  '''+Fore.CYAN+'''
-----------------------------------------------------------------------------------------------------------------------''')


        logoxnew = (Fore.CYAN+'''Options:
1  - Issue a Bill                                              4  - Store Report
2  - Manage Customers:                                         5  - Manage Deliveries
        a: Register a Customer    c: Purchase Records          6  - DBFA Options
        b: Customer Registry      d: Find a Customer           7  - DBFA Backup & Switch 
        e: Export data as CSV                                  8  - Analyse Sales
3  - Store Options:                                            '''+Fore.MAGENTA+'''emp/EMP - DBFA Employee Manager'''+Fore.CYAN+'''
        a: Manage Stock           c: Manage Vouchers           9  - About DBFA 
        b: DBFA Stock Master      d: Product Listing           10 - Check for updates
        e: Sales Log              f: Export data as CSV        11 - Quit
        g: Invoice Deep Archive                                
- 'mark'/'MARK': to mark attendance                               
'''+Fore.MAGENTA+'''                                                                 
What would you like to do?                        The OG Store Manager'''+Fore.WHITE+''' █▀▀█ █▀█  █▀▀ █▀█  █▀▀█'''+Fore.CYAN+'''
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ '''+Fore.WHITE+'''█__█ █▀▀█ █▀  █▬█  ▄▄▄▄'''+Fore.CYAN+'''
DBFA Music Controls: *prev* <<< | *pause* <|> | *next* >>>             INCEPTION 1.0 CLIENT   \n'''
+Back.CYAN+Fore.BLACK+'''Administrator Controls'''+Back.BLACK+Fore.CYAN+'''                              
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬''')
#  '''+Fore.RED+'''
#  '''+Fore.CYAN+'''
        logoxnewrestrictedperms = (Fore.CYAN+'''Options:
1  - Issue a Bill                                              
2  - Manage Customers:                                         5  - Manage Deliveries
        a: Register a Customer    c: Purchase Records          
        b: Customer Registry      d: Find a Customer           
                                                               
3  - Store Options:                                            '''+Fore.MAGENTA+'''emp/EMP - DBFA Employee Manager'''+Fore.CYAN+'''
        a: Manage Stock                                        9  - View Software License
        b: DBFA Stock Master      d: Product Listing           10 - About DBFA 8.4
                                                               
                                                               12 - Quit
- 'mark'/'MARK': to mark attendance                               
'''+Fore.MAGENTA+'''                                                                 
What would you like to do?                        The OG Store Manager'''+Fore.WHITE+''' █▀▀█ █▀█  █▀▀ █▀█  █▀▀█'''+Fore.CYAN+'''
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ '''+Fore.WHITE+'''█__█ █▀▀█ █▀  █▬█  ▄▄▄▄'''+Fore.CYAN+'''
DBFA Music Controls: *prev* <<< | *pause* <|> | *next* >>>             INCEPTION 1.0 CLIENT  \n'''
+Back.RED+Fore.BLACK+'''Restricted access mode'''+Back.BLACK+Fore.CYAN+'''                               
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬''')

        # To underline What would you like to do?::                                                                            
        if settingscommonfetch(7) == 1:
            if delcount != 0:
                print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                lener1 = "Profit (last week): " + '%s'%pro7d
                print(lener1 + (62-len(lener1))*" ", "Profit (today): ", protd)
                #pro7d, (56-len(str(pro7d)))*" ", "DONNAGER 8.01 RC-2 Test Beta")
                print(Back.BLACK + Fore.MAGENTA+ "Pending deliveries: " + str(delcount) + " "  + "           DBFA User: " + os.getlogin() + "             "+ dt_string + Fore.CYAN)
                print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            else:
                print(Fore.BLACK + Back.CYAN + "No deliveries pending! " + Back.BLACK + Fore.CYAN)
            if str(settingscommondumpfetch(10)) == "Administrator":
                print(logoxnew)
            elif str(settingscommondumpfetch(10)) in ("Sales - 1", "Sales - 2", "Sales - 3"):
                print(logoxnewrestrictedperms)
        else:
            if delcount != 0:
                print("-----------------------------------------------------------------------------------------------------------------------")
                lener1 = "Profit (last week): " + '%s'%pro7d
                print(lener1 + (95-len(lener1))*" ", "   Profit (today): ", protd)
                #pro7d, (56-len(str(pro7d)))*" ", "DONNAGER 8.01 RC-2 Test Beta")
                print(Back.BLACK + Fore.MAGENTA+ "Pending deliveries: " + str(delcount) + " "  + "       DBFA User: " + os.getlogin() + "              "+ dt_string + Fore.CYAN)
                print("-----------------------------------------------------------------------------------------------------------------------")
            else:
                print(Fore.BLACK + Back.CYAN + "No deliveries pending! " + Back.BLACK + Fore.CYAN)
            print(logoxold)
        #Settings Checker
        if settingscommonfetch(3) == 1:
            time.sleep(0.2)
            try:
                if spotify.current() not in ("", " ", [], (), None):
                    print("Currently playing:", Fore.MAGENTA , spotify.current()[0], Fore.CYAN, "by ", Fore.MAGENTA, spotify.current()[1], Fore.CYAN)
                else:
                    print(Fore.MAGENTA, "No music playing. Use Spotify to play your favourite music and control it via DBFA", Fore.CYAN)
            except Exception as e:
                print(Fore.MAGENTA, "No music playing. Play your favourite music and control it via DBFA", Fore.CYAN)
            if settingscommonfetch(7) == 1:
                print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬", Fore.MAGENTA)
            else:
                print("-----------------------------------------------------------------------------------------------------------------------", Fore.MAGENTA)
        else:
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("Re-enable DBFA Music Controls Service from the settings to be able to control your music ")
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

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
                print("You have loyalty points: ", lylpoints, "worth: ₹", lylpoints)
                time.sleep(0.5)
                pointscheck = input("Use " + '%s'%total + " points (y/n)? ")
                print(Fore.LIGHTBLUE_EX + "-----------------" + Fore.WHITE)
                if pointscheck == "y":
                    if total > lylpoints:
                        redeemam = lylpoints
                    else:
                        redeemam = total
                    getOTP()
                    emailfetch(custid)
                    print("Please wait..")
                    email = str(securedatafetch(5))
                    password = str(securedatafetch(1))
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
                    os.startfile(r'Process_Handlers\\emailprocesswindow.pyw')
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
                            return total

                        else:
                            redeemindic = 1
                            netpay = total
                            pointsuse(custid, total)
                            time.sleep(0.3)
                            total = 0
                            print("Points redeemed worth: ", lylpoints)
                            return total
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
                                return total
                            else:
                                netpay = 0
                                pointsuse(custid, total)
                                time.sleep(0.3)
                                total = 0
                                print("Points redeemed worth: ", lylpoints)
                                return total
                        else:
                            print("Wrong OTP. (0) attempt(s) remaining")
                            time.sleep(0.2)
                elif pointscheck == "n":
                    redeemindic = 0
                    netpay = total
                    return total
                else:
                    pass
                time.sleep(1)
                os.system(command)
            else:
                netpay = total
                return total
            
        else:
            redeemindic = 0
            netpay = total
            redeemindic = 0
            lylpoints = 0
            netpay = total
            return total


    global custname, email, idd

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
                        print(tabulate(zip(col_labels, ccrt), floatfmt = ".4f", tablefmt='fancy_grid'))

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
                    print(tabulate(zip(col_labels, ccrt), floatfmt = ".4f", tablefmt='fancy_grid'))
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
                    print(tabulate(zip(col_labels, ccrt), floatfmt = ".4f", tablefmt='fancy_grid'))
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
            csvex=sql.connect(currdir+'\\DBFA.db')
            cursor = csvex.cursor()
            cursor.execute("select * from cust")
            print("Fetching data from database - I...")
            with open("DBFAcustrec.csv", "w") as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in cursor.description])
                csv_writer.writerows(cursor)
                csvexx=sql.connect(currdir+'\\DBFA_CUSTCC.db')
                print("Fetching data from database - II...")
                cursorx = csvexx.cursor()
                cursorx.execute("select * from custcc")
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in cursorx.description])
                csv_writer.writerows(cursorx)    
            dirpath = os.getcwd() + "/DBFAcustrec.csv"
            print("Data exported Successfully into {}".format(dirpath))
            time.sleep(2)

            #Settings Checker
            if settingscommonfetch(4) == 1:
                os.startfile(r"DBFAcustrec.csv")
            else:
                pass

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
        from colorama import init, Fore, Back, Style #color-settings for the partner/sponsor adverts
        init(convert = True)
        time.sleep(1)
        print(Fore.MAGENTA+'''
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Options:                              Store Options >>> DBFA Stock Master v1
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    a: Order New Stock
    b: Update Delivery Status
    c: MASS - Fetch Current Status
    d: INDVL - Fetch Current Status
    e: View Vendor Details
    f: Contact Vendor
    g: Edit Vendor Contact
    h: Modify Low-Stock Warning Bar

What would you like to do?            '''+Fore.WHITE+'''█▀▀ █ █ ██   █▀█▀█ █▀ █▀██ █ █ DBFA'''+Fore.MAGENTA+'''
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  '''+Fore.WHITE+'''▀▀█ █_█ ███  █ ▬ █ █_ █ ▬█ █_█ Manager'''+Fore.MAGENTA+'''
'''+Fore.CYAN+'''Stock Master ~'''+Fore.MAGENTA+'''     
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬'''+Fore.WHITE)
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
        print(tabulate(tablx, headers = titlex, floatfmt = ".4f", tablefmt='fancy_grid'))



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
            csvex=sql.connect(currdir+'\\recmaster.db')
            print("Exporting sales data to CSV....")
            cursor = csvex.cursor()
            cursor.execute("select * from recmasterx")
            with open("DBFAstorerec.csv", "w") as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in cursor.description])
                csv_writer.writerows(cursor)

            dirpath = os.getcwd() + "/DBFAcustrec.csv"
            print("Data exported Successfully into {}".format(dirpath))
            time.sleep(2)

            #Settings Checker
            if settingscommonfetch(4) == 1:
                os.startfile(r"DBFAcustrec.csv")
            else:
                pass

        except Error as e:
            print(e)

        finally:
            pass
    
    def del3g(): #delta DEEP ARCHIVAL VAULT ENGINE
        print("DBFA uses advanced algorithms to store invoice data in easily indecipherable strings.")
        print("These can be used at any point to generate an invoice from any date, given its key is stored with the deep archival VAULT.")
        print("This ensures data protection and enables us to practically store infinity invoices in a relatively non-existent amount of space\n\n")
        print("This option can be used to generate such back-dated invoices.")
        time.sleep(2)
        from DBFADeepArchivalEngine import deepfetch_deeparchival, encoder_deeparchival
        from DBFADeepArchivalEngine import alphadecoder, dttdecoder, decoder_deeparchival
        deepfetch_deeparchival()

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

    #Settings Checker
    if settingscommonfetch(1) == 1:
        floodscreen() #comment to disable boot-flash screen
    else:
        pass


    import requests, time, json, urllib, os, math, random, sqlite3
    from tqdm import tqdm 
    import logging, os, time, requests, socket
    import telegram_send
    from pynput.keyboard import Key, Controller
    # Telegram BOT API 2 (FULL)
    from telegram import InlineKeyboardButton, InlineKeyboardMarkup
    from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    xlogger = logging.getLogger(__name__)

    def telegram_bot_sendtext(bot_message):
        bot_token = str(securedatafetch(2))
        bot_chatID = str(securedatafetch(3))
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        return response.json()

    def start(update, context):
        keyboard = [[InlineKeyboardButton("✅ Validate", callback_data='1'),
                    InlineKeyboardButton("❌ Deny", callback_data='2')]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text("delta 2FA Handler Service\n\n\nValidate login?", reply_markup=reply_markup)


    def button(update, context):
        query = update.callback_query
        # CallbackQueries need to be answered, even if no notification to the user is needed
        # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
        inlet = ("{}".format(query.data))
        if inlet in (1, "1"):
            query.edit_message_text(text="✅ delta 2FA approved! \n\nThis allows your installation of the DBFA client, and its data to be accessed. \n\nIf this wasn't you, contact support and revoke your bot login at the earliest.\n\ndelta Security Service")
            with open(currdir+'\\deltatgstickerlogonew.webp', "rb") as f:
                telegram_send.send(stickers=[f])
                keyboard = Controller()
                print("\n\nValidation recieved! DBFA Client will start in a moment\n\n")
                print("telegram_extended.updtr_pushreq(deltaonealpha, set.webhook: (on, getUpdated.redir(servers.gokku.com/deltaonealpha/arterxt1, callback=False)))")
                print("\n\nif there's no print below for around 5 secs from now, press ctrl+c to continue\n\n")
                keyboard.press(Key.ctrl)
                keyboard.press('c')
                keyboard.release('c')
                keyboard.release(Key.ctrl)

        if inlet in (2, "2"):
            query.edit_message_text(text="❌🔐 Denied delta 2FA request.\n\ndelta Security Service")
            with open(currdir+'\\deltatgstickerlogonew.webp', "rb") as f:
                telegram_send.send(stickers=[f])
            keyboard = Controller()
            print("\n\nThe login request for this session has been DENIED.\n\n")
            time.sleep(1)
            print("telegram_extended.updtr_pushreq(deltaonealpha, set.webhook: (on, getUpdated.redir(servers.gokku.com/deltaonealpha/arterxt1, callback=False)))")
            print("\n\nif there's no print below for around 5 secs from now, press ctrl+c to continue\n\n")
            keyboard.press(Key.ctrl)
            keyboard.press('c')
            keyboard.release('c')
            keyboard.release(Key.ctrl)
            time.sleep(1)
            time.sleep(1)
            print("DBFA Client will now exit! ")
            time.sleep(5)
            os._exit(0)
        if inlet in (3, "3"):
            query.edit_message_text(text="Use */help*")    
        

    def OAuthvalidate():
        from datetime import datetime
        import sqlite3, time, os
        currdir = str(os.getcwd())
        os.system('cls')
        now = datetime.now()
        try: #To avoid error when time is 00:00:00
            netr = int(now.strftime("%H"))*3600 + int(now.strftime("%M"))*60 + int(now.strftime("%S"))
        except:
            time.sleep(1)
            netr = int(now.strftime("%H"))*3600 + int(now.strftime("%M"))*60 + int(now.strftime("%S"))
        oauth = sqlite3.connect(r'dbfasettings.db')
        oauthx = oauth.cursor()
        oauthx.execute("SELECT Value FROM LoginHandler")
        check = oauthx.fetchall()[0][0]
        if check != 1:
            print("Login was bypassed! DBFA will now exit!")
            time.sleep(1)
            os._exit(0)
        oauthx.execute("SELECT count(*) FROM LoginHandler")
        rows = oauthx.fetchall()
        if (rows[0][0]) > 1:
            print("DBFA Authenticator has been tampered with! DBFA WILL EXIT NOW!")
            oauthx.execute("UPDATE LoginHandler SET Value = 0, TimeMark = 0")
            oauth.commit()
            oauth.close()   
            time.sleep(2)
            os._exit(0)
        oauthx.execute("SELECT TimeMark FROM LoginHandler")
        stamp = oauthx.fetchall()[0][0]
        if int(netr)-int(stamp) > 60:
            print("netr")
            oauthx.execute("UPDATE LoginHandler SET Value = 0, TimeMark = 0")
            oauth.commit()
            oauth.close()   
            os.startfile(curdir+'\\authtimeout.pyw')
            time.sleep(1)
            os._exit(0)
        elif int(netr)-int(stamp) < 60:
            print("- - - Login validated - - -\n\n")
            oauthx.execute("SELECT PermSet FROM LoginHandler")
            permset = oauthx.fetchall()[0][0]
            permssetter(permset)
            print("Permissions set: ", settingscommondumpfetch(10))

        else:
            oauthx.execute("UPDATE LoginHandler SET Value = 0, TimeMark = 0")
            oauth.commit()
            oauth.close()   
            print("Login was bypassed! DBFA will now exit!")
            time.sleep(1)
            os._exit(0)
        
        oauthx.execute("UPDATE LoginHandler SET Value = 0, TimeMark = 0")
        oauth.commit()
        oauth.close()    

    OAuthvalidate()


    def help_command(update, context):
        update.message.reply_text("Use /auth when prompted. This bot will only respond when a delta service raises a request. ")


    def main():
        # Create the Updater and pass it your bot's token.
        # Make sure to set use_context=True to use the new context based callbacks
        # Post version 12 this will no longer be necessary
        updater = Updater("1215404401:AAEvVBwzogEhOvBaW5iSpHRbz3Tnc7fCZis", use_context=True)

        updater.dispatcher.add_handler(CommandHandler('auth', start))
        updater.dispatcher.add_handler(CallbackQueryHandler(button))
        updater.dispatcher.add_handler(CommandHandler('help', help_command))

        # Start the Bot
        updater.start_polling()

        # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT
        updater.idle()


    def settingscommonfetch(SettingsType):
        import sqlite3
        settings = sqlite3.connect(r'dbfasettings.db')
        settingsx = settings.cursor()
        settingsx.execute(("SELECT Value from settings WHERE SettingsType = ?"), (SettingsType,))
        settingsfetch = (settingsx.fetchall()[0][0])
        return settingsfetch



    if settingscommonfetch(6) == 1:
        def telegram_bot_sendtext(bot_message):
            bot_token = str(securedatafetch(2))
            bot_chatID = str(securedatafetch(3))
            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
            response = requests.get(send_text)
            return response.json()

        print("delta2 Authenication Service")    
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("DBFA 2FA Service   █▀▀█ █▀█  █▀▀ █▀█  █▀▀█")
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ █__█ █▀▀█ █▀  █▬█  ▄▄▄▄")
        time.sleep(0.5)
        print("")


        print("You have DBFA 2FA activated. Please validate the login from your Telegram account. ")
        for i in tqdm (range (10), desc="Connecting.."):     
            time.sleep(0.00001)    
        if __name__ == '__main__':
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            import platform
            from datetime import datetime  #for reporting the billing time and date
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")  #datetime object containing current date and time
            with open(currdir+'\\deltatgstickerlogonew.webp', "rb") as f:
                telegram_send.send(stickers=[f])
            telegram_bot_sendtext("🔐delta 2FA Handler Service\nA login request has been recieved from your DBFA installation.\n\nRequest time        - " + '%s'%dt_string + f"\nHostname             - {hostname}\n" + f"IP Address             - {ip_address}\n" + "Service Identifier  - "+ platform.system() + platform.release() +"\n\nWARNING:  Do not approve this if this isn't you!\n\nPlease send */auth* to start the validation process: ")
            main()
        os.system('cls')

    else:
        print("DBFA 2FA is disabled. We recommend you to turn it on from the settings for a more secure experience with DBFA client.")


    print("---------------------------------\n\n༼ つ ◕_◕ ༽つ delta IntelliSense Updater\n\n---------------------------------")
    time.sleep(0.1)
    print("Talking to server ~ ")
    url = "https://raw.githubusercontent.com/deltaonealpha/DBFA_UpdateHandler/master/updates.txt"
    r = requests.get(url)
    dbfaver = ((str(r.content.decode('utf-8'))))[4:]
    xdbfaver = ((str(r.content.decode('utf-8'))))
    with open(parentdir+'\\updates.txt', 'r+') as upread:
        upread = (str(upread.read())).strip()
    print("Server: ", dbfaver, "\nLocal: ", upread[4: ])
    spass1 = []
    spass2 = []
    for i in dbfaver:
        spass1.append(i)
    for j in upread[4: ]:
        spass2.append(j)
    if float(upread[4: ]) > float(dbfaver):
        pass

    os.system('cls')


    from win10toast import ToastNotifier
    toaster = ToastNotifier()
    toaster.show_toast("DFBA System","Read documentation prior to use.", duration = 1)
    print("Heyy there,", os.getlogin()) #enable parts in the auth script to enable user detection
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

        #DBFA Mark Attendance
        if decfac in ('attendance', 'ATTENDANCE', 'mark', 'MARK', 'mArK', 'MaRk', 'maRK', 'MArk', 'm a r k', 'M A R K', 'M A r k', 'm a R K'):
            import sqlite3, time, os, requests
            from datetime import datetime  #for reporting the billing time and date
            empmas = sqlite3.connect(r'dbfaempmaster.db')
            empmascur = empmas.cursor()

            empmascur.execute("SELECT DISTINCT * FROM emp")
            dump = empmascur.fetchall()
            Oiddump = []
            for row in dump:
                Oiddump.append(row[0])
            print("OiDs registered: ", Oiddump)
            try:
                Oid = int(input("DBFA MARK ATTENDANCE- Enter your OiD: "))
                trypass = 1
            except:
                print("OiDs are integer-only. Please retry using valid credentials! \n")
                trypass = 0
                
            if trypass == 1:
                if Oid in Oiddump:
                    print("OiD found ")
                    time.sleep(0.5)
                    now = datetime.now()
                    dt_string = now.strftime("%Y/%m/%d")  #datetime object containing current date and time
                    tm_string = now.strftime("%H:%M:%S")  #datetime object containing current date and time
                    empmascur.execute("SELECT count(*) FROM attendance WHERE Date = ? AND OiD = ?", (dt_string, Oid,))
                    data = empmascur.fetchone()[0]
                    if data==0:
                        #print('No record on %s'%dt_string+' for Employee %s'%Oid)
                        #print("insert into attendance(Date, OiD, Time, YN, IO) values(?, ?, ?, ?, ?)", (dt_string, Oid, tm_string, 'Y', 'I'))
                        empmascur.execute("insert into attendance(Date, OiD, Time, YN, IO) values(?, ?, ?, ?, ?)", (dt_string, Oid, tm_string, 'Y', 'I'))
                        #empmascur.execute("UPDATE attendance SET Oid = 'Y' WHERE DATE = ?", (dt_string))
                        empmas.commit()
                        print("\n----------------DBFA-----------------")
                        print("C1 ENTRY: Marked Attendance! OiD: ", Oid)
                        print("-------------------------------------\n")
                    elif data==1:
                        #print('Component %s found in %s row(s)'%(dt_string, data))
                        empmascur.execute("insert into attendance(Date, OiD, Time, YN, IO) values(?, ?, ?, ?, ?)", (dt_string, Oid, tm_string, 'Y', 'O'))
                        empmas.commit()
                        print("\n----------------DBFA-----------------")
                        print("C2 DAY END: Marked Attendance! OiD: ", Oid)
                        print("-------------------------------------\n")
                    elif data > 1:
                        print("You can only mark in/out attendance once a day! \n")

                else:
                    print("OiD not found! \n")

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
            inmaintainer()
            writer = writer + "DBFA Billing Framework" + "\n" + "One-stop solution for all your billing needs!" + "\n" + "\n" + "Billing time: " + dt_string + "\n" + "Customer ID: " + custt + "\n" + "-----------------------------" + "\n" + "Invoice ID: " + '%s'%inval + "\n \n"
            global billiemaster
            billiemaster = 0 #variable for totalling the price
            time.sleep(0.0247) #for a seamless experience
            afac = 0
            dde_productlist = ""
            while(1):
                item = input("Enter product code: ")
                if item == "0":
                    break
                elif item in data:
                    ssxstockmaster(item)
                    if ssxvarscheck == 1:
                        billiemaster+=data[item]
                        dde_productlist += str(item) + '00'
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
                pass        

            if cponid != "":
                isol = sqlite3.connect(r'cponmgmtsys.db')
                isolx = isol.cursor()
                isolx.execute(("SELECT DISTINCT cponid from cponmaster WHERE cponid = ?"), (cponid, ))
                if isolx.fetchall() in ("", " ", [], (), None):
                    print("Invalid voucher identifier! Not applying any!")
                    discount = int(input("Enter discount % (if any): "))
                else:
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
                    netpay = payboxie(custt, total)
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
                        strprofer = ""
                        for i in profer:
                            strprofer+='%s'%i
                        filedel.write("\ndel"+str(delcount+1) + "  Purchased: " + strprofer +"    " + addressx)
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
                        if total > lylpoints:
                            print("Redeemed loyalty points worth: ₹", lylpoints)
                        else:
                            print("Redeemed loyalty points worth: ₹", total)
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

                    # delta DDE - Deep Archival Engine
                    from DBFADeepArchivalEngine import encoder_deeparchival
                    #Data Format: <order ids>///<customer name>///<customer id>///<date and time string>///tax///discount///loyalty///net
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")  #datetime object containing current date and time
                    if redeemindic == 1:
                        data = [dde_productlist, 'dde', custt, dt_string, 18, discount, lylpoints, netpay]
                    else:
                        data = [dde_productlist[:-1], 'dde', custt, dt_string, 18, discount, 0, netpay]
                    encoder_deeparchival(data, inval)
                    
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
                    destination = currdir+'\\Generated_invoices'
                    dest = shutil.move(source, destination)  
                    time.sleep(1.5) #for a seamless experience


                    if custt not in ("", " ", 0, "0") and cccheck == 0:
                        #Settings Checker
                        if settingscommonfetch(2) == 1:
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
                            attachment = open(currdir+'\\\Generated_invoices\\'+'%s'%namer, "rb") 
                            attac= MIMEBase('application', 'octet-stream') 
                            attac.set_payload((attachment).read()) 
                            encoders.encode_base64(attac) 
                            attac.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
                            msg.attach(attac) 
                            os.startfile(r'Process_Handlers\\emailprocesswindow.pyw')
                            email = smtplib.SMTP('smtp.gmail.com', 587)  
                            email.starttls() 
                            email.login(fromaddr, "dbfaidlepass") 
                            message = msg.as_string() 
                            email.sendmail(fromaddr, toaddr, message) 
                            print("Invoice mailed. ")
                            print("-------------------------------------------------------------------------\n\n")
                        #Settings Checker
                        elif settingscommonfetch(1) == 2:
                            pass
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
            from colorama import init, Fore, Back, Style #color-settings for the partner/sponsor adverts
            init(convert = True)
            print(Fore.MAGENTA+'''
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Options:                                               Client >>> Manage Customers
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    a: Register a Customer 
    b: Customer Registry 
    c: Customer Purchase Records 
    d: Find a Customer 
    e: Export Records as CSV 

What would you like to do?                '''+Fore.WHITE+'''█▀▀ █ █ ██   █▀█▀█ █▀ █▀██ █ █ DBFA'''+Fore.MAGENTA+'''
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  '''+Fore.WHITE+'''▀▀█ █_█ ███  █ ▬ █ █_ █ ▬█ █_█ Manager'''+Fore.MAGENTA+'''
'''+Fore.CYAN+'''Manage Customers ~'''+Fore.MAGENTA+'''     
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬'''+Fore.WHITE)
            selected = input("What would you like to do? "+Fore.WHITE)
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
                if str(settingscommondumpfetch(10)) == "Administrator":
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
                else:
                    print("This function is restricted on your account.")

            elif selected not in ("a", "b", "c", "d", "e", "A", "B", "C", "D", "E"):
                print("Please chose a valid option!")
                time.sleep(1)

        #Store Options:
        elif decfac == "3":
            from colorama import init, Fore, Back, Style #color-settings for the partner/sponsor adverts
            init(convert = True)
            print(Fore.MAGENTA+'''
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Options:                                                  Client >>> Store Options
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    a: Manage Stock 
    b: DBFA Stock Master 
    c: Manage Vouchers 
    d: Product Listing 
    e: Sales Log 
    f: Export Sales Data as CSV 
    g: Invoice Deep Archive 

What would you like to do?                '''+Fore.WHITE+'''█▀▀ █ █ ██   █▀█▀█ █▀ █▀██ █ █ DBFA'''+Fore.MAGENTA+'''
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  '''+Fore.WHITE+'''▀▀█ █_█ ███  █ ▬ █ █_ █ ▬█ █_█ Manager'''+Fore.MAGENTA+'''
'''+Fore.CYAN+'''Store Options ~'''+Fore.MAGENTA+'''     
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬'''+Fore.WHITE)
            storeselected = input("What would you like to do? ")
            print("\n")

            if storeselected in ("a", "A"):
                del3a()
                
            elif storeselected in ("b", "B"):
                del3b()

            elif storeselected in ("c", "C"):
                if str(settingscommondumpfetch(10)) == "Administrator":
                    del3c()
                else:
                    print("This function is restricted on your account.")

            elif storeselected in ("d", "D"):
                del3d()            

            elif storeselected in ("e", "E"):
                if str(settingscommondumpfetch(10)) == "Administrator":
                    del3e()
                    logger.write("\n--------------------------------------- \n")
                    logger.write("Sales log accessed! ")
                else:
                    print("This function is restricted on your account.")

            elif storeselected in ("f", "F"):
                if str(settingscommondumpfetch(10)) == "Administrator":
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
                else:
                    print("This function is restricted on your account.")

            elif storeselected in ("g", "G"):
                if str(settingscommondumpfetch(10)) == "Administrator":
                    print("Deep Archival Engine")
                    del3g()
                else:
                    print("This function is restricted on your account.")

            elif storeselected not in ("a", "b", "c", "d", "e", "f", "g", "A", "B", "C", "D", "E", "F", "G"):
                print("Please select a valid option! ")
                time.sleep(1)
                mainmenu()



        #Reports
        elif decfac == "4":
            if str(settingscommondumpfetch(10)) == "Administrator":
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
                isolx.execute(("SELECT prodid, prodname, ordqty, delstat, vendor from stock WHERE delstat = ?"), ("TBD", ))
                rowsrec = isolx.fetchall()
                col_labels = [("P. ID", "P. Name", "Qty. to be delivered", "Status", "Vendor")]
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
                csvexx=sql.connect(currdir+'\\DBFA_CUSTCC.db')
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
                telegram_bot_sendtext("Access alert: Store Report")
                t1dot = ("<b>DBFA Automatic Store Report: </b> <br />This report has been automatically generated. This lists the profit earned, stock analytics and customer records as logged by DBFA.<br /><br />")
                t2dot = ("DBFA synchronously updates its database alongwith algorithmic data interpretation to deliver these reports. <br />This report contains information from the start of using DBFA on this system.<br /><br />")
                t6dot = ("Report generated on: " + dt_string)
                t3dot = ("<br /><br /><b>Most sold listing: </b><br />")
                t4dot = ("<br /><br /><b>Total profit per listing: </b><br /><br />")
                t5dot = ("<br /><br /><b>Most profit making listing: </b><br /><br />")
                t8dot = ("<br /><br /><b>Customer purchases: </b><br /><br />")
                t10dot = ("<br /><br /><br /><br /><br /><br /><b>DBFA Stock Orders Report: </b><br />Product stock yet to be recieved: <br /><br />")
                t11dot = ("<br /><br /><b>DBFA Sales Analysis Plotter: </b><br />DBFA uses advanced data analysis algorithms to generate this plot. This is as per the latest data sets available. <br />")
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
                text11=Paragraph(t11dot)
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
                # -------------------------------------------------------------------------------
                import sqlite3, time
                import matplotlib.pyplot as plt
                salesr = sqlite3.connect(r'dbfasales.db')
                salesx = salesr.cursor()
                datefetch = []

                salesx.execute("SELECT DISTINCT date FROM sales")    
                for i in salesx.fetchall():
                    datefetch.append((i[0]))

                netray = []
                for i in datefetch:
                    salesx.execute(("SELECT sum(prof) FROM sales WHERE date = ?"), (i, ))
                    netray.append(salesx.fetchall()[0][0])

                # Plotting
                plt.plot(datefetch, netray, color='purple', linestyle='dashed', linewidth = 3, 
                        marker='o', markerfacecolor='magenta', markersize=12) 
                # naming the x axis 
                plt.xlabel('Date') 
                # naming the y axis 
                plt.ylabel('Profit') 
                # Graph Title
                plt.title('DBFA Profit Report') 
                time.sleep(1)
                # Finally, display
                plt.savefig('DBFAplot.png', dpi=300, bbox_inches='tight')
                # -------------------------------------------------------------------------------

                delI = Image('DBFAplot.png')
                delI.drawHeight =  4.2*inch
                delI.drawWidth = 5.5*inch
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
                elements.append(text11)
                elements.append(delI)
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
            else:
                    print("This function is restricted on your account.")


        #DBFA Backup&Switch
        elif decfac == "7":
            if str(settingscommondumpfetch(10)) == "Administrator":
                print('''DBFA Backup & Switch v2.0

a. ) Create a backup
b. ) Restore from backup file (Switch/ Restore)

c. ) 'Enter' to return to main menu
                ''')
                basfac = input("What would you like to do?: ")
                if basfac in ("A", "a"):            
                    os.startfile(r'delauth.py')
                    time.sleep(0.3)
                    os._exit(0)
                elif basfac in ("B", "b"):            
                    os.startfile(r'dbfarestoration.py')
                    time.sleep(0.3)
                    os._exit(0)
                else:
                    pass
            else:
                    print("This function is restricted on your account.")
            
        

        #Stock Ordering Option
        elif decfac == "5":
            from colorama import init, Fore, Back, Style #color-settings for the partner/sponsor adverts
            init(convert = True)
            time.sleep(2)
            print(Fore.MAGENTA+'''
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Options:                                         Client >>> Delivery Handler
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
For issuing new delivery orders, use the invoicing option
-----------------------------------------------------------
a: View existing deliveries
b: Show delivery count
c: Confirm a delivery

What would you like to do?            '''+Fore.WHITE+'''█▀▀ █ █ ██   █▀█▀█ █▀ █▀██ █ █ DBFA'''+Fore.MAGENTA+'''
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  '''+Fore.WHITE+'''▀▀█ █_█ ███  █ ▬ █ █_ █ ▬█ █_█ Manager'''+Fore.MAGENTA+'''
'''+Fore.CYAN+'''DBFA Delivery Handler ~'''+Fore.MAGENTA+'''     
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬'''+Fore.WHITE)
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
        elif decfac == "9":
            print("\nAbout DBFA: ")
            print("DBFA Inception 1.0 by deltaonealpha")
            print("Fetching latest licensing information.......")
            logoprintxrt()
            time.sleep(0.5)
            print(" ")
            print("_______ Licensing _______")
            print("           GNU PUBLIC LICENSE - TERMS AND CONDITIONS")
            print("    <deltaBillingFramework>  Copyright (C) 2020 Pranav Balaji and Sushant Gupta")
            print("    This program comes with ABSOLUTELY NO WARRANTY; for details type *show w*.")
            print("    This is free software, and you are welcome to redistribute it")
            print("    under certain conditions; type *show c* for details. ")
            toaster.show_toast("DFBA Framework Runtime Broker", "©2020: DBFA by Pranav Balaji and Sushant Gupta", duration = 1.5)
            print(" ")
            print("Visit: www.github.com/deltaonealpha/deltaBillingFramework for complete licensing terms. ")            
            print(" ")
            print(" ")
            webbrowser.open('https://telegra.ph/DBFA-Licensing-Information-08-16')
            print("--------------------------------------------------")
            print("\n\nLatest Development Changelog: \n")
            webbrowser.open('https://telegra.ph/DBFA-8-RC2-Highlights-08-17')
            webbrowser.open('https://telegra.ph/DBFA-8-Release-Candidate---1-08-16')
            print("--------------------------------------------------")
            time.sleep(2)

        #DBFA Settings - Currently in development
        elif decfac == "6":
            if str(settingscommondumpfetch(10)) == "Administrator":
                def transitionprogress():
                    from colorama import init, Fore, Back, Style
                    os.system("cls")
                    time.sleep(1)
                    print(Fore.WHITE+'|'+Fore.RED+'████ OFF |')
                    time.sleep(0.3)
                    print(Fore.WHITE+'|'+Fore.RED+'███     '+Fore.GREEN+'█|')
                    time.sleep(0.3)
                    print(Fore.WHITE+'|'+Fore.RED+'██     '+Fore.GREEN+'██|')
                    time.sleep(0.3)
                    print(Fore.WHITE+'|'+Fore.RED+'█     '+Fore.GREEN+'███|')
                    time.sleep(0.3)
                    print(Fore.WHITE+'|'+Fore.GREEN+ ' ON  ████|'+Fore.WHITE)
                    time.sleep(1.24)
                    os.system("cls")


                def transitionprogressneg():
                    from colorama import init, Fore, Back, Style
                    os.system("cls")
                    time.sleep(1)
                    print(Fore.WHITE+'|'+Fore.GREEN+ ' ON  ████|')
                    time.sleep(0.3)
                    print(Fore.WHITE+'|'+Fore.RED+'█     '+Fore.GREEN+'███|')
                    time.sleep(0.3)
                    print(Fore.WHITE+'|'+Fore.RED+'██     '+Fore.GREEN+'██|')
                    time.sleep(0.3)
                    print(Fore.WHITE+'|'+Fore.RED+'███     '+Fore.GREEN+'█|')
                    time.sleep(0.3)
                    print(Fore.WHITE+'|'+Fore.RED+'████ OFF |'+Fore.WHITE)
                    time.sleep(1.24)
                    os.system("cls")

                os.system("cls")

                def settingsmenu():
                    from colorama import init, Fore, Back, Style
                    while(1):
                        import time
                        time.sleep(0.2)
                        print("████████████████████████████████████████████████████████████████████████████")
                        print(" --------------------------  DBFA Settings  --------------------------    ")
                        
                        if (settingscommonfetch(1)) == 1:
                            print(" 1:    Display boot image                               :", '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|      ')
                        else:
                            print(" 1:    Display boot image                               :", ('|'+Fore.RED+'████'+Fore.WHITE+' OFF|      '))
                        if (settingscommonfetch(2)) == 1:
                            print(" 2:    Email invoice to registered customers            :", '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|      ')
                        else:
                            print(" 2:    Email invoice to registered customers            :", ('|'+Fore.RED+'████'+Fore.WHITE+' OFF|      '))
                        if (settingscommonfetch(3)) == 1:
                            print(" 3:    Enable DBFA Music Controls (beta):               :", '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|      ')
                        else:
                            print(" 3:    Enable DBFA Music Controls (beta):               :", ('|'+Fore.RED+'████'+Fore.WHITE+' OFF|      '))
                        if (settingscommonfetch(4)) == 1:
                            print(" 4:    Open CSV when exported                           :", '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|      ')
                        else:
                            print(" 4:    Open CSV when exported                           :", ('|'+Fore.RED+'████'+Fore.WHITE+' OFF|      '))
                        if (settingscommonfetch(5)) == 1:
                            print(" 5:    Enable database encryption                       :", '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|      '+Fore.RED)
                            print(" ")
                        else:
                            print(" 5:    Enable database encryption                       :", ('|'+Fore.RED+'████'+Fore.WHITE+' OFF|      ')+Fore.RED)
                            print(" ")
                        if (settingscommonfetch(6)) == 1:
                            print(" 6:    Enable DBFA Secure Two-Factor-Authenication      :", '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|      ')
                            print(" ")
                        else:
                            print(" 6:    Enable DBFA Secure Two-Factor-Authenication      :", ('|'+Fore.RED+'████'+Fore.WHITE+' OFF|      '))
                            print(" ")
                        if (settingscommonfetch(7)) == 1:
                            print(" 7:    Use new DBFA Menu style                          :", '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|      '+Fore.RED)
                            print(" ")
                        else:
                            print(" 7:    Use new DBFA Menu style                          :", ('|'+Fore.RED+'████'+Fore.WHITE+' OFF|      ')+Fore.RED)
                            print(" ")

                        print(Fore.MAGENTA+" 8:    Create DBFA Desktop Shortcut                     :"+Fore.WHITE, '|'+Fore.MAGENTA+"██ Proceed > "+Fore.WHITE+"| ")

                        print(Fore.RED+" 9:    Delete customer records                          :"+Fore.WHITE, '|'+Fore.RED+"██ Proceed > "+Fore.WHITE+"| ")
                        print(Fore.RED+" 10:   Delete store records                             :"+Fore.WHITE, '|'+Fore.RED+"██ Proceed > "+Fore.WHITE+"| ")
                        print(Fore.MAGENTA+" 11:   Check for updates                                :"+' |'+"██ Proceed > "+Fore.WHITE+"|  " )
                        print("                                                                          ")
                        print(Fore.RED+" 12:   Return to Main Menu                             :"+' |'+"██ Proceed > "+Fore.WHITE+"| " )
                        print("                                                                          ")
                        #print("████████████████████████████████████████████████████████████████████████████")
                        settfac = input("What would you like to do? ")
                        if settfac == "1":
                            print('''DBFA displays an image for 2 seconds when it is started. 
                            This image changes with each major iteration of DBFA. 
                            Displaying this image let's us prepare files in the background so that DBFA runs smoothly once its started.
                            Disabling this option may lead to errors. Continue? ''')
                            print(" ")
                            print("Display DBFA boot image? ")
                            print("y:    ",  '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|')
                            settfac1x = input(("n:     "+ '|'+Fore.RED+'████'+Fore.WHITE+' OFF|: '))
                            if settfac1x == "y":
                                settingsmodifier(1, 1)
                                transitionprogress()
                                print("DBFA will now display its boot image when it prepares the backend on boot. ")
                                print("")
                                time.sleep(1)
                                settingsmenu()
                            elif settfac1x == "n":
                                settingsmodifier(1, 0)
                                transitionprogressneg()
                                print("DBFA won't display its boot image when it prepares the backend on boot from now. ")
                                print("")
                                time.sleep(1)
                                settingsmenu()
                            else:
                                print("That's an invalid input... ")
                                print("")
                                time.sleep(1)
                                settingsmenu()
                            
                        elif settfac == "2":
                            print('''DBFA creates an invoice on each billing cycle
                            If the customer account in-use is registered with DBFA, the invoice is E-Mailed to the same.
                            Disabling this option will stop DBFA from E-Mailing customers with their invoice from now.''')
                            print(" ")
                            print("E-Mail registered customers their invoice? ")
                            print("y:    ",  '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|')
                            settfac1x = input(("n:     "+ '|'+Fore.RED+'████'+Fore.WHITE+' OFF|: '))
                            if settfac1x == "y":
                                settingsmodifier(2, 1)
                                transitionprogress()
                                print("DBFA will continue E-Mailing customers with their invoice. ")
                                print("")
                                time.sleep(1)
                                settingsmenu()
                            elif settfac1x == "n":
                                settingsmodifier(2, 0)
                                transitionprogressneg()
                                print("DBFA will stop E-Mailing customers their invoice from now on. ")
                                print("")
                                time.sleep(1)
                                settingsmenu()
                            else:
                                print("That's an invalid input... ")
                                print("")
                                time.sleep(1)
                                settingsmenu()
                            
                        elif settfac == "3":
                            print('''In our mission of making DBFA the ultimate space to control your entire store and its functioning,
                            we keep adding tiny tid-bits to make that process even easier.
                            DBFA Music Controls is one such feature introduced in DBFA 8 RC3x (IB3).
                            When you disable this functionality:
                                    - The currently-playing track will no longer be displayed. 
                                    - DBFA Music Controls, including but not limited to pause/play, prev and next will be restricted. ''')
                            print(" ")
                            print("Enable DBFA Music Controls? ")
                            print("y:    ",  '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|')
                            settfac1x = input(("n:     "+ '|'+Fore.RED+'████'+Fore.WHITE+' OFF|: '))
                            if settfac1x == "y":
                                settingsmodifier(3, 1)
                                transitionprogress()
                                print("DBFA Music Controls Service will be started with the next menu-cycle. ")
                                print("")
                                time.sleep(1)
                                settingsmenu()
                            elif settfac1x == "n":
                                settingsmodifier(3, 0)
                                transitionprogressneg()
                                print("DBFA Music Controls Service will be restricted from the next menu-cycle.")
                                print("")
                                time.sleep(1)
                                settingsmenu()
                            else:
                                print("That's an invalid input... ")
                                print("")
                                time.sleep(1)
                                settingsmenu()
                            
                            
                        elif settfac == "4":
                            print("CSV files once generated are auto-opened in your default worksheet app")
                            print("Example: Microsoft Excel, LibreOffice Calc, Google Docs, et cetera.")
                            print(" ")
                            print("Open file after export? ")
                            print("y:    ",  '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|')
                            settfac1x = input(("n:     "+ '|'+Fore.RED+'████'+Fore.WHITE+' OFF|: '))
                            if settfac1x == "y":
                                settingsmodifier(4, 1)
                                transitionprogress()
                                print("DBFA will now open CSV files when exported on request. ")
                                print("")
                                time.sleep(1)
                                settingsmenu()
                            elif settfac1x == "n":
                                settingsmodifier(4, 0)
                                transitionprogressneg()
                                print("DBFA will not open CSV files when exported from now on. ")
                                print("")
                                time.sleep(1)
                                settingsmenu()
                            else:
                                print("That's an invalid input... ")
                                print("")
                                time.sleep(1)
                                settingsmenu()
                            
                        elif settfac == "5":
                            print('''In our process of phasing-out .txt based storage in favour of sqlite storage, 
                            we at DBFA are trying to make our files even tougher to access than ever before without valid credentials.
                            
                            DBFA is currently experimenting with sqlcipher encryption for it's sqlite databases.
                            Please note that this functionality is a part of DBFA internal test builds for now,
                            and is not ready for public rollout.
                            
                            This process might impact DBFA's data integrity. We recommend you to run *DBFA Backup&Switch* from option *5*
                            before you attempt to encrypt/ decrypt DBFA databases by running this command.''')
                            print(" ")
                            print("Enable DBFA database encryption? ")
                            print("y:    ",  '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|')
                            settfac1x = input(("n:     "+ '|'+Fore.RED+'████'+Fore.WHITE+' OFF|: '))
                            if settfac1x == "y":
                                settingsmodifier(5, 1)
                                transitionprogress()
                                print('''DBFA will attempt to encrypt it's databases when restarted. 
                                This process may fail, as this *internal test build* of DBFA currently has encryption as a beta feature.''')
                                print("")
                                time.sleep(1)
                                settingsmenu()
                            elif settfac1x == "n":
                                settingsmodifier(5, 0)
                                transitionprogressneg()
                                print('''DBFA will attempt to de-crypt it's databases on the next restart. 
                                This process may fail, as this *internal test build* of DBFA currently has encryption as a beta feature.
                                
                                If DBFA databases are already decrypted, no change will take place and data integrity will be untouched.''')
                                print("")
                                time.sleep(1)
                                settingsmenu()
                            else:
                                print("That's an invalid input... ")
                                print("")
                                time.sleep(1)
                                settingsmenu()

                        elif settfac == "6":
                            print("----DBFA 2FA MANAGER----")
                            print("Two-factor authenication is a widely-used method helpful in securing accounts when their passwords get compromised.")
                            print("With DBFA, you can choose between Telegram and Google Authenicator as a medium to recieve these 2FA requests. ")
                            print(" ")
                            print("DBFA randomly generates these OTPs/ requests and sends them via a secure and encrypted connection.")
                            time.sleep(2)
                            print(" ")
                            print(" ")
                            print("Please do note that enabling/ disabling 2FA will reboot DBFA Store Manager!!")
                            print(" ")
                            print(" ")
                            print("Available authenication methods: ")
                            print("1: Telegram Authenication")
                            import os
                            print("2: Google Authenicator (alpha; experimental)")
                            print("3/ skip: Exit to settings menu")
                            authfac = input("What would you like?: ")
                            if authfac == "1":
                                print("Connecting to the Telegram Web API..")
                                print("To turn on/ off DBFA 2FA, you need to authenicate with 2FA first.")
                                time.sleep(0.5)
                                os.startfile('modif2fa.py')
                                time.sleep(1)
                                os._exit(0)

                            if authfac == "2":
                                print("Loading Django framework..")
                                print("This option is currently under development!")
                                print(" ")
                                time.sleep(2)
                            else:
                                print("Please choose a valid option! ")
                                print(" ")

                        elif settfac == "7":                    
                            print("This option let's you switch between the older DBFA menu-style")
                            print("and the newer one as introduced with DBFA 8.12")
                            print("\nFor the best visual experience with DBFA, we recommend you to use the newer design.\n\n")
                            print("DBFA Menu-Style: ")
                            print("1: Use new style (recommended)")
                            print("2: Use old style")
                            msdsfac = input("Please make a choice: ")
                            if msdsfac == "1":  
                                settingsmodifier(7, 1)
                                transitionprogress()
                                print("New menu style applied! ")
                            if msdsfac == "2":
                                print("Old menu style")
                                settingsmodifier(7, 0)
                                transitionprogressneg()
                                print("Old menu style applied..! ")
                            else:
                                print("Please choose a valid option! ")
                                print(" ")



                        elif settfac == "8":
                            import shutil
                            import os
                            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive\Desktop')
                            # Prints: C:\Users\sdkca\Desktop
                            print("Shortcut will be created at: " + desktop)
                            try:
                                original = currdir+'\\Assets\run_DBFA.lnk'
                                shutil.copy(original, desktop)
                                print("Executed. ")
                            except:
                                print("DBFA Permission Error: Can't get perms to execute in directory! ")

                        elif settfac == "9":
                            print('''This option PERMANENTLY CLEARS ALL DBFA CUSTOMER RECORDS.
                            This includes their registration data, purchase records, and loyalty points.
                            
                            This execution can NOT BE REVERSED.
                            DATA INTEGRITY MAY BE LOST during this process.
                            Proceed with caution! ''')
                            print(" ")
                            print("ERASE DBFA customer records PERMANENTLY? ")
                            print("y:    ",  '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|')
                            settfac1x = input(("n:     "+ '|'+Fore.RED+'████'+Fore.WHITE+' OFF|: '))
                            
                            if settfac1x == "y":
                                print("DBFA will now reboot itself to finish applying changes.")
                                time.sleep(0.5)
                                transitionprogress()
                                # window.close()
                                os.startfile(r'securepack.py')
                                time.sleep(1)
                                os._exit(0)
                                    

                                settingsmenu()
                            elif settfac1x == "n":
                                print("Denied. ")
                                settingsmenu()
                            else:
                                print("That's an invalid input... ")
                                print("")
                                time.sleep(1)
                                settingsmenu()

                        elif settfac == "10":
                            print('''This option PERMANENTLY CLEARS ALL DBFA VOUCHERS/ COUPONS
                            All current vouchers/ coupons WILL BE LOST.
                            Vouchers already issued will become redundant unless manually re-added again.
                            Validity and usage limits will be lost for all voucher/ coupon instanced recorded by DBFA.
                            
                            However, DBFA's logged voucher/ coupon usage will continue to exist in memory and will not be erased.
                            
                            This execution can NOT BE REVERSED.
                            DATA INTEGRITY MAY BE LOST during this process.
                            Proceed with caution! ''')
                            print(" ")
                            print("ERASE DBFA voucher/ coupon records PERMANENTLY? ")
                            print("y:    ",  '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|')
                            settfac1x = input(("n:     "+ '|'+Fore.RED+'████'+Fore.WHITE+' OFF|: '))
                            if settfac1x == "y":
                                print("DBFA will now reboot itself to finish applying changes.")
                                time.sleep(0.5)
                                transitionprogress()
                                # window.close()
                                os.startfile(r'securepackxvc.py')
                                time.sleep(1)
                                os._exit(0)
                                
                                
                                settingsmenu()
                            elif settfac1x == "n":
                                print("Denied.")
                                
                                
                                settingsmenu()
                            else:
                                print("That's an invalid input... ")
                                print("")
                                time.sleep(1)
                                settingsmenu()


                        elif settfac == "11":
                            print("Please use DBFA Updater from the main menu (option 11)")
                            settingsmenu()


                        elif settfac == "11":
                            break
                            break
                            break

                        else:
                            print("That's an invalid input... ")
                            print("")
                            time.sleep(1)
                            break
                            break
                            break

                settingsmenu()
            else:
                    print("This function is restricted on your account.")
        #Profit Graph Plotter
        elif decfac == "8":
            if str(settingscommondumpfetch(10)) == "Administrator":
                time.sleep(0.5)
                print("---- DBFA Sales Analyzer Engine v1 ----")    
                time.sleep(0.5)
                print("In DBFA's plotter, you can zoom in/out of the graph, adjust plot dimensions and export the plot to a .png file\n")
                time.sleep(1)
                print("Please wait while we analyze store sales..\n\n")
                time.sleep(2)
                print("A new window will be shortly opened. ")
                print("You're requested to close the same when you want to return to DBFA's main menu.\n")
                time.sleep(1.7)
                os.startfile(r'plotter.pyw')
            else:
                print("This function is restricted on your account.")


        #DBFA Updater
        elif decfac == "10":
            if str(settingscommondumpfetch(10)) == "Administrator":
                import requests, os, time, shutil, oschmod
                os.system('cls')
                print('''---------------------------------
delta Update Deployment Service
---------------------------------
Checking for updates. . . 
---------------------------------''')
                time.sleep(1)

                import os, time
                currdir = str(os.getcwd())
                from pathlib import Path
                path = Path(os.getcwd())
                parentdir = str(Path(path.parent))
                #print(parentdir)
                #print(parentdir+'\\updates.txt')
                userdir = os.path.expanduser('~')
                url = "https://raw.githubusercontent.com/deltaonealpha/DBFA_UpdateHandler/master/updates.txt"
                r = requests.get(url)
                dbfaver = ((str(r.content.decode('utf-8'))))[4:]
                xdbfaver = ((str(r.content.decode('utf-8'))))
                with open(parentdir+'\\updates.txt', 'r+') as upread:
                    upread = (str(upread.read())).strip()

                print("Server: ", dbfaver, "\nLocal: ", upread[4: ])
                time.sleep(1)
                spass1 = []
                spass2 = []
                for i in dbfaver:
                    spass1.append(i)
                for j in upread[4: ]:
                    spass2.append(j)
                if float(upread[4: ]) > float(dbfaver):
                    pass

                else:
                    if xdbfaver == upread:
                        print("This installation of DBFA is already up-to date ~ \n")

                    elif spass1 != spass2:
                        print("Please wait...")
                        time.sleep(2)
                        os.startfile(r'updateDBFA.py')
                        print("Updater opened in a different window")
                        time.sleep(2)
                        os._exit(0)
            else:
                print("This function is restricted on your account.")

        #Exit System
        elif decfac == "11":
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
        
        #DBFA EMPLOYEE MANAGER
        elif decfac in ("emp", "EMP", "EMPLOYEE", "employee", "manager", "MANAGER", "empm", "EMPM"):
            print("Continuing to DBFA Employee Manager - -")
            time.sleep(2)
            print("\n-------------------------------------------------")
            print("This action needs administrator authorization.")
            print("This will provide access to: ")
            print("     - All employee data on your DBFA installation")
            print("\n-------------------------------------------------")
            time.sleep(1)
            import getpass
            passrt = getpass.getpass(prompt='Enter password: ', stream=None)
            if passrt == str(securedatafetch(6)):
                with HiddenPrints():
                    try:
                        sender = telegram_bot_sendtext(dt_string + "\n" + "DBFA Employee Manager accessed! \n\n - DBFA Security")
                        print(sender)
                    except Exception:
                        pass
                
                import os, time, sqlite3, requests, json
                os.system('cls')
                print("-------DBFA Employee Manager-------")
                time.sleep(0.5)
                print("༼ つ ◕_◕ ༽つ ")
                time.sleep(0.5)
                print("         ༼ つ ◕_◕ ༽つ ")
                time.sleep(0.5)
                print("                  ༼ つ ◕_◕ ༽つ ")
                time.sleep(1)
                os.system('cls')

                def empmenu():
                    from colorama import init, Fore, Back, Style #color-settings for the partner/sponsor adverts
                    init(convert = True)
                    print(Fore.CYAN+'''\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\nOptions:              
1  - Hire an employee                    5  - Scheduler & Leave Application
2  - View employee records               
3  - Update employee details             6  - Mark attendance
4  - Fire an employee ༼ ●'◡'● ༽つ        7  - Work records - All
perms - Add new user account             8  - Work records - oID-specf.
11 - Pay salary                          9  - Work records - All (past 30)
12 - <<< Back to DBFA menu               10 - Work records - oID-specf. (past 30)
                                         13 - View Salary Payment Records          

What would you like to do?                    '''+Fore.WHITE+'''█▀▀█ █▀█  █▀▀ █▀█  █▀▀█ Employee'''+Fore.CYAN+'''
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  '''+Fore.WHITE+'''█__█ █▀▀█ █▀  █▬█  ▄▄▄▄ Manager 2.12'''+Fore.CYAN+'''
'''+Fore.MAGENTA+'''The Ultimate Employee Buster ~'''+Fore.CYAN+'''     
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬'''+Fore.WHITE)

                while (1):
                    empmenu()
                    empfac = input("What would you like to do? ")
                    
                    if str(empfac) in ("perms", "PERMS", "Perms", "pERMS"):
                        print("User Account Creation Wizard ")
                        import sqlite3
                        settings = sqlite3.connect(r'dbfasettings.db')
                        settingsx = settings.cursor()
                        settingsx.execute("SELECT MAX(Sno) FROM passkeyhandler")
                        sno = (int(settingsx.fetchall()[0][0]) + 1)
                        uid = input("Enter username for new account: ")
                        kpass = input("Enter password for:" + str(uid) + ": ")
                        confkpass = input("Confirm password: ")
                        if kpass == confkpass:
                            print("Alloting permission set 'sales_group' to ", uid)
                            settingsx.execute(("INSERT INTO passkeyhandler(Sno, Col1, Col2) VALUES (?, ?, ?)"), (sno, uid, kpass))
                            settings.commit()
                            time.sleep(2)
                            print("User account registered. Reboot DBFA Client from login to view changes.")
                        else:
                            print("Wrong re-entry of password. Retry from Employee Manager.")
                    
                    if empfac == "13":
                            import sqlite3
                            empmas = sqlite3.connect(r'dbfaempmaster.db')
                            empmascur = empmas.cursor()
                            empmascur.execute("SELECT * FROM salpay")
                            datastream = empmascur.fetchall()
                            from tabulate import tabulate
                            print("Payment records: ")
                            print(tabulate(datastream, headers=['Employee ID:', "DATE of payment:", 'Amount paid:'], tablefmt='fancy_grid'))

                    if empfac == "1":
                        print("DBFA will now be opening a seperate window due to GUI-restrictions.")
                        time.sleep(2)
                        with HiddenPrints():
                            try:
                                sender = telegram_bot_sendtext(dt_string + "\n" + "Accessed: Hire Employee - deltaDBFA")
                                print(sender)
                            except Exception:
                                pass
                        os.startfile(r'dbfaempman.py')
                        

                    if empfac == "2":
                        print("\n2. View employee records\n-----------------------------------------------")
                        empmas = sqlite3.connect(r'dbfaempmaster.db')
                        empmascur = empmas.cursor()
                        print("Employee records as maintained by DBFA: ")
                        with HiddenPrints():
                            try:
                                sender = telegram_bot_sendtext(dt_string + "\n" + "Accessed: Employee Records - deltaDBFA")
                                print(sender)
                            except Exception:
                                pass
                        empmascur.execute("SELECT * FROM emp")
                        emprows = empmascur.fetchall()
                        time.sleep(1)
                        for emprow in emprows:
                            print(emprow, "\n")
                        print("\n\n-----------------------------------------------")
                        time.sleep(3)
                    
                    if empfac == "3":
                        print("3. Change employee details")
                        empmas = sqlite3.connect(r'dbfaempmaster.db')
                        empmascur = empmas.cursor()
                        empmascur.execute("SELECT * FROM emp")
                        emprows = empmascur.fetchall()
                        time.sleep(1)
                        for emprow in emprows:
                            print(emprow, "\n")
                        print("\n")
                        emppay = str(input("Enter the Oid (Employee ID) to change details for: "))
                        empmascur.execute("SELECT Name FROM emp WHERE Oid LIKE ?", ("%"+emppay+"%", ))
                        firename = str(empmascur.fetchall()[0][0])
                        confofac = input("CONFIRM: Change details for "+firename+"? (y/n): ")
                        if confofac == "y":
                            from colorama import init, Fore, Back, Style #color-settings for the partner/sponsor adverts
                            init(convert = True)
                            print(Fore.MAGENTA+'''
    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    Options:                            Employee Manager >>> Employee Details Modifier
    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
        1. Change Name
        2. Change Email
        3. Change Mobile Contact

        4. Change Residential Address
        5. Change UPI Payments ID

        6. Change Department
        7. Change Designation (POST)
        8. Change Salary 

    What would you like to do?                '''+Fore.WHITE+'''█▀▀ █ █ ██   █▀█▀█ █▀ █▀██ █ █ DBFA'''+Fore.MAGENTA+'''
    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  '''+Fore.WHITE+'''▀▀█ █_█ ███  █ ▬ █ █_ █ ▬█ █_█ Manager'''+Fore.MAGENTA+'''
    '''+Fore.CYAN+'''Employee Details Modifier ~'''+Fore.MAGENTA+'''     
    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬'''+Fore.WHITE)                  
                            subfac = input("What would you like to do? ")
                            if subfac == "1":
                                print("1. Change Name")
                                empmas = sqlite3.connect(r'dbfaempmaster.db')
                                empmascur = empmas.cursor()
                                newmodif = input("Enter the changed name: ")
                                time.sleep(1)
                                empmascur.execute("UPDATE emp SET Name = ? WHERE Oid = ?", (newmodif, emppay))
                                empmas.commit()
                                print("Name changed for OID", emppay, " from ", firename, "to ", newmodif)
                                time.sleep(1)
                                with HiddenPrints():
                                    try:
                                        sender = telegram_bot_sendtext(dt_string + "\n" + "Accessed: Employee Details Changed - deltaDBFA")
                                        print(sender)
                                    except Exception:
                                        pass
                                print("--------")
                                time.sleep(1)

                            if subfac == "2":
                                print("2. Change Email")
                                empmas = sqlite3.connect(r'dbfaempmaster.db')
                                empmascur = empmas.cursor()
                                empmascur.execute("SELECT Email FROM emp WHERE Oid LIKE ?", ("%"+emppay+"%", ))
                                firename = str(empmascur.fetchall()[0][0])
                                newmodif = input("Enter the changed e-mail: ")
                                time.sleep(1)
                                empmascur.execute("UPDATE emp SET Email = ? WHERE Oid = ?", (newmodif, emppay))
                                empmas.commit()
                                with HiddenPrints():
                                    try:
                                        sender = telegram_bot_sendtext(dt_string + "\n" + "Accessed: Employee Details Changed - deltaDBFA")
                                        print(sender)
                                    except Exception:
                                        pass
                                print("Email changed for OID", emppay, " from ", firename, "to ", newmodif)
                                time.sleep(1)
                                print("--------")
                                time.sleep(1)

                            if subfac == "3":
                                print("3. Change Mobile Contact")
                                empmas = sqlite3.connect(r'dbfaempmaster.db')
                                empmascur = empmas.cursor()
                                empmascur.execute("SELECT Mobile FROM emp WHERE Oid LIKE ?", ("%"+emppay+"%", ))
                                firename = str(empmascur.fetchall()[0][0])
                                newmodif = input("Enter the changed mobile contact: ")
                                time.sleep(1)
                                empmascur.execute("UPDATE emp SET Mobile = ? WHERE Oid = ?", (newmodif, emppay))
                                empmas.commit()
                                with HiddenPrints():
                                    try:
                                        sender = telegram_bot_sendtext(dt_string + "\n" + "Accessed: Employee Details Changed - deltaDBFA")
                                        print(sender)
                                    except Exception:
                                        pass
                                print("Mobile contact changed for OID", emppay, " from ", firename, "to ", newmodif)
                                time.sleep(1)
                                print("--------")
                                time.sleep(1)

                            if subfac == "4":
                                print("4. Change Residential Address")
                                empmas = sqlite3.connect(r'dbfaempmaster.db')
                                empmascur = empmas.cursor()
                                empmascur.execute("SELECT Address FROM emp WHERE Oid LIKE ?", ("%"+emppay+"%", ))
                                firename = str(empmascur.fetchall()[0][0])
                                newmodif = input("Enter the changed address (in one-line): ")
                                time.sleep(1)
                                empmascur.execute("UPDATE emp SET Address = ? WHERE Oid = ?", (newmodif, emppay))
                                empmas.commit()
                                with HiddenPrints():
                                    try:
                                        sender = telegram_bot_sendtext(dt_string + "\n" + "Accessed: Employee Details Changed - deltaDBFA")
                                        print(sender)
                                    except Exception:
                                        pass
                                print("Address changed for OID", emppay, " from ", firename, "to ", newmodif)
                                time.sleep(1)
                                print("--------")
                                time.sleep(1)

                            if subfac == "5":
                                print("5. Change UPI Payments ID")
                                empmas = sqlite3.connect(r'dbfaempmaster.db')
                                empmascur = empmas.cursor()
                                empmascur.execute("SELECT UPI FROM emp WHERE Oid LIKE ?", ("%"+emppay+"%", ))
                                firename = str(empmascur.fetchall()[0][0])
                                newmodif = input("Enter the changed UPI ID: ")
                                time.sleep(1)
                                empmascur.execute("UPDATE emp SET UPI = ? WHERE Oid = ?", (newmodif, emppay))
                                empmas.commit()
                                with HiddenPrints():
                                    try:
                                        sender = telegram_bot_sendtext(dt_string + "\n" + "Accessed: Employee Details Changed - deltaDBFA")
                                        print(sender)
                                    except Exception:
                                        pass
                                print("UPI ID changed for OID", emppay, " from ", firename, "to ", newmodif)
                                time.sleep(1)
                                print("--------")
                                time.sleep(1)

                            if subfac == "6":
                                print("6. Change Department")
                                time.sleep(1)
                                empmas = sqlite3.connect(r'dbfaempmaster.db')
                                empmascur = empmas.cursor()
                                empmascur.execute("SELECT Dept FROM emp WHERE Oid LIKE ?", ("%"+emppay+"%", ))
                                firename = str(empmascur.fetchall()[0][0])
                                print("-----------------------------------\nCurrent Dept: ", firename)
                                print('''Options: 
                                            IT,
                                            Administration, 
                                            Sales, 
                                            Care-taking, 
                                            Logistics ''')
                                print("-----------------------------------\n\n")
                                time.sleep(2)
                                newmodif = input("Enter the changed department: ")
                                time.sleep(1)
                                empmascur.execute("UPDATE emp SET Dept = ? WHERE Oid = ?", (newmodif, emppay))
                                empmas.commit()
                                with HiddenPrints():
                                    try:
                                        sender = telegram_bot_sendtext(dt_string + "\n" + "Accessed: Employee Details Changed - deltaDBFA")
                                        print(sender)
                                    except Exception:
                                        pass
                                print("Department changed for OID", emppay, " from ", firename, "to ", newmodif)
                                time.sleep(1)
                                print("--------")
                                time.sleep(1)

                            if subfac == "7":
                                print("7. Change Designation (POST)")
                                empmas = sqlite3.connect(r'dbfaempmaster.db')
                                empmascur = empmas.cursor()
                                empmascur.execute("SELECT Post FROM emp WHERE Oid LIKE ?", ("%"+emppay+"%", ))
                                firename = str(empmascur.fetchall()[0][0])
                                newmodif = input("Enter the new designation: ")
                                time.sleep(1)
                                empmascur.execute("UPDATE emp SET Post = ? WHERE Oid = ?", (newmodif, emppay))
                                empmas.commit()
                                with HiddenPrints():
                                    try:
                                        sender = telegram_bot_sendtext(dt_string + "\n" + "Accessed: Employee Details Changed - deltaDBFA")
                                        print(sender)
                                    except Exception:
                                        pass
                                print("Designation (Post) changed for OID", emppay, " from ", firename, "to ", newmodif)
                                time.sleep(1)
                                print("--------")
                                time.sleep(1)

                            if subfac == "8":
                                print("8. Change Salary")
                                empmas = sqlite3.connect(r'dbfaempmaster.db')
                                empmascur = empmas.cursor()
                                empmascur.execute("SELECT Salary FROM emp WHERE Oid LIKE ?", ("%"+emppay+"%", ))
                                firename = str(empmascur.fetchall()[0][0])
                                newmodif = input("Enter the new salary (net; not incremental): ")
                                time.sleep(1)
                                empmascur.execute("UPDATE emp SET Salary = ? WHERE Oid = ?", (newmodif, emppay))
                                empmas.commit()
                                with HiddenPrints():
                                    try:
                                        sender = telegram_bot_sendtext(dt_string + "\n" + "Accessed: Employee Details Changed - deltaDBFA")
                                        print(sender)
                                    except Exception:
                                        pass
                                print("Salary changed for OID", emppay, " from ", firename, "to ", newmodif)
                                time.sleep(1)
                                print("--------")
                                time.sleep(1)
                            else:
                                print("Invalid option! \n\n")
                                time.sleep(1)
                        else:
                            print("Invalid option! \n\n")
                            time.sleep(1)


                    if empfac == "4":
                        empmas = sqlite3.connect(r'dbfaempmaster.db')
                        empmascur = empmas.cursor()
                        print("4. Fire an employee ༼ ●'◡'● ༽つ \n")
                        empmascur.execute("SELECT * FROM emp")
                        emprows = empmascur.fetchall()
                        time.sleep(1)
                        for emprow in emprows:
                            print(emprow, "\n")
                        print("\n")
                        emppay = str(input("Enter the Oid (Employee ID) for the employee to fire: "))
                        empmascur.execute("SELECT Name FROM emp WHERE Oid LIKE ?", ("%"+emppay+"%", ))
                        firename = str(empmascur.fetchall()[0][0])
                        confofac = input("CONFIRM: Fire "+firename+"? (y/n): ")
                        if confofac == "y":
                            reasonfire = input("Enter the reason for firing: ")
                            print("FIRING EMPLOYEE! ")
                            empmascur.execute("DELETE FROM emp WHERE Oid = ?", ("%"+emppay+"%", ))
                            empmas.commit()
                            telethon = ""
                            print("\n\n")
                            print("---------------------------------------------")
                            telethon += ("----------------------------\n")
                            print("DBFA Employee Firing Record        deltaDBFA")
                            telethon += ("DBFA Employee Firing Record\n")
                            print("- - - - - - - - - - - - - - - - - - - - - - -")
                            telethon += ("- - - - - - - - - - - - - - - - -\n")
                            print("Name  :", '%s'%firename)
                            telethon += ("Name  : "+ '%s'%firename)
                            print("Reason:", '%s'%reasonfire)
                            telethon += ("\nReason: "+ '%s'%reasonfire)
                            print("- - - - - - - - - - - - - - - - - - - - - - -")
                            telethon += ("\n- - - - - - - - - - - - - - - - -\n")
                            telethon += ("~ deltaDBFA\n")
                            telethon += ("-----------------------------\n\n")
                            telegram_bot_sendtext(telethon)
                            print("~ Event logged in Infinity Logger & Telegram.")
                            print("---------------------------------------------\n\n")
                            
                            time.sleep(2)
                        else:
                            print("Cancelled op..")
                    
                    if empfac == "5":
                        print("\nDBFA Scheduler handles duty scheduling and shifts for 24x7 services.\nDBFA can automatically schedule shifts and handle leave applications.")
                        from colorama import init, Fore, Back, Style #color-settings for the partner/sponsor adverts
                        init(convert = True)
                        print(Fore.MAGENTA+'''
    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    Options:                                       Employee Manager >>> deltaScheduler
    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
        a. View tomorrow's schedule 
        b. Apply for a leave (effective tomorrow only)
        c. Return to main menu ~ 

    What would you like to do?                '''+Fore.WHITE+'''█▀▀ █ █ ██   █▀█▀█ █▀ █▀██ █ █ DBFA'''+Fore.MAGENTA+'''
    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  '''+Fore.WHITE+'''▀▀█ █_█ ███  █ ▬ █ █_ █ ▬█ █_█ Manager'''+Fore.MAGENTA+'''
    '''+Fore.CYAN+'''Shift Scheduler ~'''+Fore.MAGENTA+'''     
    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬'''+Fore.WHITE)
                        submen = input("What would you like to do?: ")
                        if submen in ("A", "a"):
                            with open('lastsched.txt', 'r+', encoding="utf-8") as file:
                                print("Latest schedule as sent to employees:\n", file.read())
                                file.close()
                            contfac = input("Press 'enter' to continue: (workspace will be cleared!)")
                        if submen in ("B", "b"):
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
                                    print("Leave application recieved ~ Enjoy your day tomorrow :)")
                                    empmas = sqlite3.connect(r'dbfaempmaster.db')
                                    empmascur = empmas.cursor()
                                    empmascur.execute("INSERT INTO leave(Oid, Date) VALUES (?, ?)", ('%s'%OiD, '%s'%dt_string, ))
                                    empmas.commit()
                                else:
                                    print("Oof. Now get to work ;) ")
                            else:
                                print("Invalid OiD identifier. Please try again ~")

                        if submen in ("C", "c"):
                            pass


                    if empfac == "6":
                        import sqlite3, time, os, requests
                        from datetime import datetime  #for reporting the billing time and date
                        empmas = sqlite3.connect(r'dbfaempmaster.db')
                        empmascur = empmas.cursor()
                        empmascur.execute("SELECT DISTINCT * FROM emp")
                        dump = empmascur.fetchall()
                        Oiddump = []
                        for row in dump:
                            Oiddump.append(row[0])
                        print("OiDs registered: ", Oiddump)
                        try:
                            Oid = int(input("DBFA MARK ATTENDANCE- Enter your OiD: "))
                            trypass = 1
                        except:
                            print("OiDs are integer-only. Please retry using valid credentials! \n")
                            trypass = 0
                        
                        if trypass == 1:
                            if Oid in Oiddump:
                                print("OiD found ")
                                time.sleep(0.5)
                                now = datetime.now()
                                dt_string = now.strftime("%Y/%m/%d")  #datetime object containing current date and time
                                tm_string = now.strftime("%H:%M:%S")  #datetime object containing current date and time
                                empmascur.execute("SELECT count(*) FROM attendance WHERE Date = ? AND OiD = ?", (dt_string, Oid,))
                                data = empmascur.fetchone()[0]
                                if data==0:
                                    #print('No record on %s'%dt_string+' for Employee %s'%Oid)
                                    #print("insert into attendance(Date, OiD, Time, YN, IO) values(?, ?, ?, ?, ?)", (dt_string, Oid, tm_string, 'Y', 'I'))
                                    empmascur.execute("insert into attendance(Date, OiD, Time, YN, IO) values(?, ?, ?, ?, ?)", (dt_string, Oid, tm_string, 'Y', 'I'))
                                    #empmascur.execute("UPDATE attendance SET Oid = 'Y' WHERE DATE = ?", (dt_string))
                                    empmas.commit()
                                    print("\n----------------DBFA-----------------")
                                    print("C1 ENTRY: Marked Attendance! OiD: ", Oid)
                                    with HiddenPrints():
                                        try:
                                            sender = telegram_bot_sendtext(dt_string + "\n" + "C1 ENTRY: Marked attendance - OiD"+'%s'%Oid)
                                            print(sender)
                                        except Exception:
                                            pass
                                    print("-------------------------------------\n")
                                elif data==1:
                                    #print('Component %s found in %s row(s)'%(dt_string, data))
                                    empmascur.execute("insert into attendance(Date, OiD, Time, YN, IO) values(?, ?, ?, ?, ?)", (dt_string, Oid, tm_string, 'Y', 'O'))
                                    empmas.commit()
                                    print("\n----------------DBFA-----------------")
                                    print("C2 DAY END: Marked Attendance! OiD: ", Oid)
                                    with HiddenPrints():
                                        try:
                                            sender = telegram_bot_sendtext(dt_string + "\n" + "C2 DAY END: Marked attendance - OiD"+'%s'%Oid)
                                            print(sender)
                                        except Exception:
                                            pass
                                    print("-------------------------------------\n")
                                elif data > 1:
                                    print("You can only mark in/out attendance once a day! \n")
                            else:
                                print("OiD not found! \n")

                    if empfac == "7":
                        print("7. Attendance records - All")
                        with HiddenPrints():
                            try:
                                sender = telegram_bot_sendtext(dt_string + "\n" + "Accessed: Employee Attendance Records - deltaDBFA")
                                print(sender)
                            except Exception:
                                pass
                        import sqlite3, time, os, requests, datetime
                        from datetime import datetime, date

                        empmas = sqlite3.connect(r'dbfaempmaster.db')
                        empmascur = empmas.cursor()

                        empmascur.execute("SELECT DISTINCT * FROM emp")
                        dump = empmascur.fetchall()
                        Oiddump = []
                        for row in dump:
                            Oiddump.append(row[0])

                        print("OiDs registered: ", Oiddump)


                        now = datetime.now()
                        dt_string = now.strftime("%Y/%m/%d")  #datetime object containing current date and time    

                        month = datetime.now().month - 1
                        if month < 1:
                            month = 12 + month  # At this point month is 0 or a negative number so we add
                        if len(str(month)) == 1:
                            month = "0"+str(month)
                        dt1mb = ('%s'%now.strftime("%Y")+'%s'%"/"+'%s'%month+'%s'%"/"+now.strftime("%d"))


                        time.sleep(0.5)
                        print("\nLoading ALL attendance data recorded since the start of using DBFA\n")
                        empmascur.execute("SELECT * FROM attendance ORDER BY Date ASC")
                        returned = empmascur.fetchall()
                        for row in returned:
                            print(row)


                    if empfac == "8":
                        print("8. Attendance records - OiD-specific")
                        with HiddenPrints():
                            try:
                                sender = telegram_bot_sendtext(dt_string + "\n" + "Accessed: Employee Attendance Records - deltaDBFA")
                                print(sender)
                            except Exception:
                                pass
                        import sqlite3, time, os, requests
                        from datetime import datetime  #for reporting the billing time and date

                        empmas = sqlite3.connect(r'dbfaempmaster.db')
                        empmascur = empmas.cursor()

                        empmascur.execute("SELECT DISTINCT * FROM emp")
                        dump = empmascur.fetchall()
                        Oiddump = []
                        for row in dump:
                            Oiddump.append(row[0])

                        print("OiDs registered: ", Oiddump)

                        try:
                            Oid = int(input("DBFA ATTENDANCE RECORDS- Enter the OiD: "))
                            trypass = 1
                        except:
                            print("OiDs are integer-only. Please retry using valid credentials! \n")
                            trypass = 0
                            
                        if trypass == 1:
                            if Oid in Oiddump:
                                print("OiD found ")
                                time.sleep(0.5)
                                empmascur.execute("SELECT * FROM attendance WHERE Oid = ? ORDER BY Date ASC, Time, IO", ('%s'%Oid))
                                returned = empmascur.fetchall()
                                for row in returned:
                                    print(row)


                    if empfac == "9":
                        print("9. Attendance records - All (THIS MONTH)")
                        with HiddenPrints():
                            try:
                                sender = telegram_bot_sendtext(dt_string + "\n" + "Accessed: Employee Attendance Records - deltaDBFA")
                                print(sender)
                            except Exception:
                                pass
                        print("Coming soon! ")
                        import sqlite3, time, os, requests, datetime
                        from datetime import datetime, date

                        empmas = sqlite3.connect(r'dbfaempmaster.db')
                        empmascur = empmas.cursor()

                        empmascur.execute("SELECT DISTINCT * FROM emp")
                        dump = empmascur.fetchall()
                        Oiddump = []
                        for row in dump:
                            Oiddump.append(row[0])

                        print("OiDs registered: ", Oiddump)


                        now = datetime.now()
                        dt_string = now.strftime("%Y/%m/%d")  #datetime object containing current date and time    

                        month = datetime.now().month - 1
                        if month < 1:
                            month = 12 + month  # At this point month is 0 or a negative number so we add
                        if len(str(month)) == 1:
                            month = "0"+str(month)
                        dt1mb = ('%s'%now.strftime("%Y")+'%s'%"/"+'%s'%month+'%s'%"/"+now.strftime("%d"))


                        time.sleep(0.5)
                        print("\nLoading data for days between "+'%s'%dt1mb+" and "+'%s'%dt_string+"\n")
                        empmascur.execute("SELECT * FROM attendance WHERE Date BETWEEN ? AND ? ORDER BY Date ASC", (dt1mb, dt_string))
                        returned = empmascur.fetchall()
                        for row in returned:
                            print(row)


                    if empfac == "10":
                        print("10. Attendance records - OiD-specific (THIS MONTH)")
                        with HiddenPrints():
                            try:
                                sender = telegram_bot_sendtext(dt_string + "\n" + "Accessed: Employee Attendance Records - deltaDBFA")
                                print(sender)
                            except Exception:
                                pass
                        import sqlite3, time, os, requests, datetime
                        from datetime import datetime, date

                        empmas = sqlite3.connect(r'dbfaempmaster.db')
                        empmascur = empmas.cursor()

                        empmascur.execute("SELECT DISTINCT * FROM emp")
                        dump = empmascur.fetchall()
                        Oiddump = []
                        for row in dump:
                            Oiddump.append(row[0])

                        print("OiDs registered: ", Oiddump)

                        try:
                            Oid = int(input("DBFA ATTENDANCE RECORDS- Enter the OiD: "))
                            trypass = 1
                        except:
                            print("OiDs are integer-only. Please retry using valid credentials! \n")
                            trypass = 0

                        now = datetime.now()
                        dt_string = now.strftime("%Y/%m/%d")  #datetime object containing current date and time    

                        month = datetime.now().month - 1
                        if month < 1:
                            month = 12 + month  # At this point month is 0 or a negative number so we add
                        if len(str(month)) == 1:
                            month = "0"+str(month)
                        dt1mb = ('%s'%now.strftime("%Y")+'%s'%"/"+'%s'%month+'%s'%"/"+now.strftime("%d"))

                        if trypass == 1:
                            if Oid in Oiddump:
                                print("OiD found ")
                                time.sleep(0.5)
                                print("\nLoading data for days between "+'%s'%dt1mb+" and "+'%s'%dt_string+"\n")
                                empmascur.execute("SELECT * FROM attendance WHERE OiD = ? AND Date BETWEEN ? AND ? ORDER BY Date ASC", ('%s'%Oid, dt1mb, dt_string))
                                returned = empmascur.fetchall()
                                for row in returned:
                                    print(row)

                        
                    if empfac == "11":                       
                        from datetime import datetime, date
                        now = datetime.now()
                        dt_string = now.strftime("%d")  #datetime object containing current date and time 
                        #print(dt_string)
                        if dt_string in ("01", "02", "03", "04", "05"):
                            def errorout():
                                print("Invalid parameters, please retry")
                                exit

                            import sqlite3, os, datetime
                            from datetime import datetime, date

                            def getpost(Oid):
                                empmas = sqlite3.connect(r'dbfaempmaster.db')
                                empmascur = empmas.cursor()
                                empmascur.execute("SELECT Post FROM emp WHERE OiD = ?", ('%s'%Oid,))
                                daysrt = empmascur.fetchall()
                                return daysrt[0][0]


                            def getdays(Oid):
                                empmas = sqlite3.connect(r'dbfaempmaster.db')
                                empmascur = empmas.cursor()
                                now = datetime.now()
                                dt_string = now.strftime("%Y/%m/%d")  #datetime object containing current date and time    
                                month = datetime.now().month - 1
                                if month < 1:
                                    month = 12 + month  # At this point month is 0 or a negative number so we add
                                if len(str(month)) == 1:
                                    month = "0"+str(month)
                                dt1mb = ('%s'%now.strftime("%Y")+'%s'%"/"+'%s'%month+'%s'%"/"+now.strftime("%d"))
                                empmascur.execute("SELECT * FROM attendance WHERE OiD = ? AND Date BETWEEN ? AND ? ORDER BY Date ASC", ('%s'%Oid, dt1mb, dt_string))
                                returned = empmascur.fetchall()
                                return len(returned)


                            def gethoursavg(Oid):
                                empmas = sqlite3.connect(r'dbfaempmaster.db')
                                empmascur = empmas.cursor()
                                empmascur.execute("SELECT * FROM attendance WHERE OiD = ? ORDER BY Date ASC, Time", ('%s'%Oid,))
                                count = 0
                                rows = empmascur.fetchall()
                                datelist = []
                                for i in rows:
                                    datelist.append(i[0])
                                a = [i for i in rows if datelist.count(i[0])>1]
                                netr = (len(datelist) - len(a)) * 8
                                ini_list = [i[2] for i in a]
                                from datetime import timedelta   
                                diff_list = [] 
                                for x, y in zip(ini_list[0::], ini_list[1::]): 
                                    t1 = str((timedelta(hours=int(y.split(':')[0]), minutes=int(y.split(':')[1])) - timedelta(hours=int(x.split(':')[0]), minutes=int(x.split(':')[1])))).split(':')[0]
                                    diff_list.append(t1)
                                del diff_list[1::2]
                                for i in range(0, len(diff_list)): 
                                    diff_list[i] = int(diff_list[i]) 
                                if int(netr) > 0:
                                    diff_list.append(netr) 
                                return (sum(diff_list)/len(diff_list))


                            def getovertime(Oid):
                                from datetime import datetime, date
                                now = datetime.now()
                                dt_string = now.strftime("%Y/%m/%d")  #datetime object containing current date and time    
                                month = datetime.now().month - 1
                                if month < 1:
                                    month = 12 + month  # At this point month is 0 or a negative number so we add
                                if len(str(month)) == 1:
                                    month = "0"+str(month)
                                dt1mb = ('%s'%now.strftime("%Y")+'%s'%"/"+'%s'%month+'%s'%"/"+now.strftime("%d"))
                                empmas = sqlite3.connect(r'dbfaempmaster.db')
                                empmascur = empmas.cursor()
                                empmascur.execute("SELECT * FROM attendance WHERE OiD = ? AND Date BETWEEN ? AND ? ORDER BY Date ASC", ('%s'%Oid, dt1mb, dt_string, ))
                                count = 0
                                rows = empmascur.fetchall()
                                datelist = []
                                for i in rows:
                                    datelist.append(i[0])
                                a = [i for i in rows if datelist.count(i[0])>1]
                                netr = (len(datelist) - len(a)) * 8
                                ini_list = [i[2] for i in a]
                                from datetime import timedelta   
                                diff_list = [] 
                                for x, y in zip(ini_list[0::], ini_list[1::]): 
                                    t1 = str((timedelta(hours=int(y.split(':')[0]), minutes=int(y.split(':')[1])) - timedelta(hours=int(x.split(':')[0]), minutes=int(x.split(':')[1])))).split(':')[0]
                                    diff_list.append(t1)
                                del diff_list[1::2]
                                for i in range(0, len(diff_list)): 
                                    diff_list[i] = int(diff_list[i]) 
                                finlist = []
                                for i in range(0, len(diff_list)): 
                                    if diff_list[i] > 8:
                                        finlist.append(diff_list[i])
                                return sum(finlist)



                            def calcengine(Oid, bonus):
                                postnet = ("ceo", "cto", "admin", "it", "sales", "maintanence", "logistics")
                                salnet = (97000, 84000, 42000, 35000, 32000, 22000, 21000)
                                days = 30
                                leave_days = 30-int(days)
                                post = getpost(Oid)
                                avg_hours_week = gethoursavg(Oid)
                                hours_overtime = getovertime(Oid)
                                paynet = int(salnet[postnet.index(post.lower())])
                                if int(avg_hours_week) < 8:
                                    paynet = paynet - ((8-int(avg_hours_week))*1000)
                                if int(hours_overtime) > 0:
                                    paynet += (int(hours_overtime)*1500)
                                if int(leave_days) > 3:
                                    paynet = paynet - ((int(leave_days)-3)*750)
                                if int(bonus) > 0:
                                    paynet += bonus
                                print("----------------------------")
                                print("Average hours worked     : ", avg_hours_week)
                                print("Overtime hours worked    : ", hours_overtime)
                                print("Leave(s) taken           : ", leave_days)
                                print("Bonus added              : ", bonus)
                                print("----------------------------\n")
                                return paynet


                            import time
                            import pyqrcode, png, os
                            from pyqrcode import QRCode 

                            empmas = sqlite3.connect(r'dbfaempmaster.db')
                            empmascur = empmas.cursor()

                            empmascur.execute("SELECT Oid, Name, Mobile, UPI, Dept, Post, Salary FROM emp")
                            emprows = empmascur.fetchall()
                            from tabulate import tabulate
                            print(tabulate(emprows, headers=['O-ID', 'Name', 'Mobile', 'UPI', 'Dept', "Post", 'Salary'], tablefmt='fancy_grid'))
                            #for emprow in emprows:
                                #print(emprow)

                            time.sleep(2)

                            emppay = str(input("Enter the Oid (Employee ID) to pay salary for: "))
                            empmascur.execute("SELECT * FROM emp WHERE Oid LIKE ?", ("%"+emppay+"%", ))
                            print(tabulate(empmascur.fetchall(), headers=['O-ID', 'Name', 'DOB', 'Email', 'Mobile', 'Address', 'UPI', 'Dept', "Post", 'Salary'], tablefmt='fancy_grid'))
                            print('\n')
                            print("Please pay the employee: ₹", calcengine(1, 0))
                            time.sleep(2)
                            emppayconfox = input("\n\nPay salary? (y/n): ")
                            if emppayconfox == "y":
                                #emarpay = str("%"+'%s'%emppay+"%")
                                empmascur.execute("SELECT Name, UPI FROM emp WHERE Oid LIKE ?", (emppay,) )
                                tempemppay = empmascur.fetchall()
                                print("Paying ", list(tempemppay[0])[0], "at ", list(tempemppay[0])[1])
                                name = list(tempemppay[0])[0]
                                upid = list(tempemppay[0])[1]
                            else:
                                empmenu()
                                exit
                                print("Aaaa")

                            #upid = '9810141714@upi'
                            #name = 'KPBalaji'

                            s = "upi://pay?pa="+'%s'%upid+"&pn="+'%s'%name+"&cu=INR"

                            # Generate QR code 
                            url = pyqrcode.create(s) 

                            url.png('payqr.png', scale = 6) 
                            from PIL import Image, ImageDraw, ImageFont
                            image = Image.open('payqr.png')
                            try:
                                sender = telegram_bot_sendtext(dt_string + "\n" + "Started Process: Issue Salary - deltaDBFA")
                                print(sender)
                            except Exception:
                                pass
                            draw = ImageDraw.Draw(image)
                            font = ImageFont.truetype(fontsdir, size=200)
                            (x, y) = (5, 250)
                            xname = 'Scan to pay with UPI              deltaDBFA'
                            draw.text((x, y), xname) #, fill=color)
                            (x, y) = (5, 5)

                            name = "Paying "+'%s'%name+" "*(28-len(str(name)))+"deltaPay"
                            draw.text((x, y), name) #, fill=color)
                            image.save('payqr.png', optimize=True, quality=120)
                            
                            print("Please pay the employee: ₹", calcengine(1, 0))
                            print("-------------------------------------")
                            time.sleep(1)
                            print("Scan the code in a UPI app to pay")
                            time.sleep(1)

                            os.system(currdir+'\\payqr.png')

                            time.sleep(5)
                            paycheck = input("Mark salary as 'PAID'? (y/n): ")
                            if paycheck == "y":
                                print("Salary paid!")
                                from datetime import datetime, date
                                now = datetime.now()
                                dt_string = now.strftime("%d")  #datetime object containing current date and time 
                                empmas = sqlite3.connect(r'dbfaempmaster.db')
                                empmascur = empmas.cursor()
                                empmascur.execute("insert into salpay(Oid, Date, Amount) values(?, ?, ?)", (emppay, dt_string, calcengine(1, 0)))
                                empmas.commit()
                            else:
                                print("Not paid. ")


                        else:
                            print("Salary payments can only be made between 01st - 05th of each month. ~")



                    if empfac == "12":
                        print("Returning to DBFA Main.. ")
                        time.sleep(1)
                        break
                    
                    #else:
                        #import os
                        #os.system('cls')

            else:
                print("Invalid password! ")

            
        #CIT
        elif decfac == "113":
            if str(settingscommondumpfetch(10)) == "Administrator":
                print("INTERNAL TESTING MODE")
                ffxfac = str(input("Enter CIT Testing Mode? (y/n):: "))
                if ffxfac == "y":
                    ffrxfac = str(input("Entering CIT may lead to data loss. Confirm entering CIT? (y/n):: "))
                    if ffrxfac == "y":
                        from colorama import init, Fore, Back, Style #color-settings for the partner/sponsor adverts
                        init(convert = True)
                        print(Fore.RED+'''
    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    Internal Testing Mode                               DBFA Debugger >>> Permissive Options
    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    DBFA Client will restart to execute Permissive Options!'''+Fore.MAGENTA+'''
        '1' - to CLEAR ALL CUSTOMER RECORDS
        '2' - to CLEAR ALL VOUCHERS/ COUPONS
        '3' - to exit CIT

    What would you like to do?                '''+Fore.RED+'''█▀▀█ █▀ ██  █ █ █▀▀  █▀▀  █▀ ██   Internal'''+Fore.MAGENTA+'''
    '''+Fore.RED+'''▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  '''+Fore.RED+'''█__█ █_ ███ █_█ █_▀█ █_▀█ █_ █ ▀_ Testing Mode'''+Fore.MAGENTA+'''
    '''+Fore.CYAN+'''DBFA Debugger >>> Permissive Options ~    
    '''+Fore.RED+'''▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬'''+Fore.WHITE)

                        citfacin = int(input("Waiting for input:: "))
                        if citfacin == 1:
                            # window.close()
                            with HiddenPrints():
                                try:
                                    sender = telegram_bot_sendtext(dt_string + "\n" + "Accessed: CIT del cust recs - deltaDBFA")
                                    print(sender)
                                except Exception:
                                    pass
                            os.startfile(r'securepack.py')
                            time.sleep(1)
                            os._exit(0)
                        if citfacin == 2:
                            # window.close()
                            with HiddenPrints():
                                try:
                                    sender = telegram_bot_sendtext(dt_string + "\n" + "Accessed: CIT del voucher recs - deltaDBFA")
                                    print(sender)
                                except Exception:
                                    pass
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
            else:
                print("This function is restricted on your account.")


        # Direct Calls Section - 2
        elif decfac in ("2a", "2A", "2 a", "2 A"):
            del2a()
            logger.write("--------------------------------------- \n")
            logger.write("  \n")
            logger.write("Date and time: ") #including the date and time of billing (as taken from the system)
            logger.write(dt_string)
            logger.write(" \n")
            logger.write("New customer registered! ")
            #x = " custname: " + custname + " custemail: " + email + "\n"
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
            if str(settingscommondumpfetch(10)) == "Administrator":
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
            else:
                print("This function is restricted on your account ")



        # Direct Calls Section - 3
        elif decfac in ("3a", "3A", "3 a", "3 A"):
            del3a()

        elif decfac in ("3b", "3B", "3 b", "3 B"):
            del3b()

        elif decfac in ("3c", "3C", "3 c", "3 C"):
            if str(settingscommondumpfetch(10)) == "Administrator":
                del3c()
            else:
                print("This function is restricted on your account.")

        elif decfac in ("3d", "3D", "3 d", "3 D"):
            del3d()

        elif decfac in ("3e", "3E", "3 e", "3 E"):
            if str(settingscommondumpfetch(10)) == "Administrator":
                del3e()
                logger.write("\n--------------------------------------- \n")
                logger.write("Sales log accessed! ")
            else:
                print("This function is restricted on your account.")


        elif decfac in ("3f", "3F", "3 f", "3 F"):
            if str(settingscommondumpfetch(10)) == "Administrator":
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
            else:
                    print("This function is restricted on your account.")

        elif decfac in ("3g", "3G", "3 f", "3 F"):
            if str(settingscommondumpfetch(10)) == "Administrator":
                print("Deep Archival Engine")
                del3g()
            else:
                    print("This function is restricted on your account.")

        elif decfac in (None, "", " "):
            print("Please select a valid main-menu option. erc101\n\n")

        else:
            print("Please select a valid main-menu option. erc101\n\n")

except:
    try:
        import os, requests, time
        os.system('cls')
        error_message = traceback.format_exc()
        print("DBFA has crashed due to unexpected reasons. ")
        print("DBFA will now automatically check its installation for integrity issues:: ")
        time.sleep(1)
        print("Error recieved from interpreter follows:")
        print("    ", error_message)
        time.sleep(3)
        time.sleep(2)
        from md5checker import make_hash

        print("-------------------------------------------------")
        print(" delta Installation Integrity Validation Service")
        print("-------------------------------------------------")
        time.sleep(1)

        listing = ('bleading_edge', 'modif2fa', 'dbfaempman', 'plotter', 'delauth', 'dbfabackupper', 'authtimeout', 'securepack', 'securepackxvc', 'wrelogin', 'run_DBFA')

        print("Fetching MD5 from server.")
        servermd5 = ((requests.get("https://raw.github.com/deltaonealpha/DBFAcrashhandler/main/md5")).content).decode('utf-8')
        #.replace(" ", "").replace("\n", "")
        serverdump = (servermd5.split())
        print("Arranging hashes ###")
        server_md5 = []
        server_md5.append(serverdump[0].replace(" ", "").replace("\n", ""))
        server_md5.append(serverdump[1].replace(" ", "").replace("\n", ""))
        server_md5.append(serverdump[2].replace(" ", "").replace("\n", ""))
        server_md5.append(serverdump[3].replace(" ", "").replace("\n", ""))
        server_md5.append(serverdump[4].replace(" ", "").replace("\n", ""))
        server_md5.append(serverdump[5].replace(" ", "").replace("\n", ""))
        server_md5.append(serverdump[6].replace(" ", "").replace("\n", ""))
        server_md5.append(serverdump[7].replace(" ", "").replace("\n", ""))
        server_md5.append(serverdump[8].replace(" ", "").replace("\n", ""))
        server_md5.append(serverdump[9].replace(" ", "").replace("\n", ""))
        server_md5.append(serverdump[10].replace(" ", "").replace("\n", ""))

        print("Fetching logged MD5.")
        try:
            localdump = str(open(parentdir+'\\md5').read())
            sorteddump = (localdump.split())
            print("Arranging hashes ###")
            local_md5 = []
            local_md5.append(sorteddump[0].replace(" ", "").replace("\n", ""))
            local_md5.append(sorteddump[1].replace(" ", "").replace("\n", ""))
            local_md5.append(sorteddump[2].replace(" ", "").replace("\n", ""))
            local_md5.append(sorteddump[3].replace(" ", "").replace("\n", ""))
            local_md5.append(sorteddump[4].replace(" ", "").replace("\n", ""))
            local_md5.append(sorteddump[5].replace(" ", "").replace("\n", ""))
            local_md5.append(sorteddump[6].replace(" ", "").replace("\n", ""))
            local_md5.append(sorteddump[7].replace(" ", "").replace("\n", ""))
            local_md5.append(sorteddump[8].replace(" ", "").replace("\n", ""))
            local_md5.append(sorteddump[9].replace(" ", "").replace("\n", ""))
            local_md5.append(sorteddump[10].replace(" ", "").replace("\n", ""))
        except:
            print("DBFA's code has been tampered with! Please rectify this to avoid such program crashes!")
            print("    rrtt - Master Copy Error: dta=intl.err_instldir?imp=md5lognotfound")


        print("Hashing MD5 from deployed code.")
        live_md5 = []
        live_md5.append(make_hash('bleading_edge.py', algo='md5'))
        live_md5.append(make_hash('modif2fa.py', algo='md5'))
        live_md5.append(make_hash('dbfaempman.py', algo='md5'))
        live_md5.append(make_hash('plotter.pyw', algo='md5'))
        live_md5.append(make_hash('delauth.py', algo='md5'))
        live_md5.append(make_hash('dbfabackupper.py', algo='md5'))
        live_md5.append(make_hash('authtimeout.pyw', algo='md5'))
        live_md5.append(make_hash('securepack.py', algo='md5'))
        live_md5.append(make_hash('securepackxvc.py', algo='md5'))
        live_md5.append(make_hash('wrelogin.pyw', algo='md5'))
        live_md5.append(make_hash('run_DBFA.pyw', algo='md5'))
        print("Arranging hashes ###")


        alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        for i in range(len(listing)):
            if live_md5[i] != local_md5[i]:
                print("! - Misaligned MD5 at")
                print(live_md5[i], local_md5[i], "////\n")
        print("Alignment check done p1x")

        for i in server_md5:
            arter = ""
            for j in i.replace(" ", "").replace("\n", ""):
                if str(j).isalpha() is True:
                    arter += '%d'%(alphas.index(j.lower()))
                else:
                    arter += j
            server_md5[server_md5.index(i)] = int(arter)

        for i in local_md5:
            arter = ""
            for j in i.replace(" ", "").replace("\n", ""):
                if str(j).isalpha() is True:
                    arter += '%d'%(alphas.index(j.lower()))
                else:
                    arter += j
            local_md5[local_md5.index(i)] = int(arter)

        for i in live_md5:
            arter = ""
            for j in i.replace(" ", "").replace("\n", ""):
                if str(j).isalpha() is True:
                    arter += '%d'%(alphas.index(j.lower()))
                else:
                    arter += j
            live_md5[live_md5.index(i)] = int(arter)

        for i in range(len(listing)):
            if live_md5[i] != local_md5[i]:
                print("! - Misaligned MD5 at")
                print(live_md5[i], local_md5[i], "////\n")
        print("Alignment check done p2x")

        print("\n")
        if live_md5 != local_md5:
            marker = 1
            issue = i
        elif live_md5 == local_md5:
            marker = 2

        time.sleep(3)

        if marker == 1:
            if sum(server_md5) == sum(live_md5):
                os.startfile(r'ep1.pyw')
            elif sum(server_md5) > sum(live_md5):
                os.startfile(r'ep2.pyw')
            elif sum(server_md5) < sum(live_md5):
                os.startfile(r'ep3.pyw')
        elif marker == 2:
                os.startfile(r'ep4.pyw')
        else:
            print("Integrity checker service failed to execute properly \\ | / |  -_- -_- -_-  \\ | / | ")
            time.sleep(10)

    except IndexError:
        print("----------------------------------------------")
        print("dnss internal error: (error code - rep.pvt-01)")
        time.sleep(10)


# End of program
# Available on github: www.github.com/deltaonealpha/DBFA
# https://deltaonealpha.github.io/DBFA/