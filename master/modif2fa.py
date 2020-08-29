import requests, time, json, urllib, os, math, random, sqlite3
from tqdm import tqdm 
import PySimpleGUI as sgx



def settingscommonfetch(SettingsType):
    import sqlite3
    settings = sqlite3.connect(r'dbfasettings.db')
    settingsx = settings.cursor()
    settingsx.execute(("SELECT Value from settings WHERE SettingsType = ?"), (SettingsType,))
    settingsfetch = (settingsx.fetchall()[0][0])
    return settingsfetch

def settingsmodifier(SettingsType, NewValue):
    import sqlite3
    settings = sqlite3.connect(r'dbfasettings.db')
    settingsx = settings.cursor()
    settingsx.execute(("UPDATE settings SET Value = ? WHERE SettingsType = ?"), (NewValue, SettingsType))
    settings.commit()




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


def telegram_bot_sendtext(bot_message):
    bot_token = '1215404401:AAEvVBwzogEhOvBaW5iSpHRbz3Tnc7fCZis'
    bot_chatID = '680917769'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

def getOTP():
    digits = "0123456789"
    otp = ""
    otp += (digits[math.floor(random.random() * 10)])
    otp += (digits[math.floor(random.random() * 10)])
    otp += (digits[math.floor(random.random() * 10)])
    otp += (digits[math.floor(random.random() * 10)])
    otp += (digits[math.floor(random.random() * 10)])
    otp += (digits[math.floor(random.random() * 10)])
    return otp


def Login():
    layout = [  [sgx.Text('Login to authenicate: ')],
                [sgx.Text('Username: '), sgx.InputText()],
                [sgx.Text('Password: '), sgx.InputText(password_char='*')],
                [sgx.Button('Authenicate'), sgx.Button('Cancel')] ]
    window = sgx.Window('deltaAuthenication Service', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):	# if user closes window or clicks cancel
            print("DBFA 2FA Modification cancelled!! ")
            time.sleep(5)            
            window.close
            os._exit(0)
            window.close()
            window.close()
            os._exit(1)
        if values[0] == 'ed' and values[1] == 'edd':
            window.close
            window.close
            print("delta2FAAuthenicationAPI-lite")
            print("As you're accessing sensitive information, this request needs to be validated.")
            time.sleep(2)
            print("")
            print("A one-time-password (OTP) has been sent to your Telegram account to validate this request")
            time.sleep(0.5)
            for i in tqdm (range (10), desc="Generating and sending OTP"):     
                time.sleep(0.00001)    
            texter = "delta2FA Authenication Service" + "\n\n" + "A login request has been recieved from your DBFA installation. Entering this OTP in your DBFA installation will enable/ disable 2FA authenication aboard that installation." + "\n\n" + "Do not share this OTP with anyone. Use key: "+ '%s'%delsecox  + "\n\n" + "deltaAuthenication Service"
            sender = telegram_bot_sendtext(texter)
            window.close
            window.close
            mainprocess()

        else:
            sgx.theme('DarkRed')
            Login()

def mainprocess():
    time.sleep(1)
    tries = 0
    while(1):
        passkeyinput = input("Enter the validation key recieved: ")
        if tries in (0, 1, 2, 3, 4):
            if passkeyinput == delsecox:
                telegram_bot_sendtext("You have validated a DBFA 2FA login request.\n\nThis allows your installation of DBFA and the data it stores, to be used.\n\nContact support and revoke your bot login at the earliest if this wasn't you!\n\ndeltaAuthenication Service")
                tries += 1
                time.sleep(1)
                from colorama import init, Fore, Back, Style
                print("\n\nEnable DBFA two-factor-authenication? ")
                print("y:    ",  '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|')
                settfac1x = input(("n:     "+ '|'+Fore.RED+'████'+Fore.WHITE+' OFF|: '))
                if settfac1x == "y":
                    if (settingscommonfetch(6)) != 1:
                        settingsmodifier(6, 1)
                        transitionprogress()
                        time.sleep(3)
                        print("Please wait while we restart DBFA main client")
                        os.startfile('bleading_edge.py')
                        time.sleep(1)
                        os._exit(0)
                    else:
                        print("DBFA 2FA is already enabled!")
                        time.sleep(3)
                        print("Please wait while we restart DBFA main client")
                        os.startfile('bleading_edge.py')
                        time.sleep(1)
                        os._exit(0)

                if settfac1x == "n":
                    if (settingscommonfetch(6)) != 0:
                        settingsmodifier(6, 0)
                        transitionprogressneg()
                        time.sleep(3)
                        print("Please wait while we restart DBFA main client")
                        os.startfile('bleading_edge.py')
                        time.sleep(1)
                        os._exit(0)
                    else:
                        print("DBFA 2FA is already enabled!")
                        time.sleep(3)
                        print("Please wait while we restart DBFA main client")
                        os.startfile('bleading_edge.py')
                        time.sleep(1)
                        os._exit(0)

            else:
                print("Invalid validation key entered. Please retry! ")
                tries += 1
                telegram_bot_sendtext('%s'%tries+"/5: validation attempts; no valid key recieved.")
        else:
            telegram_bot_sendtext("(5) validation attempts completed, yet no valid key recieved." + "\n\n" + "2FA denied." +"\n\ndeltaAuthenication Service")
            print("(5) validation attempts completed, yet no valid key recieved. 2FA denied. ")
            print("DBFA 2FA Modification cancelled!! ")
            time.sleep(5)
            break

delsecox = getOTP()
Login()