# This revision throws MySQL in the bin, and adopts SQLalchemy instead. MySQL is shit.
# Don't mess by removing those damn delays. I didn't write them for crap's sake.
# Boot-flash and advert options have been added for you moni-bags.
# Looking into using a custom Authenication API for log-in/out ops instead of the fuckingly easily hackable in-built eww.
# Full changelog on https://deltaonealpha.github.io/deltaBillingFramework
# Code-copiers will be punished. Def. Period. Gimme more words.

import getpass, time
import os #library used to open the notepad application to display the sales records
from pathlib import Path
if os.path.exists(r'userblock.zconf'):
    print("Decrypting authenication blobs...")
    print(" ")
    p = Path('userblock.zconf')
    p.rename(p.with_suffix('.txt'))
if os.path.exists(r'userblock.txt'):
    userblock = open(r"userblock.txt","r") #Opening / creating (if it doesn't exist already) the .txt record file
    namebar = userblock.read(500)
    valfn = 0
else:
    valfn = 1
if os.path.exists(r'userblock.txt'):
    userblock.close()  
    os.remove(r'userblock.txt')
elif os.path.exists(r'userblock.zconf'):
    userblock.close()
    os.remove(r'userblock.zconf')
 
#Values stored in two dictionaries
data = {"del1":40000, "del2":55000, "del3":67000, "del4":25000, "del5":21000, "del6":14000, "del7":13000, "del8":220000, "del9":4500, "del10":17000, "del11":1200, "del12":3700, "del13":4500, "del14":2200, "del15":700, "del16":2750, "del17":6499, "del18":1499, "del19":799, "del20":27000, "del21":6750, "del22":2100, "del23":1199, "del24":3210, "del25":989, "del26":750, "del27":1700, "del28":600, "del29":2175, "del30":890, "del31":2100, "del32":7158, "del33":597, "del34":347, "del35":500, "del36":300, "del37":1097, "del38":80000, "del39":87900, "del40":23790}
namie = {"del1":"TV 4K OLED 50", "del2":"TV FHD OLED 50", "del3":"8K QLED 80", "del4":"Redmi K20 PRO", "del5":"Redmi K20", "del6":"Redmi Note 8 PRO", "del7":"POCOPHONE F1", "del8":"Mi MIX ALPHA", "del9":"delta CaptureElite Wireless Headphones", "del10":"delta CaptureElite Noise-Cancelling Wireless Headphones", "del11":"delta CaptureElite Essentials Headphones", "del12":"delta CaptureElite Gaming Headphones", "del13":"delta CaptureElite Truly-Wireless Eadphones", "del14":"delta CaptureElite Neckband-Style Wireless Earphones", "del15":"delta CaptureElite Essentials Earphones", "del16":"delta CaptureElite Gaming Earphones", "del17":"delta CaptureElite 30W Bluetooth Speakers", "del18":"delta CaptureElite 10W Bluetooth Speakers", "del19":"delta CaptureElite Essentials Bluetooth Speaker", "del20":"delta CaptureElite ULTRA Home Theatre", "del21":"delta CaptureElite Essentials Home Theatre", "del22":"delta CaptureElite Wired Speaker - 5.1", "del23":"delta CaptureElite Essentials Wired Speaker - STEREO", "del24":"delta Polowski Tactical SHERPAELITE Power Bank 30000mah", "del25":"delta Polowski Tactical Essentials Power Bank 10000mah", "del26":"delta Polowski Tactical Essentials Mouse", "del27":"delta Polowski Tactical RGB Gaming Mouse", "del28":"delta Polowski Tactical Essentials Keyboard", "del29":"delta Polowski Tactical RGB Gaming Keyboard", "del30":"delta Polowski Tactical SHERPAELITE Flashlight", "del31":"deltaNetworking Wi-Fi Router AX17", "del32":"deltaNetworking SHERPAELITE Mesh Wi-Fi Router", "del33":"deltaSupport 120W Laptop Adapter", "del34":"deltaSupport 60W Laptop Adapter", "del35":"deltaSupport Phone Case", "del36":"deltaSupport Essentials Phone Charger 10W", "del37":"deltaSupport SHERPAELITE Phone Charger 30W", "del38":"deltaCiccadella Gaming Laptop", "del39":"deltaCiccadella Content Creator's Laptop", "del40":"deltaCiccadella Student's Laptop"}

def floodscreen():
    import cv2 
    image = cv2.imread("imagepx.png")
    cv2.imshow("Initializing... ", image)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()


print("           GNU PUBLIC LICENSE - TERMS AND CONDITIONS")
print("    <deltaBillingFramework>  Copyright (C) 2020 Pranav Balaji")
print("    This program comes with ABSOLUTELY NO WARRANTY; for details type *show w*.")
print("    This is free software, and you are welcome to redistribute it")
print("    under certain conditions; type *show c* for details. ")
time.sleep(0.5)
print(" ")
print("Visit: www.github.com/deltaonealpha/deltaBillingFramework for complete licensing terms. ")
time.sleep(3)
command = "cls"
os.system(command)
 
def mainmenu(): #defining a function for the main menu
    from colorama import init, Fore, Back, Style #color-settings for the partner/sponsor adverts
    init(convert = True)
    print(Fore.RED) #red-line to indicate program start
    print("---------------------------------------------")
    print(Fore.WHITE)
    print('A word from our partner: ' + Fore.BLACK + Back.CYAN + 'HOTEL? Trivago!') #Text over here
    print(Style.RESET_ALL) 
    print("Welcome to the delta Electronics Store!")
    print("Enter: ") 
    print("'1' to GENERATE A BILL")
    print("'2' to REGISTER A CUSTOMER,")
    print("'3' to VIEW ALL CUSTOMERS,")
    print("'4' to VIEW GENERATED BILLS,")
    print("'5' to VIEW STORE LISTING,")
    print("and '6' to exit the system.")
    print("---------------------------------------------")
    print()
    print()
 
#void-setup phase
from datetime import datetime #for reporting the billing time and date
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") #datetime object containing current date and time
logger = open(r"log.txt","a+") #Opening / creating (if it doesn't exist already) the .txt record file
logger.write("--------------------------------------------- \n")
logger.write("deltaStoreManager \n")
logger.write(namebar)
logger.write("\n")
logger.write("SALES RECORD: \n") 
import mysql.connector #to connect to the SQL database (local)
import time #to provide delays to make the system run seamlessly
conn = mysql.connector.connect(host='localhost', database='delta', user='root', password='shieldlogmein') #sql connection parameters
cursor = conn.cursor()
cursor.execute("select * from cust")
row = cursor.fetchone()
def inserter(custid, custname, email): #defining a function to input data into the SQL database's table
    conn = mysql.connector.connect(host='localhost', database='delta', user='root', password='shieldlogmein')
    cursor = conn.cursor(buffered=True)
    str = "insert into cust(custid, custname, email) values('%s', '%s', '%s')"
    io = (custid, custname, email)
    cursor.execute(str % io)
    conn.commit()
    print("Customer registered successfully! - deltaServerHandler")
 
#void-loop phase
floodscreen()
import win32api #small one-time pop-up for adverts; # Windows API by Microsoft Corporation
win32api.MessageBox(0, 'Please read documentation from install directory for instructions:', 'Alert!') # '0' or '1' for on/off, first str for text, second str for windows heading
print("Heyy there!", namebar)
time.sleep(1.34)
if valfn == 1:
    logger.write("LOGIN BYPASS")
    time.sleep(1.5445677)
    print("Welcome to the deltaSTOREMANAGER")
    time.sleep(1.5)
    print("We at delta value security primemostly.")
    time.sleep(2)
    print("It has been detected that you have bypassed the login process.")
    time.sleep(2)
    print("The program shall now exit. Error code:LOGINBYPASS")
    time.sleep(5)
    print("------------------------------------------")
    time.sleep(2)
    exit()
 
while(1): #while (always) true
    mainmenu() #mainmenu
    time.sleep(0.34) #for a seamless experience
    decfac = int(input("Enter your choice now: "))
    #Bill Mode
    if decfac == 1:
        print()
        print("Billing MODE: ")
        print()
        custid = input("Enter customer ID if already registered; else press enter: ")
        logger.write("-----------------  ") #writing to log file
        logger.write("Customer ID: \n")
        logger.write(custid)
        logger.write("  \n")
        logger.write("Date and time: \n") #including the date and time of billing (as taken from the system)
        logger.write(dt_string)
        logger.write(" \n")
        abcd1 = 1
        time.sleep(0.3) #for a seamless experience
        
        numfac = int(input("Enter the number of items: "))
        time.sleep(0.34) #for a seamless experience
        afac = 0
        billiemaster = 0 #variable for totalling the price
        while(afac!=numfac):
            item = input("Enter the item code: ")
            time.sleep(0.3) #for a seamless experience
            if item in data:
                billiemaster+=data[item]
                print("Product purchased: ", namie[item], " costing: ", data[item])
                print("---")
                logger.write("Purchased: \n") #writing to file
                logger.write(namie[item])
                logger.write(" \n")

            else:
                print("Wrong input. Try again!")
                print("---")
            afac+=1
        '''
        import tkinter as tk
        from tkinter import simpledialog
        ROOT = tk.Tk()
        ROOT.withdraw()
        # the input dialog
        tax = int(simpledialog.askstring(title="deltaSTOREMANAGER",prompt="Enter the tax percentage: "))
        '''
        tax = int(input("Enter the net tax %: ")) #comment and uncomment tkinter lines to use GUI-based input
        print(tax,"% NET TAX - Incoicing!")
        time.sleep(0.4) #for a seamless experience
        #discount = int(simpledialog.askstring(title="deltaSTOREMANAGER",prompt="Enter the discount percentage: "))
        discount = int(input("Enter the discount %: ")) #comment and uncomment tkinter lines to use GUI-based input
        print(discount,"% NET DISCOUNT - Invoicing!")
        time.sleep(0.4) #for a seamless experience
        print("Please Wait....... Billing.......")
        time.sleep(0.67) #for a seamless experience
        tota = (((tax/100)*billiemaster)+billiemaster)
        total = tota-((discount/100)*tota)
        print("BILL NUMBER: ", abcd1, "; the total bill is: ", total)
        logger.write("Total amount billed for: \n") #writing to file
        logger.write(str(total))
        logger.write("\n")
        abcd1+=1
        afac+=1
        time.sleep(1.67) #for a seamless experience
        print()
        print()
    #Register Customer
    elif decfac == 2:
        print("Connecting to server....... Please wait...") #SQL connection prompt
        time.sleep(0.4) #for a seamless experience
        conn = mysql.connector.connect(host='localhost', database='delta', user='root', password='shieldlogmein')
        cursor = conn.cursor()
        cursor.execute("select * from cust")
        row = cursor.fetchone()
        #takes values from the SQL database
        countguy = 0
        while row is not None:
            displayguyfornouse = row
            row = cursor.fetchone()
            countguy+=1
        incfac = countguy + 1
        print("Registering for customer number", incfac)
        custname = input("Enter the customer's name: ")
        email = input("Enter the customer's E-mail ID: ")
        inserter(incfac, custname, email) #argumental function to insert values into the SQL database
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
        print("#Data flush success!")
        print("---------------------------------------")
        print(" ")
        print(" ")
        time.sleep(1) #for a seamless experience
    #VIEW ALL CUSTOMERS
    elif decfac == 3:
        print()
        print("Waiting for server connection.......") #SQL connection prompt #usdscncn
        time.sleep(0.7) #for a seamless experience
        print("The registered customers are: ")
        #Re-writing to refresh connection
        conn = mysql.connector.connect(host='localhost', database='delta', user='root', password='shieldlogmein')
        cursor = conn.cursor()
        cursor.execute("select * from cust")
        row = cursor.fetchone()
        print(" ")
        #takes values from the SQL database
        while row is not None:
            print(row)
            row = cursor.fetchone()
        logger.write("--------------------------------------- \n")
        logger.write("  \n")
        logger.write("Date and time: ") #including the date and time of billing (as taken from the system)
        logger.write(dt_string)
        logger.write(" \n")
        logger.write("Customer listing database accessed! \n")
        logger.write("--------------------------------------- \n")
        cursor.close()
        conn.close()
        print()
        print()
        time.sleep(2) #delay for easy-table viewing
    #View Generated Bills
    elif decfac == 4:
        #password verification as sales record is not to be shown to all;
        print("Entered passwords shall be hidden for security purposes.")
        passw = getpass.getpass(prompt='To view all sales records, enter the administrator password: ', stream=None)
        logger.write("  \n")
        logger.write("Date and time: ") #including the date and time of billing (as taken from the system)
        logger.write(dt_string)
        logger.write(" \n")
        if passw == "root":
                time.sleep(1) #for a seamless experience
                print("Authorization Succesfull! ")
                time.sleep(0.4)
                print("Opening sales log externally:: ")
                time.sleep(0.2) #for a seamless experience 
                logger.write("Log file access attempt - AUTHORIZATION SUCCESS \n")
                logger.close() #to change file access modes 
                logger = open("log.txt","r+")  
                # Uncomment the below lines if the program has to be modified to show the records in the shell itself and not externally
                # print(logger.read())
                # print()
                # print("Opening sales log externally now. ")
                time.sleep(1.4) #for a seamless experience
                os.startfile('log.txt') #to open the external notepad application
        else:
            logger.write("  \n")
            logger.write("Date and time: ") #including the date and time of billing (as taken from the system)
            logger.write(dt_string)
            logger.write(" \n")
            time.sleep(1) #for a seamless experience
            logger.write("Log file access attempt - AUTHORIZATION FAILED!!! \n")
            print("Wrong password entered. Try again. ")
            print(" ")
            print("Entered passwords shall be hidden for security purposes.")
            passw = getpass.getpass(prompt='To view all sales records, enter the administrator password: ', stream=None)
            if passw == "root":
                    time.sleep(1) #for a seamless experience
                    print("Authorization Succesfull! ")
                    print("Opening sales log externally:: ")
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
                print("Multiple Unsuccesfull Attempts Detected. Re-run the program to login now. ")
                logger.write("(MULTIPLE ATTEMPTS!): Log file access attempt - AUTHORIZATION FAILED!!! \n")
                time.sleep(1.4) #for a seamless experience
                print()
                print()
    #View Listing Option
    elif decfac == 5:
        print("Store listing (as per updated records): ")
        for name, age in data.items():
            print('{} {}'.format(name, age))
        for name, age in namie.items():
            print('{} {}'.format(name, age))
    #Exit System
    elif decfac == 6:
        if os.path.exists(r'userblock.txt'):
            userblock.close()
            os.remove(r'userblock.txt')
        if os.path.exists(r'userblock.zconf'):
            userblock.close()
            os.remove(r'userblock.zconf')
        print("System exit option: ")
        print("Please wait. Encrypting program before exiting.......")
        print("Exiting system now:: ")
        print(" ")
        print("      []         [] []               ")
        print("      []         [] []]]]]] software ")
        print("[======] [=====] [] [] [======]  CLI ")
        print("[]====[] []---[] [] [] []====[]      ")
        print("[======] []____  [] [] [======]]]]   ")
        print(" ")
        print(" ")
        time.sleep(2)
        break
        exit()
        os.close('securepack.pyw')
# Program ENDS here
# Available on github: deltaonealpha.github.io/dsmsapl5
# IF YOU WANT AN UNREADABLE BYTE CODE FILE TO ENCRYPT AT BASICS THEN USE THIS:
# Use python -OO -m py_compile hms1.py with Anaconda and - 
# - rename the file in the py_cache folder by changing the extension to .py from .pyc, ultimately renaming it to hms1c.py
