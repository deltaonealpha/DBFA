#################################################
# deltaDBFA Internal Testing Build              #
#                                               #
# Test subject: Automated Salary Calculation    #
# Broad category: DBFA Employee Manager         #
#                                               #
# Author: @deltaonealpha                        #
#################################################

# The future of dbfa (will take a LONG time to code :D)
# Automated salary amount calculation using weekly hours worked (on top of minimum amount)
#3 cashiers 8 hour shifts each
#9 general workers 8 hour shifts each
#2 maintanence crew 8 hour shifts each
#
#Fetch net hours per day
#Make that per week (get all and avg/ sum)
#Fetch weekly limit and subtract
#Schedule now
#Send weekly schedule emails to employees (needs extensive db usage to store sending statuses)
#need a leave management way
#
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
    font = ImageFont.truetype(r'C:\Users\balaj\AppData\Local\Microsoft\Windows\Fonts\MiLanProVF.ttf', size=200)
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

    os.system(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\payqr.png')

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
