import os, time, sqlite3, requests, json

os.system('cls')

def telegram_bot_sendtext(bot_message):
        bot_token = '1215404401:AAEvVBwzogEhOvBaW5iSpHRbz3Tnc7fCZis'
        bot_chatID = '680917769'
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        return response.json()




print("DBFA will now open a GUI-based form for you to enter the required details.")
time.sleep(1)

import PySimpleGUI as sg

SYMBOL_UP =    '▲'
SYMBOL_DOWN =  '▼'

def collapse(layout, key):
    return sg.pin(sg.Column(layout, key=key))


section1 = [[sg.Text('Name:')],
            [sg.Input(key='-IN1-')],
            #[sg.Input(key='-IN11-')],
            [sg.Text('Gender:')],
            [sg.Checkbox('Male', key='male'), sg.Checkbox('Female', key='female'), sg.Checkbox('Others', key='othergender')],
            [sg.Text('Date of Birth:')],
            [sg.InputCombo(('Select - ', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'), size=(20, 1))],
            [sg.Text('Year:')],
            [sg.Input(key='-IN3-')],
            [sg.Text('Day:')],
            [sg.Input(key='-IN4-')]]

section2 = [[sg.Text('Email:')],
            [sg.I(k='-IN5-')],
            [sg.Text('Mobile Contact:')],
            [sg.I(k='-IN6-')],
            [sg.Text('Residential Address:')],
            [sg.I(k='-IN7-')],
            [sg.Text("Employee's UPI ID for salary payments:")],
            [sg.I(k='-IN8-')]]

section3 = [[sg.Text('Department Name:')],
            [sg.InputCombo(('Select - ', 'IT' ,'Administration', 'Sales', 'Care-taking', 'Logistics'), size=(20, 1))],
            #[sg.Input(key='-IN11-')],
            [sg.Text('Designation:')],
            [sg.Input(key='-IN8-')],
            [sg.Text('Salary:')],
            [sg.Input(key='-IN9-')]]


layout =   [[sg.Text('Hire an employee')],
            #### Section 1 part ####
            [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC1-', text_color='white'), sg.T('Personal Details', enable_events=True, text_color='yellow', k='-OPEN SEC1-TEXT')],
            [collapse(section1, '-SEC1-')],
            #### Section 2 part ####
            [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC2-', text_color='white'),
            sg.T('Personal Details', enable_events=True, text_color='white', k='-OPEN SEC2-TEXT')],
            [collapse(section2, '-SEC2-')],
            #### Buttons at bottom ####
            [sg.Button('Proceed'), sg.Button('Exit')]]
            

layout3 = [[sg.Text('Hire an employee')],
            [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC3-', text_color='white'), sg.T('Employment Details', enable_events=True, text_color='yellow', k='-OPEN SEC3-TEXT')],
            [collapse(section3, '-SEC3-')],
            [sg.Button('Complete Form >>>'), sg.Button('Exit')]]

window = sg.Window('deltaDBFA 8.2 - Add New Employee', layout)
arter = 0
opened1, opened2 = True, True

while True:             # Event Loop
    event, values = window.read()
    eventx, valuesx = event, values
    #print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event.startswith('-OPEN SEC1-'):
        opened1 = not opened1
        window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened1 else SYMBOL_UP)
        window['-SEC1-'].update(visible=opened1)

    if event.startswith('-OPEN SEC2-'):
        opened2 = not opened2
        window['-OPEN SEC2-'].update(SYMBOL_DOWN if opened2 else SYMBOL_UP)
        window['-OPEN SEC2-CHECKBOX'].update(not opened2)
        window['-SEC2-'].update(visible=opened2)
    
    if  event.startswith('Proceed'):
        axt = open(r"dbfaempre.txt", "w+")
        axt.write(str(eventx))
        axt.write(str(valuesx))
        #print(eventx, valuesx)
        global ds1
        ds1 = (eventx, valuesx)
        window.close()
        window = sg.Window('deltaDBFA 8.2 - Add New Employee', layout3)
        opened1, opened2 = True, True
        while True:             # Event Loop
            event, values = window.read()
            eventr, valuesr = event, values
            global ds2
            ds2 = (eventr, valuesr)
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
                break

            if event.startswith('Complete Form'):
                opened1 = not opened1
                arter = 1
                window.close()
                break

window.close()

if arter == 0:
    print("No data recieved! ")
if arter == 1:
    import os
    os.system('cls')
    print("Data sets recieved! ")
    ds1 = (dict(ds1[1]))
    ds2 = (dict(ds2[1]))
    print("----------------")
    print("Data from the filled form follows. These details will be sent to DBFA's data repository for safekeeping: ")

    ds1a = list(ds1.keys()) 
    ds1b = list(ds1.values()) 

    ds2a = list(ds2.keys()) 
    ds2b = list(ds2.values()) 

    #print(ds1a, ds1b, ds2a, ds2b)

    print("\n\nName          :", ds1b[0])
    print("Gender        :", ds1a[ds1b.index(True)])
    #print("DOB: (Month)  :", ds1b[4])
    monthx = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    for i in monthx:
        if i == ds1b[4]:
            month = (int(monthx.index(i))+1)
    #print(month)
    if len(str(ds1b[6])) == 1:
        day = ("0"+'%s'%ds1b[6])
    else:
        day = (ds1b[6])
    dob = str(ds1b[5])+"-"+str(month)+"-"+str(day)
    print("DOB           :", dob)
    print("EMail         :", ds1b[8])
    print("Mobile Contact:", ds1b[9])
    print("Resd. Address :", ds1b[10])
    print("UPI Payment ID:", ds1b[11])

    print("\nDepartment    :", ds2b[0])
    print("Designation   :", ds2b[1])
    print("Salary        :", ds2b[2])
    if len(str(month)) == 1:
        month = "0"+'%s'%month
        #print(month)

    import sqlite3, time

    empmas = sqlite3.connect(r'dbfaempmaster.db')
    empmascur = empmas.cursor()
    empmascur.execute("SELECT MAX(Oid) FROM emp")
    Oid = (int(empmascur.fetchall()[0][0]) + 1)
    strix = ('insert into emp(Oid, Name, DOB, Email, Mobile, Address, UPI, Dept, Post, Salary) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)')
    io = (Oid, str(ds1b[0]), str(dob), str(ds1b[8]), int(ds1b[9]), str(ds1b[10]), ds1b[11], str(ds2b[0]), str(ds2b[1]), int(ds2b[2]))
    empmascur.execute(strix, io)
    empmas.commit()
    time.sleep(2)
    print("\n\nData sets logged with DBFA..")
    empmascur.execute("SELECT * FROM emp ORDER BY Oid DESC LIMIT 0, 1")
    time.sleep(1)
    print("\n\nNEW Employee Details:: ")
    print("-----------------------------------------------------------")
    print('%s'%ds1b[0]+(30-len(str(ds1b[0])))*" "+"deltaDBFA Employee Identifier")
    print("Employee OID: ", empmascur.fetchall()[0][0])
    print("-----------------------------------------------------------\n\n")
    time.sleep(2)


    