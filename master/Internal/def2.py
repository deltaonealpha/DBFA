#################################################
# deltaDBFA Internal Testing Build              #
#                                               #
# Test subject: Scheduler and Leave Application #
# Broad category: DBFA Employee Manager         #
#                                               #
# Author: @deltaonealpha                        #
#################################################

# The future of dbfa (will take a LONG time to code :D)
# Automatic employee shift scheduling with an option to apply for leaves.

#delta           █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ ▀
#Scheduler       █   0600 - 1400   █   1400 - 2200   █   2200 - 0600   █ ▀
#▀▀▀▀▀▀▀▀▀       █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ ▀
#SALES           █                 █                 █                 █ ▀
#                █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ ▀
#MAINTANENCE     █                 █                 █ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ █ ▀
#                █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ ▀
#LOGISTICS       █                 █ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ █                 █ ▀
#                ███████████████████████████████████████████████████████ ▀

# Todo now
# Generate, send email, send tg and update db IF NOT UPDATED IN DB YET
        # Add apply for leave/ see regen option

import sqlite3, time, random, requests
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
        bot_token = '1215404401:AAEvVBwzogEhOvBaW5iSpHRbz3Tnc7fCZis'
        bot_chatID = '680917769'
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

    telegram_bot_sendtext(bot_message.replace("&", "and"))
    time.sleep(2)
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