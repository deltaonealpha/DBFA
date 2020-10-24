# ---------------------------------------------- #
# DBFA First Time Automatic Setup                #
# deltasystems deltasoftware DBFA Client Manager #
# Licensed under the GNUAPL License              #
# ---------------------------------------------- #

import sqlite3, os, time, sys
os.system('cls')
time.sleep(1)

global curdir, parentdir, fontsdir
currdir = str(os.getcwd())
file_path = currdir+'\\initsetup.zip'

def mover():
    from tqdm import tqdm
    import shutil, os, time, sys
    slave = currdir
    for i in tqdm (range (100), desc="Restoring Databases                       "): 
        master = currdir+'\\TempRestoration\\DBFATempc\\DBFA_vend.db'
        shutil.copy(master, slave)
        master = currdir+'\\TempRestoration\\DBFATempc\\cponmgmtsys.db'
        shutil.copy(master, slave)
        master = currdir+'\\TempRestoration\\DBFATempc\\DBFA.db'
        shutil.copy(master, slave)
        master = currdir+'\\TempRestoration\\DBFATempc\\DBFA_CUSTCC.db'
        shutil.copy(master, slave)
        master = currdir+'\\TempRestoration\\DBFATempc\\DBFA_handler.db'
        shutil.copy(master, slave)
        master = currdir+'\\TempRestoration\\DBFATempc\\recmaster.db'
        shutil.copy(master, slave)
        time.sleep(0.0000000001)
        master = currdir+'\\TempRestoration\\DBFATempc\\invoicemaster.db'
        shutil.copy(master, slave)
        master = currdir+'\\TempRestoration\\DBFATempc\\dbfaempmaster.db'
        shutil.copy(master, slave)
        master = currdir+'\\TempRestoration\\DBFATempc\\dbfasales.db'
        shutil.copy(master, slave)
        master = currdir+'\\TempRestoration\\DBFATempc\\dbfasettings.db'
        if os.path.exists(currdir+'\\delauth.txt'):
            os.remove(currdir+'\\delauth.txt')
        shutil.copy(master, slave)
        master = currdir+'\\TempRestoration\\DBFATempc\\DeepArchivalVault.db'
        shutil.copy(master, slave)
        master = currdir+'\\TempRestoration\\DBFATempc\\recmaster.db'
        shutil.copy(master, slave)

    for i in tqdm (range (100), desc="Restoring Session Keys                    "): 
        master = currdir+'\\TempRestoration\\DBFATempc\\backupconfig.txt'
        shutil.copy(master, slave)
        master = currdir+'\\TempRestoration\\DBFATempc\\lastupdateid.txt'
        shutil.copy(master, slave)
        master = currdir+'\\TempRestoration\\DBFATempc\\lastupdateid2.txt'
        shutil.copy(master, slave)
        if os.path.exists(currdir+'\\delauth.txt'):
            os.remove(currdir+'\\delauth.txt')
        master = currdir+'\\TempRestoration\\DBFATempc\\lastsched.txt'
        shutil.copy(master, slave)
        time.sleep(0.0000000001)

    for i in tqdm (range (100), desc="Restoring Authorization Keys              "): 
        master = currdir+'\\TempRestoration\\DBFATempc\\tempfile.temp'
        shutil.copy(master, slave)
        if os.path.exists(currdir+'\\delauth.txt'):
            os.remove(currdir+'\\delauth.txt')
        master = currdir+'\\TempRestoration\\DBFATempc\\client_secrets.json'
        shutil.copy(master, slave)
        time.sleep(0.0000000001)

    for i in tqdm (range (100), desc="Restoring Payment Keys                    "): 
        master = currdir+'\\TempRestoration\\DBFATempc\\DBFAdeliveries.txt'
        shutil.copy(master, slave)
        master = currdir+'\\TempRestoration\\DBFATempc\\payqr.png'
        if os.path.exists(currdir+'\\delauth.txt'):
            os.remove(currdir+'\\delauth.txt')
        shutil.copy(master, slave)
        time.sleep(0.0000000001)

    for i in tqdm (range (100), desc="Restoring Registery & Logs Files          "): 
        master = currdir+'\\TempRestoration\\DBFATempc\\log.txt'
        shutil.copy(master, slave)
        master = currdir+'\\TempRestoration\\DBFATempc\\devclog.txt'
        if os.path.exists(currdir+'\\delauth.txt'):
            os.remove(currdir+'\\delauth.txt')
        shutil.copy(master, slave)
        master = currdir+'\\TempRestoration\\DBFATempc\\registry.txt'
        shutil.copy(master, slave)
        time.sleep(0.0000000001)
        time.sleep(0.0000000001)
    if os.path.exists(currdir+'\\TempRestoration'):
        shutil.rmtree(currdir+'\\TempRestoration', ignore_errors=True)
    print("DBFA Backup Restoration Completed! ~")
    os.startfile(currdir+'\\run_DBFA.pyw')

import os, shutil, time
if os.path.exists(currdir+'\\TempRestoration'):
        shutil.rmtree(currdir+'\\TempRestoration', ignore_errors=True)
os.makedirs(currdir+'\\TempRestoration', mode = 0o777)
import zipfile
with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(currdir+'\\TempRestoration')

print('''-----------------------------------------
| DBFA Initialization Package detected! |
-----------------------------------------''')
print("Getting ready to initialize DBFA Manager ~")
time.sleep(2)
mover()
print("DBFA files loaded succesfully ~")
time.sleep(2)

print('''██▀▀ ██  ██▀▀▀██   ██▀▀▀▀  ██▀▀▀██  ██▀▀▀▀██ 
██   ██  ██   ██   ██      ██   ██  ██    ██ CLI
██   ██  ██▀▀▀▀██  ██▀▀    ██▬▬▬██           Store
██___██  ██    ██  ██      ██   ██  ████████ Manager

DBFA First-Time Setup Wizard
(WARNING: DO NOT SKIP THIS!)''')
time.sleep(1)

def settingsmodifier(SettingsType, NewValue):
    import sqlite3
    settings = sqlite3.connect(r'dbfasettings.db')
    settingsx = settings.cursor()
    settingsx.execute(("UPDATE passkeyhandler SET Col1 = ? WHERE Sno = ?"), (NewValue, SettingsType))
    settings.commit()


time.sleep(1)
print("Welcome to DBFA, the most feature packed* open-source store manager out there!")
time.sleep(1)
print("With DBFA, we at deltasoftware aim to provide a smooth and open source experience with a focus on security, packaged along with some quirky features!")
time.sleep(1)
print("\nThis setup will guide you through getting some user-dependant settings ready for you to use DBFA.")
time.sleep(1)
print("Loading setup...")
time.sleep(5)
os.system('cls')
print("DBFA emails customers their invoice and OTPs for loyalty point usage. For this, we will need you to create a special *but free* email account.")
time.sleep(1)
time.sleep(1)
print('''Please follow these steps:
        1. Create a gmail account (different from your personal account; DO NOT use your personal password; this email will be exposed to customers)''')
initset_email = input("Enter the email ID: ")
initset_emailpass = input("Enter the email ID's password: ")
time.sleep(1)
settingsmodifier(5, str(initset_email))
settingsmodifier(1, str(initset_emailpass))
###############SAVING

print("DBFA sends access notifications, purchase records and OTPs for 2FA to the store owner on Telegram for security purposes.")
time.sleep(1)
print("We will guide you through getting this set-up.")
time.sleep(1)
print('''        1. Install Telegram on your mobile device (Android/ iOS/ HarmonyOS")
        2. Create a Telegram account.
        3. Now search for 'BotFather' on Telegram. (LINK: https://t.me/BotFather)
        4. Send '/newbot' to BotFather as a message.
        5. Now provide BotFather with the bot's name, (and optionally about and description)

        DBFA will use this bot to communicate with you.

        BotFather will now provide you with a 'HTTP API CODE' (EXAMPLE: will look like 123124gk:198461384693694681364961341346134)
        ''')
time.sleep(1)
initset_btoken = input("Enter the HTTP-ACCESS-TOKEN exactly as given including ':' here: ")
settingsmodifier(2, initset_btoken)
time.sleep(1)
###############SAVING
print("DBFA also maintains a Telegram group in which the bot sends shift schedules. Please follow instructions as given below for the same:")
time.sleep(1)
print('''        1. Create a group in Telegram.
        2. Add the BOT you just created to that group.
        3. Now tap on the group's name, select 'Add Members' and search for 'Rose'. (LINK: https://t.me/MissRose_bot)
        4. Add this "Rose" bot to your group.
        5. After adding Rose, send '/id' in the group as a message. Rose will respond with a value to this.
        
        Please enter that value WITH THE NEGATIVE SIGN below:
        (NOTE: You may now remove Rose from the group if you don't want automatic group moderation.)
''')
time.sleep(1)
initset_gchatid = input("Paste the ID exactly as returned by Rose including the negative sign: ")
settingsmodifier(4, initset_gchatid)
time.sleep(1)
###############SAVING
print("For the DBFA bot to send you messages, search for the bot 'Get ID', and send it any text. It will respond with your 'Chat ID'. Please submit the same below: ")
initset_schatid = input("Enter your 'Char ID' as recieved from the 'Get ID' bot: ")
settingsmodifier(3, initset_schatid)
time.sleep(1)
###############SAVING
print("Now please visit the bot you just created and click on start. You may now exit Telegram.")
time.sleep(1)
print("\n\nA few more things: ")
initset_adminpass = input("Enter an Administrator password (DO NOT REVEAL THIS TO YOUR EMPLOYEES): ")
settingsmodifier(6, initset_adminpass)
###############SAVING
time.sleep(1)
print("DBFA will now ask you for a username and password for your cashiers. They will use these to log-into DBFA.")
initset_cshruname = input("Enter a username for your cashiers: ")
settingsmodifier(7, initset_cshruname)
###############SAVING
initset_cshrpass = input("Enter a password for your cashier account: ")
settingsmodifier(8, initset_cshrpass)
###############SAVING
print("That's it! Please give us a few seconds to prepare your DBFA installation.")
time.sleep(2)
settingsmodifier(9, "1")
print("DBFA has been readied! Please use the shortcut on your desktop to start DBFA Client.")