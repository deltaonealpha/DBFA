from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('MiLanProVF', r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\MiLanProVF.ttf'))
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm


print("FHJ")


# MySQL is ewww...
# New gui login script instead of built-in eww..
# Full changelog on github
# Code-copiers will be punished. Def. Period. Gimme more words.

import getpass, time, pathlib, os, sqlite3
import os #library used to open the notepad application to display the sales records
if os.path.exists(r'userblock.zconf'):
    print("Decrypting authenication blobs...")
    print(" ")
    p = Path('userblock.zconf')
    p.rename(p.with_suffix('.txt'))
if os.path.exists(r'userblock.txt'):
    userblock = open(r"userblock.txt","r") #Opening / creating (if it doesn't exist already) the .txt record file
    valfn = 0
else:
    valfn = 0
if os.path.exists(r'userblock.txt'):
    userblock.close()  
    os.remove(r'userblock.txt')
elif os.path.exists(r'userblock.zconf'):
    userblock.close()
    os.remove(r'userblock.zconf')

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



#Values stored in two dictionaries
data = {"1":40000, "2":55000, "3":67000, "4":25000, "5":21000, "6":14000, "7":13000, "8":220000, "9":4500, "10":17000, "11":1200, "12":3700, "13":4500, "14":2200, "15":700, "16":2750, "17":6499, "18":1499, "19":799, "20":27000, "21":6750, "22":2100, "23":1199, "24":3210, "25":989, "26":750, "27":1700, "28":600, "29":2175, "30":890, "31":2100, "32":7158, "33":597, "34":347, "35":500, "36":300, "37":1097, "38":80000, "39":87900, "40":23790}
namie = {"1":"TV 4K OLED 50", "2":"TV FHD OLED 50", "3":"8K QLED 80", "4":"Redmi K20 PRO", "5":"Redmi K20", "6":"Redmi Note 8 PRO", "7":"POCOPHONE F1", "8":"Mi MIX ALPHA", "9":"Wireless Headphones", "10":"Noise-Cancelling Wireless Headphones", "11":"Essentials Headphones", "12":"Gaming Headphones", "13":"Truly-Wireless Eadphones", "14":"Neckband-Style Wireless Earphones", "15":"Essentials Earphones", "16":"Gaming Earphones", "17":"30W Bluetooth Speakers", "18":"10W Bluetooth Speakers", "19":"Essentials Bluetooth Speaker", "20":"ULTRA Home Theatre", "21":"Essentials Home Theatre", "22":"  Wired Speaker - 5.1", "23":"  Essentials Wired Speaker - STEREO", "24":"Tactical Power Bank 30000mah", "25":"Essentials Power Bank 10000mah", "26":"Essentials Mouse", "27":"Logitech RGB Gaming Mouse with Traction & Weight Adjustment", "28":"Tactical Essentials Keyboard", "29":"Mechanical Cherry MX (Red) RGB Gaming Keyboard", "30":"Polowski Tactical Flashlight", "31":"OneFiber Wi-Fi Router AX17", "32":"Mijia Mesh Wi-Fi Router", "33":"lapcare 120W Laptop Adapter", "34":"lapcare 60W Laptop Adapter", "35":"Spigen Phone Case(s)", "36":"Essentials Phone Charger 10W", "37":"HyperPower Type-C Gallium-Nitride Charger 100W", "38":"ASUS Zephyrus G14 Gaming Laptop", "39":"L XPS 15 Content Creator's Laptop", "40":"Hewlett-Packard Essential's Student's Laptop (Chromebook)"}

'''
def floodscreen():
    import cv2 
    image = cv2.imread("imagepx.png")
    cv2.imshow("Initializing... ", image)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()
'''


print(" Licensed under the GNU PUBLIC LICENSE")
print("<DBFA>  Copyright (C) 2020 Pranav Balaji")
print(" ")
print("Visit: www.github.com/deltaonealpha/deltaBillingFramework for complete licensing terms. ")
time.sleep(1.3)
command = "cls"
os.system(command)
 
def mainmenu(): #defining a function for the main menu
    from colorama import init, Fore, Back, Style #color-settings for the partner/sponsor adverts
    init(convert = True)
    print(Fore.RED) #red-line to indicate program start
    print("---------------------------------------------")
    print(Fore.WHITE)
    print('A word from our partner: ' + Fore.BLACK + Back.CYAN + 'HOTEL? Trivago!') #Text over here #Custom advert
    print(Style.RESET_ALL) 
    print("-------DBFA standardised billing framework-------")
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
 

#void-setup phase
from datetime import datetime  #for reporting the billing time and date
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")  #datetime object containing current date and time
logger = open(r"registry.txt", "a+")  #Opening / creating (if it doesn't exist already) the .txt record file
logger.write("----------------------------------------- \n")
logger.write("DBFA Billing Framework by Pranav Balaji\n")
logger.write("Licensed under the GNU PUBLIC LICENSE\n")
logger.write('ed')
logger.write("\n")
logger.write("Automated Store Registry:\n")
import time  #to provide delays to make the system run seamlessly

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
def inserter(custt, custname, email):  #defining a function to input data into the SQL database's table
    global conn
    str = "insert into cust(custt, custname, email) values('%s', '%s', '%s')"
    io = (custt, custname, email)
    conn.execute(str % io)
    conn.commit()
    print("Customer", custname, "registered in store directory")

 
#void-loop phase
#floodscreen()

from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("DFBA Framework Runtime Broker","Please read operational and licensing documentation prior to use.", duration = 2)
print("Heyy there!",  'ed')
time.sleep(1.34)
if valfn == 1:
    logger.write("Oauth bypass - registering for security")
    time.sleep(1)
    print("-------DBFA standardised billing framework-------")
    print("Security is something to be valued primemostly, in today's digital age.")
    toaster.show_toast("DFBA Framework Runtime Broker","Unauthenicated login detected!")
    print("It has been detected that you have bypassed the login process.")
    time.sleep(1)
    print("The program shall now exit. Error code:013")
    time.sleep(2)
    print("------------------------------------------")
    time.sleep(5)
    exit()
 
while(1): #while (always) true
    mainmenu() #mainmenu
    writer = ""
    #if os.path.exists(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\Generated_invoices\regin.txt'):
    #    os.remove(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\Generated_invoices\regin.txt')
    #regin = open(r"C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\Generated_invoices\regin.txt", "a+")  #Opening / creating (if it doesn't exist already) the .txt record file
    time.sleep(0.3)  #for a seamless experience
    decfac = int(input("Select option: "))
    #Bill Mode
    if decfac == 1:
        print()
        print("Invoicing: ")
        print()
        custt = input("Enter customer ID (enter if unregistered): ")
        logger.write("-----------------  ") #writing to log file
        logger.write("Cust. ID: \n")
        logger.write(custt)
        logger.write("  \n")
        logger.write("Date and time: \n") #including the date and time of billing (as taken from the system)
        logger.write(dt_string)
        logger.write(" \n")
        abcd1 = 1
        time.sleep(0.3) #for a seamless experience
        writer = writer + "DBFA Billing Framework" + "\n" + "\n" + "Billing time: " + dt_string + "\n" + "Customer ID: " + custt + "\n" + "-----------------------------" + "\n" + "\n"
        '''regin.write("DBFA Billing Framework")
        regin.write("\n")
        regin.write("\n")
        regin.write("Billing time: ")
        regin.write(dt_string)
        regin.write("\n")
        regin.write("Customer ID: ")
        regin.write(custt)
        regin.write("\n")
        regin.write("---------------------------------------")
        regin.write("\n")
        regin.write("\n")
        regin.write("\n")
        '''
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
                priceprod = '%d' % data[item]
                logger.write("Appending product to order: \n")  #writing to file
                logger.write(namie[item])
                logger.write(" \n")
                writer = writer + "Purchased: " + "\n" + namie[item] + "\n" + priceprod + "\n"
                '''
                regin.write("Purchased: \n")  #writing to file
                regin.write(namie[item])
                regin.write(" \n")
                regin.write('%d' % data[item])
                regin.write("\n")
                '''

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
        writer = writer + "\n" + "\n" + "Tax amount: 18%" + "\n"  + "\n" 
        '''
        regin.write("\n")
        regin.write("Discount applied: ")
        regin.write('%d' % discount)
        regin.write("\n")
        regin.write("Tax amount: 18%")
        regin.write("\n")
        regin.write("\n")
        '''
        print("Invoice ID: ", abcd1, "; Total: ", total)
        toaster.show_toast("DFBA Framework Runtime Broker:      Total billed for-",str(total), duration = 1)
        logger.write("Total amount billed for: \n") #writing to file
        #regin.write("NET TOTAL: \n") #writing to file
        writer = writer + "NET TOTAL: \n" + str(total) + "\n" 
        logger.write(str(total))
        logger.write("\n")
        #regin.write(str(total))
        #regin.write("\n")
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
        printfac = int(input("Enter '1' to print or anything to NOT: "))
        if printfac == 1:
            pass
            '''        
            import win32print, win32ui, win32gui
            import win32con, pywintypes            
            # create a dc (Device Context) object (actually a PyCDC)
            dc = win32ui.CreateDC()
            # convert the dc into a "printer dc"
            # get default printer
            printername = win32print.GetDefaultPrinter ()
            # leave out the printername to get the default printer automatically
            dc.CreatePrinterDC(printername)
            # you need to set the map mode mainly so you know how
            # to scale your output.  I do everything in points, so setting
            # the map mode as "twips" works for me.
            dc.SetMapMode(win32con.MM_TWIPS) # 1440 per inch
            # here's that scaling I mentioned:
            scale_factor = 20 # i.e. 20 twips to the point
            # start the document.  the description variable is a string
            # which will appear in the print queue to identify the job.
            dc.StartDoc('DBFA invoice printing')
            # to draw anything (other than text) you need a pen.
            # the variables are pen style, pen width and pen color.
            pen = win32ui.CreatePen(0, int(scale_factor), 0)
            # SelectObject is used to apply a pen or font object to a dc.
            dc.SelectObject(pen)
            # how about a font?  Lucida Console 10 point.
            # I'm unsure how to tell if this failed.
            font = win32ui.CreateFont({
                "name": "Lucida Console",
                "height": int(scale_factor * 10),
                "weight": 400,
            })
            # again with the SelectObject call.
            dc.SelectObject(font)
            # okay, now let's print something.
            # TextOut takes x, y, and text values.
            # the map mode determines whether y increases in an
            # upward or downward direction; in MM_TWIPS mode, it
            # advances up, so negative numbers are required to
            # go down the page.  If anyone knows why this is a
            # "good idea" please email me; as far as I'm concerned
            # it's garbage.
            dc.TextOut(scale_factor * 72,
                -1 * scale_factor * 72,
                "Testing...")
            # for completeness, I'll draw a line.
            # from x = 1", y = 1"
            dc.MoveTo((scale_factor * 72, scale_factor * -72))
            # to x = 6", y = 3"
            dc.LineTo((scale_factor * 6 * 72, scale_factor * 3 * -72))
            # must not forget to tell Windows we're done.
            dc.EndDoc()
            '''
            
        else:
            pass
        print()
        #regin.close()
        print()
    #Register Customer
    elif decfac == 2:
        print("Loading server connection....")  #SQL connection prompt
        time.sleep(0.4)  #for a seamless experience
        #conn.execute("select * from cust")
        #takes values from the SQL database
        cursor = conn.cursor()
        cursor.execute("select * from cust")
        results = cursor.fetchall()
        idd = len(results)+1
        print("Registering customer with ID: ", idd)
        custname = input("Name: ")
        email = input("Customer's E-mail ID: ")
        inserter(idd, custname, email) #argumental function to insert values into the SQL database
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
        print()
        print("Loading server connection....")  #SQL connection prompt
        time.sleep(0.7) #for a seamless experience
        print("The registered customers are: ")
        #Re-writing to refresh connection
        cur = conn.cursor()
        cur.execute("SELECT * FROM cust")
        rows = cur.fetchall()
        for row in rows:
            print(row)
            print(" ")
        toaster.show_toast("DFBA Framework Runtime Broker", "Superfetch: Database acessed!", duration = 2)
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
        toaster.show_toast("DFBA Framework Runtime Broker", "Obsufcating program...", duration = 2)
        print(" ")
        print("      []         [] []               ")
        time.sleep(0.3)
        print("      []         [] []]]]]] software ")
        time.sleep(0.3)
        print("[======] [=====] [] [] [======]  CLI ")
        time.sleep(0.3)
        print("[]====[] []---[] [] [] []====[]      ")
        time.sleep(0.3)
        print("[======] []____  [] [] [======]]]]   ")
        time.sleep(0.3)
        print(" ")
        print(" ")
        time.sleep(2)
        break
        exit()
        os.close('securepack.pyw')
    elif decfac == 6:
        print("Fetching latest licensing information.......")
        print(" ")
        print(" ")
        time.sleep(1.5)
        print("      []         [] []               ")
        time.sleep(0.3)
        print("      []         [] []]]]]] software ")
        time.sleep(0.3)
        print("[======] [=====] [] [] [======]  CLI ")
        time.sleep(0.3)
        print("[]====[] []---[] [] [] []====[]      ")
        time.sleep(0.3)
        print("[======] []____  [] [] [======]]]]   ")
        time.sleep(1.5)
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
        toaster.show_toast("DFBA Framework Runtime Broker", "© 2020: DBFA by Pranav Balaji", duration = 1.5)
        print(" ")
        print(" ")
        print("Visit: www.github.com/deltaonealpha/deltaBillingFramework for complete licensing terms. ")
        print(" ")
        print(" ")
        aacsbcfac = int(input("Enter '1' to view complete licensing stuff or '2' to return."))
        if aacsbcfac == 1:
            print(" ")
            print("Please select to open with your prefered text viewer/ edittor.")
            os.startfile(r"‪C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\LICENSE")
            print(" ")
            print(" ")
            print("--------------------------------------------------")
        else:
            continue
# Program ENDS here
# Available on github: deltaonealpha.github.io/dsmsapl5
# IF YOU WANT AN UNREADABLE BYTE CODE FILE TO ENCRYPT AT BASICS THEN USE THIS:
# Use python -OO -m py_compile hms1.py with Anaconda and - 
# - rename the file in the py_cache folder by changing the extension to .py from .pyc, ultimately renaming it to hms1c.py
#
#