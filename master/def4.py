import requests, os, time, shutil, oschmod
os.system('cls')
print("---------------------------------\n\n༼ つ ◕_◕ ༽つ delta Update Utility\n\n---------------------------------")
time.sleep(1)
url = "https://raw.github.com/deltaonealpha/DBFA/master/updates.txt"
r = requests.get(url)
dbfaver = str(r.content)[6:-3]
xdbfaver = str(r.content)[2:-3]

with open(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\updates.txt', 'r+') as upread:
    upread = (str(upread.read())).strip()

print("Server: ", (xdbfaver + '%s'%len(xdbfaver)), "\nLocal: ", (upread + '%s'%len(upread)))
time.sleep(1)
if float(upread[4: ]) > float(dbfaver):
    print("\n\nThe local installation seems to have a greater version ID than the server copy\n༼ つ ◕_◕ ༽つ  つ ༽ ◕_◕ つ༼")
    print("\nIf this is the master edition, have you committed?\n\n")
else:
    if xdbfaver == upread:
        print("This installation of DBFA is up-to date! ")
    else:
        print("A new DBFA update is available: DBFA", dbfaver)
        try:
            oschmod.set_mode(r"C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\DBFA", "777")
        except:
            pass
        shutil.rmtree(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\DBFA', ignore_errors=True)
        try:
            os.rmdir(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\DBFA')
        except:
            pass
        if os.path.isdir(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\DBFA') == True:
            shutil.rmtree(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\DBFA', ignore_errors=True)
            print("Cleaning-up previous update package... ")
        else:
            pass

        os.system('git clone https://github.com/deltaonealpha/DBFA')
        os.system('git log')
        #os.system(r'git rev-parse HEAD')

        print("The new package has been downloaded to your DBFA installation > master > DBFA")
        print("Please replace *only the required* files manually. Read DBFA docs on GitHub for instructions.")