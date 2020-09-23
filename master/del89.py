import os, requests, time
from md5checker import make_hash

os.system('cls')
print("------------------------------------")
print("delta Installation Integrity Checker")
print("------------------------------------")
time.sleep(1)

print(make_hash('modif2fa.py', algo='md5'))
print(make_hash('dbfaempman.py', algo='md5'))
print(make_hash('plotter.pyw', algo='md5'))
print(make_hash('delauth.py', algo='md5'))
print(make_hash('dbfabackupper.py', algo='md5'))
print(make_hash('authtimeout.pyw', algo='md5'))
print(make_hash('securepack.py', algo='md5'))
print(make_hash('securepackxvc.py', algo='md5'))
print(make_hash('wrelogin.pyw', algo='md5'))
print(make_hash('run_DBFA.pyw', algo='md5'))

live_md5 = (make_hash('bleading_edge.py', algo='md5')).replace(" ", "").replace("\n", "")
print("Hashing MD5 from deployed code.")
time.sleep(0.2)
server_md5 = ((requests.get("https://raw.githubusercontent.com/deltaonealpha/DBFA/master/md5")).content).decode('utf-8').replace(" ", "").replace("\n", "")
print("Fetching MD5 from server.")
time.sleep(0.2)
try:
    local_md5 = (open(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\md5')).read().replace(" ", "").replace("\n", "")
    print("Fetching logged MD5.\n")
    time.sleep(0.2)
except:
    print("rrttDBFA's code has been tampered with! Please rectify this to avoid such program crashes!")
    print("    Master Copy Error: dta=intl.err_instldir?imp=md5lognotfound")

time.sleep(1)
xlocal_md5 = ""
xlive_md5 = ""
xserver_md5 = ""

alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in local_md5:
    if i.isalpha() is True:
        xlocal_md5 += str('%d'%(alphas.index(i)))
    else:
        xlocal_md5 += (str(i))

for i in live_md5:
    if i.isalpha() is True:
        xlive_md5 += str('%d'%(alphas.index(i)))
    else:
        xlive_md5 += (str(i))

for i in server_md5:
    if i.isalpha() is True:
        xserver_md5 += str('%d'%(alphas.index(i)))
    else:
        xserver_md5 += (str(i))

print(local_md5, xlocal_md5)
print(live_md5, xlive_md5)
print(server_md5, xserver_md5)

print("\n")
if xlive_md5 != xlocal_md5:
    print("DBFA's code has been tampered with! Please rectify this to avoid such program crashes!")
    print("Further diagnosis details: ")
    if xserver_md5 == xlive_md5:
        print("    DBFA is updated with latest source")
    elif xserver_md5 > xlive_md5:
        print("    DBFA is running on an older build.\nPlease update your installation!\nNew updated often pack new features, bug-fixes and security improvements.")
    elif xserver_md5 < xlive_md5:
        print("    Master Copy Error: dta=intl.err_undercommit?imp=buildahead")
elif xlive_md5 == xlocal_md5:
    if xserver_md5 == xlive_md5:
        print("    DBFA is updated with latest source")
    elif xserver_md5 > xlive_md5:
        print("    DBFA is running on an older build.\n    Please update your installation!\n    New updates often pack new features, bug-fixes and security improvements.")
    elif xserver_md5 < xlive_md5:
        print("    Master Copy Error: dta=intl.err_undercommit?imp=buildahead")
    print("\n- The driver code of this installation of DBFA seems to be fine.")
    print("- We request you to try rebooting your device and re-opening DBFA.")
    print("- If you encounter the same issue again, please contact DBFA support or re-install DBFA AFTER CREATING A DATA BACKUP FOR DBFA.")