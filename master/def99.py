import os, requests, time
from md5checker import make_hash

os.system('cls')
print("------------------------------------")
print("delta Installation Integrity Checker")
print("------------------------------------")
time.sleep(1)

server_md5 = ((requests.get("https://raw.githubusercontent.com/deltaonealpha/DBFA/master/md5")).content).decode('utf-8')

#.replace(" ", "").replace("\n", "")

localdump = str(open(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\md5').read())
sorteddump = (localdump.split())

bleading_edge = sorteddump[0]
modif2fa = sorteddump[1]
dbfaempman = sorteddump[2]
plotter = sorteddump[3]
delauth = sorteddump[4]
dbfabackupper = sorteddump[5]
authtimeout = sorteddump[6]
securepack = sorteddump[7]
securepackxvc = sorteddump[8]
wrelogin = sorteddump[9]
run_DBFA = sorteddump[10]

live_bleading_edge = (make_hash('bleading_edge.py', algo='md5')).replace(" ", "").replace("\n", "")
live_modif2fa = (make_hash('modif2fa.py', algo='md5')).replace(" ", "").replace("\n", "")
live_dbfaempman = (make_hash('dbfaempman.py', algo='md5')).replace(" ", "").replace("\n", "")
live_plotter = (make_hash('plotter.pyw', algo='md5')).replace(" ", "").replace("\n", "")
live_delauth = (make_hash('delauth.py', algo='md5')).replace(" ", "").replace("\n", "")
live_dbfabackupper = (make_hash('dbfabackupper.py', algo='md5')).replace(" ", "").replace("\n", "")
live_authtimeout = (make_hash('authtimeout.pyw', algo='md5')).replace(" ", "").replace("\n", "")
live_securepack = (make_hash('securepack.py', algo='md5')).replace(" ", "").replace("\n", "")
live_securepackxvc = (make_hash('securepackxvc.py', algo='md5')).replace(" ", "").replace("\n", "")
live_wrelogin = (make_hash('wrelogin.pyw', algo='md5')).replace(" ", "").replace("\n", "")
live_run_DBFA = (make_hash('run_DBFA.pyw', algo='md5')).replace(" ", "").replace("\n", "")