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


try:
    for i in tqdm (range (100), desc="Creating File Structure:  "): 
        if os.path.exists(r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFATemp'):
            shutil.rmtree(r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFATemp', ignore_errors=True)
        if os.path.exists(r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFA_Backup&Switch'):
            shutil.rmtree(r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFA_Backup&Switch', ignore_errors=True)
        if not os.path.exists(r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFATemp'):
            os.mkdir(r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFATemp', mode = 0o777, dir_fd = None)
        if not os.path.exists(r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFA_Backup&Switch'):
            os.mkdir(r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFA_Backup&Switch', mode = 0o777, dir_fd = None)
        time.sleep(0.000001)

    
    for i in tqdm (range (100), desc="Processing:               "): 
        slave = r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\DBFATemp'
        if os.path.exists(r'userblock.txt'):
            master = r'cponmgmtsys.db'
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
            



    def get_all_file_paths(directory): 
        file_paths = [] 
        for root, directories, files in os.walk(directory): 
            for filename in files: 
                filepath = os.path.join(root, filename) 
                file_paths.append(filepath) 
        return file_paths		 

    def main(): 
        directory = r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFATemp'
        file_paths = get_all_file_paths(directory) 

        with ZipFile('DBFABackup.zip','w') as zip: 
            for file in file_paths: 
                zip.write(file) 

        

    if __name__ == "__main__": 
        for i in tqdm (range (100), desc="Zipping Files:            "): 
            main()
            time.sleep(0.000001)
    time.sleep(1)

    shutil.move('DBFABackup.zip', 'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFA_Backup&Switch')  

    for i in tqdm (range (100), desc="Cleaning up:              "): 
        shutil.rmtree(r'C:\\Users\\balaj\\OneDrive\\Documents\\GitHub\\DBFA\\master\\DBFATemp', ignore_errors=True)
        time.sleep(0.000001)
    print("")
    print("Backup created succesfully.")

    time.sleep(1)
    ins = open(r"instructions.txt", "a+")  #Opening / creating (if it doesn't exist already) the .txt record file
    ins.write("----------------------------------------- \n")
    time.sleep(2)

except:
    time.sleep(1)
    print("PERMISSION ERROR: We couldn't get access to DBFA directories.")