# New gui login script instead of built-in eww..
# Full changelog on github
# v2.1 base snippets (sample code)


import getpass, time, pathlib, os, sqlite3
from pathlib import Path
import os #used to execute Windows-level commands
if os.path.exists(r'userblock.zconf'):
    p = Path('userblock.zconf')
    p.rename(p.with_suffix('.txt'))
if os.path.exists(r'userblock.txt'):
    userblock = open(r"userblock.txt","r") #Opens/ creates the registry file
    valfn = 1 #all good
else:
    valfn = 0 #login bypass
if os.path.exists(r'userblock.txt'):
    userblock.close()  
    os.remove(r'userblock.txt')
elif os.path.exists(r'userblock.zconf'):
    userblock.close()
    os.remove(r'userblock.zconf')
 
#Values stored in two dictionaries
data = {"1":40000, "2":55000, "3":67000, "4":25000, "5":21000, "6":14000, "7":13000, "8":220000, "9":4500, "10":17000, "11":1200, "12":3700, "13":4500, "14":2200, "15":700, "16":2750, "17":6499, "18":1499, "19":799, "20":27000, "21":6750, "22":2100, "23":1199, "24":3210, "25":989, "26":750, "27":1700, "28":600, "29":2175, "30":890, "31":2100, "32":7158, "33":597, "34":347, "35":500, "36":300, "37":1097, "38":80000, "39":87900, "40":23790}
namie = {"1":"TV 4K OLED 50", "2":"TV FHD OLED 50", "3":"8K QLED 80", "4":"Redmi K20 PRO", "5":"Redmi K20", "6":"Redmi Note 8 PRO", "7":"POCOPHONE F1", "8":"Mi MIX ALPHA", "9":"Wireless Headphones", "10":"Noise-Cancelling Wireless Headphones", "11":"Essentials Headphones", "12":"Gaming Headphones", "13":"Truly-Wireless Eadphones", "14":"Neckband-Style Wireless Earphones", "15":"Essentials Earphones", "16":"Gaming Earphones", "17":"30W Bluetooth Speakers", "18":"10W Bluetooth Speakers", "19":"Essentials Bluetooth Speaker", "20":"ULTRA Home Theatre", "21":"Essentials Home Theatre", "22":"  Wired Speaker - 5.1", "23":"  Essentials Wired Speaker - STEREO", "24":"Tactical Power Bank 30000mah", "25":"Essentials Power Bank 10000mah", "26":"Essentials Mouse", "27":"Logitech RGB Gaming Mouse with Traction & Weight Adjustment", "28":"Tactical Essentials Keyboard", "29":"Mechanical Cherry MX (Red) RGB Gaming Keyboard", "30":"Polowski Tactical Flashlight", "31":"OneFiber Wi-Fi Router AX17", "32":"Mijia Mesh Wi-Fi Router", "33":"lapcare 120W Laptop Adapter", "34":"lapcare 60W Laptop Adapter", "35":"Spigen Phone Case(s)", "36":"Essentials Phone Charger 10W", "37":"HyperPower Type-C Gallium-Nitride Charger 100W", "38":"ASUS Zephyrus G14 Gaming Laptop", "39":"L XPS 15 Content Creator's Laptop", "40":"Hewlett-Packard Essential's Student's Laptop (Chromebook)"}


'''
def floodscreen():
    import cv2 
    image = cv2.imread("imagepx.png")
    cv2.imshow("Please wait...", image)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()
'''


print("Billing Framework System")
time.sleep(1.3)
command = "cls"
os.system(command) #sys command cls
 

def mainmenu():
    from colorama import init, Fore, Back, Style #color-settings for the partner/sponsor adverts
    init(convert = True)
    print(Fore.RED) #red-line to indicate program start
    print("---------------------------------------------")
    print(Fore.WHITE)
    print('A word from our partner: ' + Fore.BLACK + Back.CYAN + 'HOTEL? Trivago!') #Text over here #Custom advert
    print(Style.RESET_ALL) 
    print("Enter: ") 
    print("'1' to GENERATE INVOICE")
    print("'2' to REGISTER CUSTOMER,")
    print("'3' to VIEW REGISTERED CUSTOMERS,")
    print("'4' to VIEW GENERATED INVOICES,")
    print("'5' to REVIEW STORE LISTING,")
    print("'6' to REVIEW LICENSING INFORMATION,")
    print("and '7' to exit the framework.")
    print("---------------------------------------------")
    print()
    print()
 

#void-setup
from datetime import datetime  #reports billing time-date
now = datetime.now() #current acc to sys time
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
logger = open(r"registry.txt", "a+")  #opens/creates the registry file
logger.write("----------------------------------------- \n")
logger.write('User identified from login: ed')
logger.write("\n")
logger.write("Automated Store Registry:\n")
import time  #to provide delays to make the system run seamlessly
conn = mysql.connector.connect(host='localhost', database='delta', user='root', password='shieldlogmein')  #sql connection parameters
cursor = conn.cursor()
cursor.execute("select * from cust")
row = cursor.fetchone()


def inserter(custid, custname, email):  #defining a function to input data into the SQL database's table
    conn = mysql.connector.connect(host='localhost', database='delta', user='root', password='shieldlogmein')
    cursor = conn.cursor(buffered=True)
    str = "insert into cust(custid, custname, email) values('%s', '%s', '%s')"
    io = (custid, custname, email)
    cursor.execute(str % io)
    conn.commit()
    print("Customer", custname, "registered in store directory")
 
 
#void-loop phase
#floodscreen()

import win32api  #small one-time pop-up for adverts; # Windows API by Microsoft
win32api.MessageBox(0, 'Please review licensing terms before usage', 'Licensing!')  # '0' or '1' for on/off, first str for text, second str for windows heading
print("Heyy there!",  'ed') #username from login process
time.sleep(1.34)
if valfn == 1:
    logger.write("Oauth bypass - registering this for security logs")
    time.sleep(1)
    print("-------DBFA standardised billing framework-------")
    print("We see you there, hackerman.")
    time.sleep(1)
    print("It has been detected that you have bypassed the login process.")
    time.sleep(1)
    print("The program shall now exit. Error code:013")
    time.sleep(2)
    print("------------------------------------------")
    time.sleep(5)
    exit()
 
while(1): #while (always) true
    mainmenu() #mainmenu
    time.sleep(0.3)  #for a seamless experience
    decfac = int(input("Select option: "))
    #Bill Mode
    if decfac == 1:
        print()
        print("Invoicing: ")
        print()
        custid = input("Enter customer ID (enter if unregistered): ")
        logger.write("-----------------  ") #writing to log file
        logger.write("Cust. ID: \n")
        logger.write(custid)
        logger.write("  \n")
        logger.write("Date and time: \n") #including the date and time of billing (as taken from the system)
        logger.write(dt_string)
        logger.write(" \n")
        abcd1 = 1
        time.sleep(0.3) #for a seamless experience
        
        numfac = int(input("Number of purchased items: "))
        time.sleep(0.34) #for a seamless experience
        afac = 0
        billiemaster = 0 #variable for totalling the price
        while(afac!=numfac):
            item = input("Enter purchased product code: ")
            time.sleep(0.3) #for a seamless experience
            if item in data:
                billiemaster+=data[item]
                print("Product purchased: ", namie[item], " costing: ", data[item])
                print("---")
                logger.write("Appending product to order: \n")  #writing to file
                logger.write(namie[item])
                logger.write(" \n")

            else:
                print("Invalid entry! Retry: ")
                print("---")
            afac+=1
        #tax = int(input("Enter the net tax %: "))  #comment and uncomment tkinter lines to use GUI-based input
        print("18% standard GST - Incoicing!")
        time.sleep(0.4)  #for a seamless experience
        #discount = int(simpledialog.askstring(title="deltaSTOREMANAGER",prompt="Enter the discount percentage: "))
        discount = int(input("Enter discount % (if any): ")) #comment and uncomment tkinter lines to use GUI-based input
        print(discount, "% net discount - Invoicing!")
        time.sleep(0.2) #for a seamless experience
        print("Invoicing... DBFA")
        time.sleep(0.4) #for a seamless experience
        tota = (((18/100)*billiemaster)+billiemaster)
        total = tota-((discount/100)*tota)
        print("Invoice ID: ", abcd1, "; Total: ", total)
        logger.write("Total amount billed for: \n") #writing to file
        logger.write(str(total))
        logger.write("\n")
        abcd1+=1
        afac+=1
        time.sleep(1.5) #for a seamless experience
        print()
        print()
    #Register Customer
    elif decfac == 2:
        print("Loading server connection....")  #SQL connection prompt
        time.sleep(0.4)  #for a seamless experience
        conn = mysql.connector.connect(host='localhost', database='delta', user='root', password='shieldlogmein')
        cursor = conn.cursor()
        cursor.execute("select * from cust")
        row = cursor.fetchone()
        #takes values from the SQL database
        countss = 0
        while row is not None:
            displayguyfornouse = row
            row = cursor.fetchone()
            countss+=1
        incfac = countss + 1
        print("Registering customer with ID: ", incfac)
        custname = input("Name: ")
        email = input("Customer's E-mail ID: ")
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
        print("Customer ID", incfac, "registered in directory.")
        print("---------------------------------------")
        print(" ")
        print(" ")
        time.sleep(1) #for a seamless experience
    #VIEW ALL CUSTOMERS
    elif decfac == 3:
        print()
        print("Loading server connection....")  #SQL connection prompt
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
        logger.write("Customer registry accessed! \n")
        logger.write("--------------------------------------- \n")
        cursor.close()
        conn.close()
        print()
        print()
        time.sleep(2) #delay for easy-table viewing
    #View Generated Bills
    elif decfac == 4:
        #password verification as sales record is not to be shown to all;
        print("Password echo shall be supressed for security.")
        passw = getpass.getpass(prompt='Enter root password to view store activity registry: ', stream=None)
        logger.write("  \n")
        logger.write("Date and time: ") #including the date and time of billing (as taken from the system)
        logger.write(dt_string)
        logger.write(" \n")
        if passw == "root":
                time.sleep(1) #for a seamless experience
                print("Hold on, moneybags.")
                time.sleep(0.4)
                print("There ya go:: ")
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
            print("Wrong, sneaky-hat. Try again: ")
            print(" ")
            print("Password echo shall be supressed for security.")
            passw = getpass.getpass(prompt='Enter root password to view store activity registry: ', stream=None)
            if passw == "root":
                    time.sleep(1) #for a seamless experience
                    print("Hold on, moneybags.")
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
    elif decfac == 7:
        if os.path.exists(r'userblock.txt'):
            userblock.close()
            os.remove(r'userblock.txt')
        if os.path.exists(r'userblock.zconf'):
            userblock.close()
            os.remove(r'userblock.zconf')
        print("System exit option: ")
        print("Please wait. Encrypting program before exiting.......")
        print("Exiting system now:: ")
        time.sleep(2)
        break
        exit()
        os.close('securepack.pyw')
    elif decfac == 6:
        print("Fetching latest licensing information.......")
        print(" ")
        print(" ")
        print("DBFA by Pranav Balaji, 2020")
        print(" ")
        print("_______ Licensing _______")
        print("           GNU PUBLIC LICENSE - TERMS AND CONDITIONS")
        print("    <deltaBillingFramework>  Copyright (C) 2020 Pranav Balaji")
        print("    This program comes with ABSOLUTELY NO WARRANTY; for details type *show w*.")
        print("    This is free software, and you are welcome to redistribute it")
        print("    under certain conditions; type *show c* for details. ")
        print(" ")
        time.sleep(0.5)
        print(" ")
        print("Visit: www.github.com/deltaonealpha/deltaBillingFramework for complete licensing terms. ")
        print(" ")
        print(" ")
        aacsbcfac = int(input("Enter '1' to view complete licensing stuff or '2' to return."))
        if aacsbcfac == 1:
            print(" ")
            print("Please select to open with your prefered text viewer/ edittor.")
            os.startfile("LICENSE")
            print(" ")
            print(" ")
            print("--------------------------------------------------")
        else:
            continue
# Program ENDS here
# IF YOU WANT AN UNREADABLE BYTE CODE FILE TO ENCRYPT AT BASICS THEN USE THIS:
# Use python -OO -m py_compile hms1.py with Anaconda and - 
# - rename the file in the py_cache folder by changing the extension to .py from .pyc, ultimately renaming it to hms1c.py
#
#