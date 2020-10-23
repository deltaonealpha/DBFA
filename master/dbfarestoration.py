# ---------------------------------------------- #
# DBFA Nightly Test Build                        #
# Test subject: Auto-estoration of backup files  #
# ---------------------------------------------- #

import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
import os
file_path = filedialog.askopenfilename()
global curdir, parentdir, fontsdir
currdir = str(os.getcwd())

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

import time

print("File selected    : ", (str(file_path).split("/"))[-1])
if (str(file_path).split("/"))[-1] == "DBFABackup.zip" and ((str(file_path).split("/"))[-1]).split('.')[-1] == "zip":
    import os, shutil
    if os.path.exists(currdir+'\\TempRestoration'):
        shutil.rmtree(currdir+'\\TempRestoration', ignore_errors=True)
    os.makedirs(currdir+'\\TempRestoration', mode = 0o777)
    import zipfile
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(currdir+'\\TempRestoration')
    with open (currdir+'\\TempRestoration\\DBFATempc\\backupconfig.txt') as configcheck:
        lines = configcheck.read().splitlines()
        ll = lines[-1]
        if ll == "DELTAID: 12907789":
            valz = 0
        else:
            valz = 1
else:
    valz = 1

if valz == 0:
    print('''---------------------------------
| DBFA Backup Package detected! |
---------------------------------''')
    with open (currdir+'\\TempRestoration\\DBFATempc\\backupconfig.txt') as configcheck:
        lines = configcheck.read().splitlines()
        ll = lines[-2].split("creation:")[-1]
        pssk = lines[-3].split("configpasskey:")[-1]
    conffacz = input("Restore DBFA data backup from:" + str(ll) + "? (y/n): ")
    if conffacz in ("Y", "y"):
        import getpass, time
        passw = getpass.getpass(prompt='\nEnter admin password of backed-up installation to proceed: ', stream=None)
        if passw == pssk:
            print("Getting ready to restore DBFA Backup package ~")
            time.sleep(2)
            mover()

        else:
            print("Invalid password! Re-enter Backup&Switch to try again.")
    else:
        print("Restoration cancelled! ~")
        time.sleep(2)



else:
    print('''-----------------------------
| INVALID package selected! |
-----------------------------
''')
    #print("ehh invalid file go brr")