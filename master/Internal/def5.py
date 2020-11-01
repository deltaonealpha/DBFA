#if str(settingscommondumpfetch(10)) == "Administrator":
import time, os, requests

def settingscommonfetch(SettingsType):
    import sqlite3
    settings = sqlite3.connect(r'dbfasettings.db')
    settingsx = settings.cursor()
    settingsx.execute(("SELECT Value from settings WHERE SettingsType = ?"), (SettingsType,))
    settingsfetch = (settingsx.fetchall()[0][0])
    return settingsfetch

currdir = str(os.getcwd())
from pathlib import Path
path = Path(os.getcwd())
parentdir = str(Path(path.parent))
#print(parentdir)
#print(parentdir+'\\updates.txt')
userdir = os.path.expanduser('~')
url = "https://raw.githubusercontent.com/deltaonealpha/DBFA_UpdateHandler/master/updates.txt"
try:
    r = requests.get(url)
    dbfaver = ((str(r.content.decode('utf-8'))))[4:]
    xdbfaver = ((str(r.content.decode('utf-8'))))
    with open(parentdir+'\\updates.txt', 'r+') as upread:
        upread = (str(upread.read())).strip()
    spass1 = []
    spass2 = []
    for i in dbfaver:
        spass1.append(i)
    for j in upread[4: ]:
        spass2.append(j)
    if float(upread[4: ]) > float(dbfaver):
        pass
    else:
        if xdbfaver == upread:
            uptd = 1
        elif spass1 != spass2:
            uptd = 2
    netcon = 1    
except (requests.ConnectionError, requests.Timeout) as exception:
    netcon = 0


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

os.system('cls')
from colorama import init, Fore, Back, Style #color-settings
print(Fore.RED+"DBFA Security Options are designed to execute functions which may render your DBFA installation completely unusable/ delete all data/ crash. Proceed with caution.")
time.sleep(3)
os.system('cls')
init(convert = True)
print(Fore.WHITE+'''
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
DBFA Security Dashboard                                           deltasoftware
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
'''+Fore.RED+'''Administrator Access Granted
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬'''+Fore.WHITE)
if netcon == 1:
    if uptd == 1:
        print(Fore.GREEN+'''
  █▀▀▀▀▀▀█              
█▀        ▀█            Security Status  : DBFA is up-to-date ~ 
█        ▄ █            File Integrity   : Acceptable
█      ▄▀  █            Storage Integrity: Strong
 █ █▄▄▀   █             Webhook Health   : Strong (INTERNET CONNECTED)
  ██    ██              
   ▀▀▀▀▀▀'''+Fore.WHITE)
    else:
            print(Fore.RED+'''
  █▀▀▀▀▀▀█              
█▀  ▄   ▄ ▀█            Security Status  : DBFA is running on an OUTDATED build!
█    ▀▄▀   █            File Integrity   : Acceptable
█   ▄▀ ▀▄  █            Storage Integrity: Strong
 █        █             Webhook Health   : Strong (INTERNET CONNECTED)
  ██    ██              
   ▀▀▀▀▀▀'''+Fore.WHITE)
elif netcon == 0:
    print(Fore.RED+'''
  █▀▀▀▀▀▀█              
█▀  ▄   ▄ ▀█            Security Status  : Connection to server unavailable!
█    ▀▄▀   █            File Integrity   : Acceptable
█   ▄▀ ▀▄  █            Storage Integrity: Strong
 █        █             Webhook Health   : DISCONNECTED (NO INTERNET)
  ██    ██              
   ▀▀▀▀▀▀'''+Fore.WHITE)
print(Fore.WHITE+'''
a - '''+Fore.RED+'''DELETE ALL'''+Fore.WHITE+' customer records                      :'+Fore.WHITE, '|'+Fore.RED+"██ Proceed > "+Fore.RED+'''|'''+Fore.WHITE+'''
b - '''+Fore.RED+'''DELETE ALL'''+Fore.WHITE+' store records                         :'+Fore.WHITE, '|'+Fore.RED+"██ Proceed > | "+Fore.WHITE)
print('''
c - Change '''+Fore.RED+'''ADMINISTRATOR'''+Fore.WHITE+''' password 
d - Change password for employee accounts >>\n''')
#if (settingscommonfetch(5)) == 0:
print(Fore.MAGENTA+"e - Enable database encryption                       : UNDER DEVELOPMENT "+Fore.WHITE+'      ')
#else:
    #print("e - Enable database encryption                       :", (Fore.RED+'|████'+Fore.RED+' OFF|      '+Fore.WHITE))
if (settingscommonfetch(6)) == 1:
    print(Fore.WHITE+"f - Enable DBFA Secure Two-Factor-Authenication      :", Fore.GREEN+'| ON '+Fore.GREEN+'████|'+Fore.WHITE+'      ')
else:
    print(Fore.WHITE+"f - Enable DBFA Secure Two-Factor-Authenication      :", (Fore.RED+'|████'+Fore.RED+' OFF|      '+Fore.WHITE))

print('''\ng - <<< Return to main menu
'''+Fore.RED+'''▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬''')
dsoa = input("What would you like to do?: "+Fore.WHITE)
if dsoa in ("a", "A"):
    print('''This option PERMANENTLY CLEARS ALL DBFA CUSTOMER RECORDS.
This includes their registration data, purchase records, and loyalty points.
This execution can NOT BE REVERSED.
DATA INTEGRITY MAY BE LOST during this process.
Proceed with caution! ''')
    print(" ")
    print("Confirm operation - DELETE all customer records? ")
    print("y:    ",  '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|')
    settfac1x = input(("n:     "+ '|'+Fore.RED+'████'+Fore.WHITE+' OFF|: '))
    if settfac1x == "y":
        print("DBFA will now reboot itself to finish applying changes.")
        time.sleep(0.5)
        transitionprogress()
        # window.close()
        os.startfile(r'securepack.py')
        time.sleep(0.5)
        os._exit(0)
    elif settfac1x == "n":
        print("Cancelled ~")
    else:
        print("That's an invalid input... ")
        
if dsoa in ("b", "B"):
    print('''This option PERMANENTLY CLEARS ALL DBFA VOUCHERS/ COUPONS
All current vouchers/ coupons WILL BE LOST.
Vouchers already issued will become redundant unless manually re-added again.
Validity and usage limits will be lost for all voucher/ coupon instanced recorded by DBFA.

However, DBFA's logged voucher/ coupon usage will continue to exist in memory and will not be erased.

This execution can NOT BE REVERSED.
DATA INTEGRITY MAY BE LOST during this process.
Proceed with caution! ''')
    print(" ")
    print("Confirm operation - DELETE all store records? ")
    print("y:    ",  '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|')
    settfac1x = input(("n:     "+ '|'+Fore.RED+'████'+Fore.WHITE+' OFF|: '))
    if settfac1x == "y":
        print("DBFA will now reboot itself to finish applying changes.")
        time.sleep(0.5)
        transitionprogress()
        # window.close()
        os.startfile(r'securepackxvc.py')
        time.sleep(0.5)
        os._exit(0)
    elif settfac1x == "n":
        print("Cancelled ~")
    else:
        print("That's an invalid input... ")

    print()
if dsoa in ("c", "C"):
    print("Option under development! ")
if dsoa in ("d", "D"):
    print("Option under development! ")
if dsoa in ("e", "E"):
    print('''In our process of phasing-out .txt based storage in favour of sqlite storage, 
we at DBFA are trying to make our files even tougher to access than ever before without valid credentials.

DBFA is currently experimenting with sqlcipher encryption for it's sqlite databases.
Please note that this functionality is a part of DBFA internal test builds for now,
and is not ready for public rollout.

This process might impact DBFA's data integrity. We recommend you to run *DBFA Backup&Switch* from option *5*
before you attempt to encrypt/ decrypt DBFA databases by running this command.\n''')

if dsoa in ("f", "F"):
    print("----DBFA 2FA MANAGER----")
    print("DBFA allows you to use 2FA to safeguard your account if your password gets compromised.\n")
    print("Please do note that enabling/ disabling 2FA will reboot DBFA Store Manager!~\n")
    import os
    print(Fore.WHITE+"Connecting to your delta account. . ."+Fore.WHITE)
    time.sleep(2)
    print("Changing 2FA settings requires 2FA to proceed: ")
    time.sleep(1)
    os.startfile('modif2fa.py')
    time.sleep(0.5)
    os._exit(0)

