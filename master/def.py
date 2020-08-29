import requests, time, json, urllib, os, math, random, sqlite3
from tqdm import tqdm 

def settingscommonfetch(SettingsType):
    import sqlite3
    settings = sqlite3.connect(r'dbfasettings.db')
    settingsx = settings.cursor()
    settingsx.execute(("SELECT Value from settings WHERE SettingsType = ?"), (SettingsType,))
    settingsfetch = (settingsx.fetchall()[0][0])
    return settingsfetch

if settingscommonfetch(6) == 1:
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


    os.system('cls')
    print("delta2FAAuthenicationAPI-lite")
    delsecox = getOTP()
    time.sleep(1)
    print("")
    print("As you have DBFA 2FA activated, a OTP will be sent to your Telegram account to validate this login request. ")
    for i in tqdm (range (10), desc="Generating and sending OTP"):     
        time.sleep(0.00001)    
    telegram_bot_sendtext("delta2FA Authenication Service" + "\n\n" + "A login request has been recieved to login to your DBFA installation. Entering this OTP in your DBFA installation will enable/ disable 2FA authenication aboard that installation." + "\n\n" + "Do not share this OTP with anyone. Use key: "+ '%s'%delsecox  + "\n\n" + "deltaAuthenication Service")
    time.sleep(1)
    tries = 0
    while(1):
        passkeyinput = input("Enter the validation key recieved: ")
        if tries in (0, 1, 2, 3, 4):
            if passkeyinput == delsecox:
                telegram_bot_sendtext("You have validated a DBFA 2FA login request.\n\nYou can now run your DBFA installation with all features unlocked for this session.\n\nContact support and revoke your bot login at the earliest if this wasn't you!\n\ndeltaAuthenication Service")
                tries += 1
                time.sleep(1)
                print("2FA validated.")            
                break
                break
                break
            else:
                print("Invalid validation key entered. Please retry! ")
                tries += 1
                telegram_bot_sendtext('%s'%tries+"/5: validation attempts; no valid key recieved.")
        else:
            telegram_bot_sendtext("(5) validation attempts completed, yet no valid key recieved." + "\n\n" + "2FA denied." +"\n\ndeltaAuthenication Service")
            print("(5) validation attempts completed, yet no valid key recieved. 2FA denied. ")
            print("DBFA 2FA Login request denied!! ")
            print("DBFA client is exiting! ")
            time.sleep(3)
            os._exit(0)


    os.system('cls')

else:
    print("DBFA 2FA is disabled. We recommend you to turn it on from the settings for a more secure experience with DBFA client.")