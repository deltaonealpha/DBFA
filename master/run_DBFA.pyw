from datetime import datetime
import sqlite3, time, os

if os.path.exists(r'userblock.txt'):
    os.remove(r'userblock.txt')
if os.path.exists(r'userblock.zconf'):
    os.remove(r'userblock.zconf')

def OAuthset():
    now = datetime.now()
    try: #To avoid error when time is 00:00:00
        netr = int(now.strftime("%H"))*3600 + int(now.strftime("%M"))*60 + int(now.strftime("%S"))
    except:
        time.sleep(1)
        netr = int(now.strftime("%H"))*3600 + int(now.strftime("%M"))*60 + int(now.strftime("%S"))
    oauth = sqlite3.connect(r'dbfasettings.db')
    oauthx = oauth.cursor()

    oauthx.execute("SELECT count(*) FROM LoginHandler")
    rows = oauthx.fetchall()
    if (rows[0][0]) > 1:
        print("DBFA Authenticator has been tampered with! DBFA WILL EXIT NOW!")
        time.sleep(2)
        os._exit(0)
    oauthx.execute("SELECT OAuthID FROM LoginHandler")
    try: #To avoid error when there's no data in the table
        maxid = int(oauthx.fetchall()[0][0]) + 1
    except:
        maxid = 1
        oauthx.execute("insert into LoginHandler(OAuthID, Value, TimeMark) values(?, 1, ?)", (maxid, netr))
    oauthx.execute("UPDATE LoginHandler SET OAuthID = ?, Value = 1, TimeMark = ?", (maxid, netr))
    print("Login session dtalgnrt", netr, "-", maxid)
    oauth.commit()
    oauth.close()

def Login():
    creds = r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\tempfile.temp'
    with open(creds, 'r') as f:
        data = f.readlines() # This takes the entire document we put the info into and puts it into the data variable
        uname = data[0].rstrip() # Data[0], 0 is the first line, 1 is the second and so on.
        pword = data[1].rstrip() # Using .rstrip() will remove the \n (new line) word from before when we input it
        import PySimpleGUI as sgx
        sgx.theme('DarkTeal9')	# Add a touch of color
        # All the stuff inside your window.
        def CAPSLOCK_STATE():
            import ctypes
            hllDll = ctypes.WinDLL ("User32.dll")
            VK_CAPITAL = 0x14
            return hllDll.GetKeyState(VK_CAPITAL)

        CAPSLOCK = CAPSLOCK_STATE()

        if ((CAPSLOCK) & 0xffff) != 0:
            #print("\nWARNING:  CAPS LOCK IS ENABLED!\n")
            layout = [  [sgx.Text('Yo we know security...')],
                        [sgx.Text('Username: '), sgx.InputText()],
                        [sgx.Text('Password: '), sgx.InputText(password_char='*')],
                        [sgx.Button('Login'), sgx.Button('Cancel')], 
                        [sgx.Text('WARNING:  CAPS LOCK IS ENABLED!')]]
        
        else:
            layout = [  [sgx.Text('Yo we know security...')],
                        [sgx.Text('Username: '), sgx.InputText()],
                        [sgx.Text('Password: '), sgx.InputText(password_char='*')],
                        [sgx.Button('Login'), sgx.Button('Cancel')]]
        # Create the Window
        window = sgx.Window('DNSS Authenication Service', layout)
        # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):	# if user closes window or clicks cancel
            window.close
            break
        window.close()
        window.close()
        if values[0] == 'ed' and values[1] == 'edd':
            #os.close(r'DDD.py')
            window.close()
            userblock = open(r"userblock.txt","a+") #Opening / creating (if it doesn't exist already) the .txt record file
            userblock.write('ed')
            #time.sleep(2)
            OAuthset()
            userblock.close()
            print("logging success")
            os.startfile('bleading_edge.py')
            window.close()
            window.close()
            exit
            exit
            exit
            break
        else:
            os.startfile(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\wrelogin.pyw')
        #window.close
        #erraise()
import PySimpleGUI as sg
if os.path.exists(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\userblock.txt'):
    os.remove(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\userblock.txt')
if os.path.exists(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\userblock.zconf'):
    os.remove(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\userblock.zconf')
sg.theme('DarkTeal9')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text("DBFA Security")],
            [sg.Text("This program requires you to login.")],
            [sg.Button('Login'), sg.Button('Exit')] ]
# Create the Window
window = sg.Window('DBFA', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Exit'):	# if user closes window or clicks cancel
        break
    window.close()
    Login()
