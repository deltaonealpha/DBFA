import os, requests, time
from md5checker import make_hash

os.system('cls')
print("------------------------------------")
print("delta Installation Integrity Checker")
print("------------------------------------")
time.sleep(1)


listing = ('bleading_edge', 'modif2fa', 'dbfaempman', 'plotter', 'delauth', 'dbfabackupper', 'authtimeout', 'securepack', 'securepackxvc', 'wrelogin', 'run_DBFA')

print("Fetching MD5 from server.")
servermd5 = ((requests.get("https://raw.githubusercontent.com/deltaonealpha/DBFA/master/md5")).content).decode('utf-8')
#.replace(" ", "").replace("\n", "")
serverdump = (servermd5.split())
print("Arranging hashes ###\n")
server_md5 = []
server_md5.append(serverdump[0].replace(" ", "").replace("\n", ""))
server_md5.append(serverdump[1].replace(" ", "").replace("\n", ""))
server_md5.append(serverdump[2].replace(" ", "").replace("\n", ""))
server_md5.append(serverdump[3].replace(" ", "").replace("\n", ""))
server_md5.append(serverdump[4].replace(" ", "").replace("\n", ""))
server_md5.append(serverdump[5].replace(" ", "").replace("\n", ""))
server_md5.append(serverdump[6].replace(" ", "").replace("\n", ""))
server_md5.append(serverdump[7].replace(" ", "").replace("\n", ""))
server_md5.append(serverdump[8].replace(" ", "").replace("\n", ""))
server_md5.append(serverdump[9].replace(" ", "").replace("\n", ""))
server_md5.append(serverdump[10].replace(" ", "").replace("\n", ""))

print("Fetching logged MD5.\n")
try:
    localdump = str(open(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\md5').read())
    sorteddump = (localdump.split())
    print("Arranging hashes ###\n")
    local_md5 = []
    local_md5.append(sorteddump[0].replace(" ", "").replace("\n", ""))
    local_md5.append(sorteddump[1].replace(" ", "").replace("\n", ""))
    local_md5.append(sorteddump[2].replace(" ", "").replace("\n", ""))
    local_md5.append(sorteddump[3].replace(" ", "").replace("\n", ""))
    local_md5.append(sorteddump[4].replace(" ", "").replace("\n", ""))
    local_md5.append(sorteddump[5].replace(" ", "").replace("\n", ""))
    local_md5.append(sorteddump[6].replace(" ", "").replace("\n", ""))
    local_md5.append(sorteddump[7].replace(" ", "").replace("\n", ""))
    local_md5.append(sorteddump[8].replace(" ", "").replace("\n", ""))
    local_md5.append(sorteddump[9].replace(" ", "").replace("\n", ""))
    local_md5.append(sorteddump[10].replace(" ", "").replace("\n", ""))
except:
    print("DBFA's code has been tampered with! Please rectify this to avoid such program crashes!")
    print("    rrtt - Master Copy Error: dta=intl.err_instldir?imp=md5lognotfound")


print("Hashing MD5 from deployed code.")
live_md5 = []
live_md5.append(make_hash('bleading_edge.py', algo='md5'))
live_md5.append(make_hash('modif2fa.py', algo='md5'))
live_md5.append(make_hash('dbfaempman.py', algo='md5'))
live_md5.append(make_hash('plotter.pyw', algo='md5'))
live_md5.append(make_hash('delauth.py', algo='md5'))
live_md5.append(make_hash('dbfabackupper.py', algo='md5'))
live_md5.append(make_hash('authtimeout.pyw', algo='md5'))
live_md5.append(make_hash('securepack.py', algo='md5'))
live_md5.append(make_hash('securepackxvc.py', algo='md5'))
live_md5.append(make_hash('wrelogin.pyw', algo='md5'))
live_md5.append(make_hash('run_DBFA.pyw', algo='md5'))
print("Arranging hashes ###\n")


alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(listing)):
    if live_md5[i] != local_md5[i]:
        print("! - Misaligned MD5 at")
        print(live_md5[i], local_md5[i], "////\n")
print("Alignment check done p1x")

for i in server_md5:
    arter = ""
    for j in i.replace(" ", "").replace("\n", ""):
        if str(j).isalpha() is True:
            arter += '%d'%(alphas.index(j.lower()))
        else:
            arter += j
    server_md5[server_md5.index(i)] = int(arter)

for i in local_md5:
    arter = ""
    for j in i.replace(" ", "").replace("\n", ""):
        if str(j).isalpha() is True:
            arter += '%d'%(alphas.index(j.lower()))
        else:
            arter += j
    local_md5[local_md5.index(i)] = int(arter)

for i in live_md5:
    arter = ""
    for j in i.replace(" ", "").replace("\n", ""):
        if str(j).isalpha() is True:
            arter += '%d'%(alphas.index(j.lower()))
        else:
            arter += j
    live_md5[live_md5.index(i)] = int(arter)

for i in range(len(listing)):
    if live_md5[i] != local_md5[i]:
        print("! - Misaligned MD5 at")
        print(live_md5[i], local_md5[i], "////\n")
print("Alignment check done p2x")

print("\n")
if live_md5 != local_md5:
    marker = 1
    issue = i
elif live_md5 == local_md5:
    marker = 2
        
if marker == 1:
    print("DBFA's code has been tampered with! Please rectify this to avoid such program crashes!")
    print("Further diagnosis details: ")
    try:
        print("Issue with service: ", listing(live_md5[issue]))
    except:
        pass
    if sum(server_md5) == sum(live_md5):
        print("    DBFA is updated with latest source")
    elif sum(server_md5) > sum(live_md5):
        print("    DBFA is running on an older build.\nPlease update your installation!\nNew updated often pack new features, bug-fixes and security improvements.")
    elif sum(server_md5) < sum(live_md5):
        print("    Master Copy Error: dta=intl.err_undercommit?imp=buildahead")
elif marker == 2:
    if sum(server_md5) == sum(live_md5):
        print("    DBFA is updated with latest source")
    elif sum(server_md5) > sum(live_md5):
        print("    DBFA is running on an older build.\n    Please update your installation!\n    New updates often pack new features, bug-fixes and security improvements.")
    elif sum(server_md5) < sum(live_md5):
        print("    Master Copy Error: dta=intl.err_undercommit?imp=buildahead")
        print("\n- The driver code of this installation of DBFA seems to be fine.")
        print("- We request you to try rebooting your device and re-opening DBFA.")
        print("- If you encounter the same issue again, please contact DBFA support or re-install DBFA AFTER CREATING A DATA BACKUP FOR DBFA.")
else:
    print("Integrity checker service failed to execute properly \\ | / |  -_- -_- -_-  \\ | / | ")