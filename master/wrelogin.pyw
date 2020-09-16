from datetime import datetime
import sqlite3, time, os

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

if os.path.exists(r'userblock.txt'):
    os.remove(r'userblock.txt')
if os.path.exists(r'userblock.zconf'):
    os.remove(r'userblock.zconf')
def Login():
    import PySimpleGUI as sgx
    sgx.theme('DarkRed')
    def CAPSLOCK_STATE():
        import ctypes
        hllDll = ctypes.WinDLL ("User32.dll")
        VK_CAPITAL = 0x14
        return hllDll.GetKeyState(VK_CAPITAL)

    CAPSLOCK = CAPSLOCK_STATE()

    if ((CAPSLOCK) & 0xffff) != 0:
        #print("\nWARNING:  CAPS LOCK IS ENABLED!\n")
        layout = [  [sgx.Text('INVALID LOGIN. Please retry:')],
                    [sgx.Text('Username: '), sgx.InputText()],
                    [sgx.Text('Password: '), sgx.InputText(password_char='*')],
                    [sgx.Button('Authenicate'), sgx.Button('Cancel')],
                    [sgx.Text('WARNING:  CAPS LOCK IS ENABLED!')]]
    
    else:
        layout = [  [sgx.Text('INVALID LOGIN. Please retry:')],
                    [sgx.Text('Username: '), sgx.InputText()],
                    [sgx.Text('Password: '), sgx.InputText(password_char='*')],
                    [sgx.Button('Authenicate'), sgx.Button('Cancel')] ]

    window = sgx.Window('deltaAuthenication Service', layout)
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
            os.startfile("wrelogin.pyw")
            exit
        #window.close
        #erraise()
import PySimpleGUI as sg
if os.path.exists(r'userblock.txt'):
    os.remove(r'userblock.txt')
if os.path.exists(r'userblock.zconf'):
    os.remove(r'userblock.zconf')

Login()
