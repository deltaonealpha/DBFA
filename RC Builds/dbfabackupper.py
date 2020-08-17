from zipfile import ZipFile 
import os, shutil, time
from tqdm import tqdm 


command = "cls"
os.system(command)


print("DBFA Backup & Switch Utility")
time.sleep(0.7)
if os.path.exists(r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\delauth.txt'):
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


def copier():
    for i in tqdm (range (100), desc="Processing:                       "): 
        slave = r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\DBFATempc'
        if os.path.exists(r'delauth.txt'):
            master = r'cponmgmtsys.db'
            shutil.copy(master, slave)
            master = r'lastupdateid.txt'
            shutil.copy(master, slave)
            time.sleep(0.0000000001)
            master = r'DBFA.db'
            shutil.copy(master, slave)
            master = r'DBFA_CUSTCC.db'
            shutil.copy(master, slave)
            master = r'DBFA_handler.db'
            shutil.copy(master, slave)
            master = r'recmaster.db'
            shutil.copy(master, slave)
            time.sleep(0.0000000001)
            master = r'invoicemaster.db'
            shutil.copy(master, slave)
            master = r'registry.txt'
            shutil.copy(master, slave)
            master = r'stockature.txt'
            shutil.copy(master, slave)
            master = r'tempfile.temp'
            shutil.copy(master, slave)
            master = r'qr-code.png'
            shutil.copy(master, slave)
            time.sleep(0.0000000001)
            master = r'log.txt'
            shutil.copy(master, slave)
            os.remove(r'delauth.txt')
            master = r'DBFA_vend.db'
            shutil.copy(master, slave)
            master = r'client_secrets.json'
            shutil.copy(master, slave)
            master = r'DBFAdeliveries.txt'
            shutil.copy(master, slave)
            master = r'graphing_testbuild.py'
            shutil.copy(master, slave)
            master = r'wrelogin.pyw'
            shutil.copy(master, slave)
            master = r'run_DBFA.pyw'
            shutil.copy(master, slave)
            master = r'lastupdateid.txt'
            shutil.copy(master, slave)
            master = r'dlr.pyq'
            shutil.copy(master, slave)
            
try:
    for i in tqdm (range (100), desc="Creating File Structure:          "): 
        if os.path.exists(r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFATempc'):
            shutil.rmtree(r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFATempc', ignore_errors=True)
        if os.path.exists(r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFA_Backup&Switchc'):
            shutil.rmtree(r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFA_Backup&Switchc', ignore_errors=True)
        if not os.path.exists(r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFATempc'):
            os.mkdir(r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFATempc', mode = 0o777, dir_fd = None)
        if not os.path.exists(r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFA_Backup&Switchc'):
            os.mkdir(r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFA_Backup&Switchc', mode = 0o777, dir_fd = None)
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
        directory = r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFATempc'
        file_paths = get_all_file_paths(directory) 

        with ZipFile('DBFABackup.zip','w') as zip: 
            for file in file_paths: 
                zip.write(file) 

        

    if __name__ == "__main__": 
        for i in tqdm (range (100), desc="Zipping Files:                    "): 
            main()
            time.sleep(0.000001)
    time.sleep(1)

    shutil.move('DBFABackup.zip', 'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFA_Backup&Switchc')  

    for i in tqdm (range (100), desc="Cleaning up:                      "): 
        shutil.rmtree(r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFATempc', ignore_errors=True)
        time.sleep(0.000001)
    for i in tqdm (range (100), desc="Writing Restoration Instructions: "): 
        slave = r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFATempc'
        master = r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\Assets\\instructions.txt'
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

        directory = r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFA_Backup&Switchc'

        folders = drive.ListFile(
            {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
        for folder in folders:
            if folder['title'] == folderName:
                file2 = drive.CreateFile({'parents': [{'id': folder['id']}]})
                file2.SetContentFile(r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFA_Backup&Switchc\\DBFABackup.zip')
                file2.Upload()
        os.startfile(r'delauth.py')
    else:
        time.sleep(2)
        os.startfile(r'delauth.py')
        os._exit(0)



        print("Directory: {} backed up successfully".format(directory))
except:
    time.sleep(1)
    print("PERMISSION ERROR: We couldn't get access to DBFA directories.")
