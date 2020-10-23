from os import curdir, error
from typing import KeysView
from zipfile import ZipFile 
import os, shutil, time
from tqdm import tqdm 
import traceback

command = "cls"
os.system(command)

global curdir, parentdir, fontsdir
currdir = str(os.getcwd())

print("DBFA Backup & Switch Utility")
time.sleep(0.7)
if os.path.exists(currdir+'\\delauth.txt'):
    pass
else:
    print("Authenication bypased. Exiting.")
    time.sleep(1)
    os._exit(0)
print("-------------------------------------")
print("All previous backups will be removed.")
print("-------------------------------------")
print("")
time.sleep(2)
print("Fetching settings..")
print("")
time.sleep(0.5)

import os
from datetime import datetime  #for reporting the billing time and date
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")  #datetime object containing current date and time
def securedatafetch(SettingsType):
    import sqlite3
    settings = sqlite3.connect(r'dbfasettings.db')
    settingsx = settings.cursor()
    settingsx.execute(("SELECT Col1 from passkeyhandler WHERE Sno = ?"), (SettingsType,))
    settingsfetch = (settingsx.fetchall()[0][0])
    return settingsfetch
with open('backupconfig.txt', 'a+') as file:
    file.close()
with open('backupconfig.txt', 'r+') as file:
    file.truncate(0)
    file.write("delta Backup Package\n")
    file.write("Installation: DBFA Client\n")
    file.write(str("User: " + str(os.getlogin())))
    file.write(str("configpasskey:" + str(securedatafetch(8))))
    file.write(str("\nTime of creation: " + str(dt_string)))
    file.write("\nDELTAID: 12907789")

def copier():
    slave = 'C:\DBFATempc'
    if os.path.exists(currdir+'\\delauth.txt'):  
        for i in tqdm (range (100), desc="Copying Databases                       "): 
            master = currdir+'\\DBFA_vend.db'
            shutil.copy(master, slave)
            master = currdir+'\\cponmgmtsys.db'
            shutil.copy(master, slave)
            master = currdir+'\\DBFA.db'
            shutil.copy(master, slave)
            master = currdir+'\\DBFA_CUSTCC.db'
            shutil.copy(master, slave)
            master = currdir+'\\DBFA_handler.db'
            shutil.copy(master, slave)
            master = currdir+'\\recmaster.db'
            shutil.copy(master, slave)
            time.sleep(0.0000000001)
            master = currdir+'\\invoicemaster.db'
            shutil.copy(master, slave)
            master = currdir+'\\dbfaempmaster.db'
            shutil.copy(master, slave)
            master = currdir+'\\dbfasales.db'
            shutil.copy(master, slave)
            master = currdir+'\\dbfasettings.db'
            if os.path.exists(currdir+'\\delauth.txt'):
                os.remove(currdir+'\\delauth.txt')
            shutil.copy(master, slave)
            master = currdir+'\\DeepArchivalVault.db'
            shutil.copy(master, slave)
            master = currdir+'\\recmaster.db'
            shutil.copy(master, slave)

        for i in tqdm (range (100), desc="Copying Session Keys                    "): 
            master = currdir+'\\backupconfig.txt'
            shutil.copy(master, slave)
            master = currdir+'\\lastupdateid.txt'
            shutil.copy(master, slave)
            master = currdir+'\\lastupdateid2.txt'
            shutil.copy(master, slave)
            if os.path.exists(currdir+'\\delauth.txt'):
                os.remove(currdir+'\\delauth.txt')
            master = currdir+'\\lastsched.txt'
            shutil.copy(master, slave)
            time.sleep(0.0000000001)

        for i in tqdm (range (100), desc="Copying Authorization Keys              "): 
            master = currdir+'\\tempfile.temp'
            shutil.copy(master, slave)
            if os.path.exists(currdir+'\\delauth.txt'):
                os.remove(currdir+'\\delauth.txt')
            master = currdir+'\\client_secrets.json'
            shutil.copy(master, slave)
            time.sleep(0.0000000001)

        for i in tqdm (range (100), desc="Copying Payment Keys                    "): 
            master = currdir+'\\DBFAdeliveries.txt'
            shutil.copy(master, slave)
            master = currdir+'\\payqr.png'
            if os.path.exists(currdir+'\\delauth.txt'):
                os.remove(currdir+'\\delauth.txt')
            shutil.copy(master, slave)
            time.sleep(0.0000000001)

        for i in tqdm (range (100), desc="Copying Registery & Logs Files          "): 
            master = currdir+'\\log.txt'
            shutil.copy(master, slave)
            master = currdir+'\\devclog.txt'
            if os.path.exists(currdir+'\\delauth.txt'):
                os.remove(currdir+'\\delauth.txt')
            shutil.copy(master, slave)
            master = currdir+'\\registry.txt'
            shutil.copy(master, slave)
            time.sleep(0.0000000001)
            time.sleep(0.0000000001)
            
try:
    for i in tqdm (range (100), desc="Creating File Structure:          "): 
        if os.path.exists('C:\DBFATempc'):
            shutil.rmtree('C:\DBFATempc', ignore_errors=True)
        if os.path.exists(currdir+'\\DBFA_Backup&Switchc'):
            shutil.rmtree(currdir+'\\DBFA_Backup&Switchc', ignore_errors=True)
        if os.path.exists('C:\DBFATempc'):
            os.remove('C:\DBFATempc')
        os.makedirs('C:\DBFATempc', mode = 0o777)
        os.makedirs(currdir+'\\DBFA_Backup&Switchc', mode = 0o777)
        #, dir_fd = None
        time.sleep(0.000001)
    copier()

    def get_all_file_paths(directory): 
        file_paths = [] 
        for root, directories, files in os.walk(directory): 
            for filename in files: 
                filepath = os.path.join(root, filename) 
                file_paths.append(filepath) 
        return file_paths		 

    def main(): 
        directory = 'C:\DBFATempc'
        file_paths = get_all_file_paths(directory) 

        with ZipFile('DBFABackup.zip','w') as zip: 
            for file in file_paths: 
                zip.write(file) 

        

    if __name__ == "__main__": 
        for i in tqdm (range (100), desc="Archiving Backup:                    "): 
            main()
            time.sleep(0.000001)
    time.sleep(1)

    shutil.move('DBFABackup.zip', (currdir+'\\DBFA_Backup&Switchc'))

    for i in tqdm (range (100), desc="Cleaning up:                      "): 
        shutil.rmtree('C:\DBFATempc', ignore_errors=True)
        time.sleep(0.000001)
        if os.path.exists(currdir+'\\backupconfig.txt'):
            os.remove(currdir+'\\backupconfig.txt')
    for i in tqdm (range (100), desc="Writing Restoration Instructions: "): 
        slave = currdir+'\\DBFA_Backup&Switchc'
        master = currdir+'\\Assets\\instructions.txt'
        shutil.copy(master, slave)
        time.sleep(0.000001)
    print("")
    print("Backup created succesfully.")
    time.sleep(2)

    drivefac = (input("Enter *1* to further backup the same to your Google Drive. To cancel, press *enter*"))
    if drivefac == "1":
        time.sleep(1)
        from pydrive.auth import GoogleAuth
        from pydrive.drive import GoogleDrive
        import os

        g_login = GoogleAuth()
        g_login.LocalWebserverAuth()
        drive = GoogleDrive(g_login)

        folderName = 'DBFA_Backup&Switchc'  # Please set the folder name.


        drive_folder = drive.CreateFile({
            'title': "DBFA_Backup&Switchc",
            "mimeType": "application/vnd.google-apps.folder"
        })
        drive_folder.Upload()

        directory = currdir+'\\DBFA_Backup&Switchc'

        folders = drive.ListFile(
            {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.foldecurrdir+'\\ and trashed=false"}).GetList()
        for folder in folders:
            if folder['title'] == folderName:
                file2 = drive.CreateFile({'parents': [{'id': folder['id']}]})
                file2.SetContentFile(currdir+'\\DBFA_Backup&Switchc\\DBFABackup.zip')
                file2.Upload()
                print("Backup archive uploaded to Google Drive ~")
        os.startfile(currdir+'\\DBFA_Backup&Switchc')
        os.startfile(currdir+'\\run_DBFA.pyw')
    else:
        time.sleep(2)
        os.startfile(currdir+'\\DBFA_Backup&Switchc')
        os.startfile(currdir+'\\run_DBFA.pyw')
        os._exit(0)

        print("Directory: {} backed up successfully".format(directory))
except:
    time.sleep(1)
    print("PERMISSION ERROR: We couldn't get access to DBFA directories.")
    error_message = traceback.format_exc()
    print(error_message)
    os.startfile(currdir+'\\DBFA_Backup&Switchc')
    time.sleep(10)