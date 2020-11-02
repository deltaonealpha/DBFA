import requests, os, time, shutil, oschmod
os.system('cls')
print('''---------------------------------
 delta Update Deployment Service
---------------------------------
Checking for updates. . . 
---------------------------------''')
time.sleep(1)

import os, time
global curdir, parentdir, fontsdir
currdir = str(os.getcwd())
from pathlib import Path
path = Path(os.getcwd())
parentdir = str(Path(path.parent))
#print(parentdir)
#print(parentdir+'\\updates.txt')
userdir = os.path.expanduser('~')
url = "https://raw.githubusercontent.com/deltaonealpha/DBFA_UpdateHandler/master/updates.txt"
r = requests.get(url)
dbfaver = ((str(r.content.decode('utf-8'))))[4:]
xdbfaver = ((str(r.content.decode('utf-8'))))
with open(parentdir+'\\updates.txt', 'r+') as upread:
    upread = (str(upread.read())).strip()

print("Server: ", dbfaver, "\nLocal: ", upread[4: ])
time.sleep(1)
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
        print("This installation of DBFA is already up-to date ~ \n")
        dddu_ddu = input("Press 'enter' to restart DBFA: ")
        os.startfile('run_DBFA.pyw')

    elif spass1 != spass2:
        time.sleep(1)
        print("A new DBFA update is available: DBFA", dbfaver, "\nUpdate Notes: \n")
        clog = requests.get('https://raw.githubusercontent.com/deltaonealpha/DBFA_UpdateHandler/master/updatechangelog.txt')
        print(str(clog.content.decode('utf-8')), "\n\n")
        time.sleep(2)
        updateconfo =  input("Update DBFA now? (y/n): ")
        if updateconfo == "y":
            try:
                os.remove(currdir+'\\updatertemp')
                shutil.rmtree(currdir+'\\updatertemp', ignore_errors=True)
                time.sleep(0.000001)
                os.remove(currdir+'\\DBFA_UpdateHandler')
                shutil.rmtree(currdir+'\\DBFA_UpdateHandler', ignore_errors=True)
            except:
                pass
            if os.path.exists(currdir+'\\DBFA_UpdateHandler'):
                shutil.rmtree(currdir+'\\DBFA_UpdateHandler', ignore_errors=True)
                shutil.rmtree(currdir+'\\DBFA_UpdateHandler', ignore_errors=True)
            if os.path.exists(currdir+'\\DBFA_UpdateHandler'):
                os.startfile(currdir+'\\DBFA_UpdateHandler')
                dddu_ddu = input("Please go to DBFA's installation folder and delete the folder 'DBFA_UpdateHandler'. Press enter once done: ")
            try:
                oschmod.set_mode(currdir+'\\DBFA_UpdateHandler', "777")
            except:
                pass
            shutil.rmtree(currdir+'\\DBFA_UpdateHandler', ignore_errors=True)
            try:
                os.rmdir(currdir+'\\DBFA_UpdateHandler')
            except:
                pass
            if os.path.isdir(currdir+'\\DBFA_UpdateHandler') == True:
                shutil.rmtree(currdir+'\\DBFA_UpdateHandler', ignore_errors=True)
                print("Cleaning-up previous update packages... ")
                shutil.rmtree(currdir+'\\DBFA_UpdateHandler', ignore_errors=True)
                try:
                    os.rmdir(currdir+'\\DBFA_UpdateHandler')
                except:
                    pass
            else:
                pass
            if os.path.exists(currdir+'\\DBFA_UpdateHandler'):
                shutil.rmtree(currdir+'\\DBFA_UpdateHandler', ignore_errors=True)
            try:
                os.system('git clone https://github.com/deltaonealpha/DBFA_UpdateHandler')
            except:
                print("The directory 'DBFA_UpdateHandler' already exists.")
                print("Please delete it from DBFA's installation location and re-run the updater.")
            #os.system('git log')
            print("Commit: ")
            os.system(r'git rev-parse HEAD')
            file_path = currdir+'\\DBFA_UpdateHandler\\updatepackage.zip'
            import os, shutil, time
            if os.path.exists(currdir+'\\updatertemp'):
                shutil.rmtree(currdir+'\\updatertemp', ignore_errors=True)
            os.makedirs(currdir+'\\updatertemp', mode = 0o777)
            import zipfile
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(currdir+'\\updatertemp')
            from tqdm import tqdm
            import shutil, os, time, sys
            slave = currdir
            for i in tqdm (range (100), desc="Updating DBFA:                       "): 
                for j in os.scandir(currdir+'\\updatertemp'):
                    master = currdir+'\\updatertemp\\'+str(j).replace("<DirEntry '", "").replace("'>", "")
                    shutil.copy(master, slave)
                    time.sleep(0.00001)
                master = currdir+'\\DBFA_UpdateHandler\\updates.txt'
                shutil.copy(master, parentdir)
            for i in tqdm (range (100), desc="Cleaning up:                         "): 
                shutil.rmtree(currdir+'\\updatertemp', ignore_errors=True)
                time.sleep(0.000001)
                shutil.rmtree(currdir+'\\DBFA_UpdateHandler', ignore_errors=True)
            print("Your DBFA installation has been succesfully updated to DBFA", dbfaver, ".")
            dddu_ddu = input("Press 'enter' to restart DBFA: ")
            os.startfile('run_DBFA.pyw')

        if updateconfo == "n":
            time.sleep(1)
            print("Use this, (option 11) whenever you want to update DBFA. We recommend doing so on urgent grounds. DBFA updates bring better security and new ground-breaking features with them!")
            dddu_ddu = input("Press 'enter' to restart DBFA: ")
            os.startfile('run_DBFA.pyw')