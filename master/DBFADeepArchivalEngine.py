#Data Format: <order ids>///<customer name>///<customer id>///<date and time string>///tax///discount///loyalty///net

# DD/MM/YYYY_HH/MM/SS
# DD000MM000YYYY000HH000MM000SS

import time
def alphadecoder(datalist):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    out = ""
    for i in (datalist):
        if i.isnumeric():
            print(i, int(i)-1)
            out += alpha[(int(i)-1)]
    del alpha
    return(out)

def dttdecoder(datalist):
    templist1 = datalist.split('y')
    out = templist1[0] + '/'
    print(templist1[0])
    out += templist1[1] + '/'
    print(templist1[1])
    out += templist1[2] + ' '
    print(templist1[2])
    out += templist1[3] + ':'
    print(templist1[3])
    out += templist1[4] + ':'
    out += templist1[5]
    print(templist1[5])
    print(templist1[3])
    return(out)

def encoder_deeparchival(data, invid):
    deeparchival_input = data
    orders, cust_name, cust_id, dt_string = deeparchival_input[0], deeparchival_input[1], deeparchival_input[2], deeparchival_input[3]
    tax_bar, disct_bar, lylredemp, net_process = deeparchival_input[4], deeparchival_input[5], deeparchival_input[6], deeparchival_input[7]
    templist = (dt_string.split(" "))
    templist2 = templist[0].split('/')
    xdatetime = templist2[0] + 'y' + templist2[1] + 'y' + templist2[2] + 'y'
    templist3 = templist[1].split(':')
    xdatetime += templist3[0] + 'y' + templist3[1] + 'y' + templist3[2] + 'y'
    dt_string = xdatetime

    ordernet = orders.split('.')

    deeparchival_key = ""
    for i in ordernet:
        deeparchival_key += str(i)+"00"
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    out = ""
    for i in str(cust_name):
        if i.isalpha():
            out += str((alpha.index(i.lower())) + 1) + 'z'
        else:
            out += str(i) + 'z'
    deeparchival_key += ("000" + out + "00000" + str(cust_id) + "00000" + str(dt_string))
    deeparchival_key += ("00000" + str(tax_bar) + "00000" + str(disct_bar) + "00000" + str(lylredemp) + "00000" + str(net_process))
    import os, sqlite3
    from datetime import datetime
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")  #datetime object containing current date and time
    time_string = now.strftime("%H:%M:%S")  #datetime object containing current date and time
    dde = sqlite3.connect(r'DeepArchivalVault.db')
    ddex = dde.cursor()
    ddex.execute("INSERT INTO archive(Invid, Date, Time, Key) VALUES (?, ?, ?, ?)", (invid, dt_string, time_string, deeparchival_key))
    dde.commit()
    print("Data stored to VAULT.")
    return deeparchival_key


def decoder_deeparchival(key):
    print(key)
    if((key is None) or (len(key) == 0)):
        print("deeparchival-error:key-none?")
    else:
        print(key)
        init_data = key.split("00000")
    if init_data is not None:
        print('Decoding')
    else:
        exit
    print('rrtt', init_data)
    orders, cust_name, cust_id, dt_string = init_data[0], init_data[1], init_data[2], init_data[3]
    tax_bar, disct_bar, lylredemp, net_process = init_data[4], init_data[5], init_data[6], init_data[7]

    ordernet = str(orders).split('00')
    print(cust_name)
    if disct_bar in (None, "", " "):
        disct_bar = '0'
    dt_string = dttdecoder(dt_string)
    cust_name = alphadecoder(cust_name.split('z'))
    out = []
    xttemp = ""
    for i in ordernet:
        xttemp += (str(i) + '.')
    xttemp = xttemp[:-1]
    print('rrtt', lylredemp)
    if str(lylredemp) in ('0', 0):
        lylredemp = (str(lylredemp[1:]))
    import os
    os.system('cls')
    return (xttemp, cust_name, cust_id, dt_string, tax_bar, disct_bar, lylredemp, net_process)

def deepfetch_deeparchival():
    import sqlite3, os
    from sqlite3 import Error
    import os, time
    from datetime import datetime  #for reporting the billing time and date
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

    dde = sqlite3.connect(r'DeepArchivalVault.db')
    ddex = dde.cursor()
    print("Starting deep archival fetch process ----\n")
    ddex.execute("SELECT * FROM archive GROUP BY Date")
    datastream = ddex.fetchall()
    
    from tabulate import tabulate
   
    print(r'''  █▀▀█ █▀█  █▀▀ █▀█  █▀▀█   █▀▀█ █▀▀ █▀▀ █▀▀█   █▀▀█ █▀▀█ █▀▀ █ █ █ ▀   ▀ █▀▀█ █     █▀▀ ██ █ █▀▀▀ █ ██ █ █▀▀
    █__█ █▀▀█ █▀  █▬█  ▄▄▄▄   █__█ ███ ███ █▀▀▀   █  █ █▀█= █__ █▀█ █  ▀_▀  █  █ █__   ███ █ ▀█ █_▀█ █ █ ▀█ ███''')
    print(tabulate(datastream, headers=['Inv. ID', 'Date', 'Time', 'Key'], tablefmt='orgtbl'))
    inputmaster = input("\nEnter the invoice ID to fetch from the VAULT: ")
    print("Fetching details for invoice ID: ", inputmaster, "from the VAULT.")
    inputmaster = '%'+inputmaster+'%'
    ddex.execute("SELECT Key FROM archive WHERE Invid LIKE ?", (inputmaster, ))
    row = ddex.fetchall()
    if row in (None, [], [[]], [()], "", " "):
        print("Invalid invoice ID.")
    else:
        ddex.execute("SELECT Invid FROM archive WHERE Key = ?", (row[0][0], ))
        xkeyer = ddex.fetchall()[0][0]
        #delta DEEP Archival System Decoder
        from DBFADeepArchivalEngine import alphadecoder, dttdecoder, decoder_deeparchival
        temp, cust_name, cust_id, dt_string, tax_bar, disct_bar, lylredemp, net_process = decoder_deeparchival(row[0][0])
        print(temp, cust_name, cust_id, dt_string, tax_bar, disct_bar, lylredemp, net_process)
        namiex = ["TV 4K OLED 50", "TV FHD OLED 50", "8K QLED 80", "Redmi K20 PRO", "Redmi K20", "Redmi Note 9 PRO", "POCOPHONE F1", "Mi MIX ALPHA", "Wireless Headphones", "Noise-Cancelling Wireless Headphones", "Essentials Headphones", "Gaming Headphones", "Truly-Wireless Eadphones", "Neckband-Style Wireless Earphones", "Essentials Earphones", "Gaming Earphones", "30W Bluetooth Speakers", "20W Bluetooth Speakers", "Essentials Bluetooth Speaker", "BOSE QC35", "Essentials Home Theatre", "Wired Speaker - 5.1", "Essentials Wired Speaker - STEREO", "Tactical Series Power Bank 30000mah", "Essentials Power Bank 10000mah", "Essentials Mouse", "Logitech G604 LightSpeed Wireless", "Tactical Essentials Keyboard", "DROP GS21k RGB Gaming Keyboard", "Polowski Tactical Flashlight", "OneFiber Wi-Fi Router AX7", "Mijia Mesh Wi-Fi Router", "lapcare 45W Laptop Adapter", "lapcare 60W Laptop Adapter","Spigen Phone Case(s)", "Essentials Phone Charger 15W", "HyperPower Type-C Gallium-Nitride Charger 120W", "ASUS Zephyrus G4 Gaming Laptop", "DELL XPS 5 Content Creator's Laptop", "Hewlett-Packard Essential's Student's Laptop (Chromebook)"]
        datax = [40000, 55000, 67000, 25000, 21000, 14000, 3000, 220000, 4500, 17000, 1200, 3700, 4500, 2200, 700, 2750, 6499, 1499, 799, 27000, 6750, 2100, 1199, 3210, 989, 750, 1700, 600, 2175, 890, 2100, 7158, 597, 347, 500, 300, 1097, 80000, 87900, 23790]
        writer = ("~DBFA DEEP ARCHIVAL VAULT~\n\nDBFA Billing Framework\nOne-stop solution for all your billing needs!\n\nBilling time:" + str(dt_string) + "\nCustomer ID: " + str(cust_id) + str(cust_name) + "\n-----------------------------Invoice ID:" + str(xkeyer) + "\nPurchased: ")
        orders = temp.split('.')
        #print(temp, orders)
        for i in orders:
            writer += str(str(namiex[int(i)-1]) + '\n')
            writer += str(str(datax[int(i)-1]) + '\n\n')
        writer += ("-----------------------------\nTax amount: " + str(tax_bar)+'%' + "\nDiscount: " + str(disct_bar) + "\nUsed DBFA loyalty points worth:" + str(lylredemp)  + "\nNET TOTAL:" + str(net_process))        
        from datetime import datetime
        import datetime
        daterey = (dt_string.replace("/","")).replace(":", "")
        namer = 'DBFAinvid'+'%s'%xkeyer+"-"+daterey+'.pdf'
        can = SimpleDocTemplate(namer, pagesize=A4,
                                rightMargin=2*cm,leftMargin=2*cm,
                                topMargin=2*cm,bottomMargin=2*cm)
        #can.setFont("MiLanProVF", 24)
        can.build([Paragraph(writer.replace("\n", "<br />"), getSampleStyleSheet()['Normal']),])

        import shutil
        source = namer
        temp = str(r"C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\Generated_invoices\\ ")[:-1] + str(namer)
        dest = shutil.move(source, temp)  
        os.startfile(temp)
        del temp
        print("DEEP ARCHIVAL VAULT: Invoice generated and moved to the 'Generated Invoices' directory ~ ")

