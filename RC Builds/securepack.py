print("Removing ALL registered customer records now...")
import os, time
print("        ___ ______ ___   _____________    ____________     _______")
time.sleep(0.1)
print("       /  /_______/  /  /  /_______/  /  /  /________/    /  /_/ /")
time.sleep(0.1)
print("      /  /       /  /  /  /       /  /  /  /             /  /  / /")
time.sleep(0.1)
print("     /  /       /  /  /  /_______/  /  /  /  CLI        /  /   / /")
time.sleep(0.1)
print("    /  /       /  /  / // // // // /  /  /_________    /  /____/ /")
time.sleep(0.1)
print("   /  /       /  /  /  /-------/  /  /  /_________/   /  /_____/ /")
time.sleep(0.1)
print("  /  /       /  /  /  /       /  /  /  /             /  /      / /")
time.sleep(0.1)
print(" /  /_______/  /  /  /______ /  /  /  /             /  /       / /")
time.sleep(0.1)
print("/__/_______/__/  /__/_______/__/  /__/             /__/        /__/")
print(" ")
print(" ")
time.sleep(2)
print("Flushing record directory. ")
time.sleep(0.5)
print("Flushing record directory. . ")
time.sleep(0.5)
print("Flushing record directory. . . ")
time.sleep(0.5)

x = "cponmgmtsys.db"
if os.path.exists(r'DBFA.db'):
    file = open(x, 'rb')
    data = file.read()
    os.remove(os.path.normpath(r"DBFA.db"))
if os.path.exists(r'DBFA.db'):
    file = open(x, 'rb')
    data = file.read()
    os.remove(os.path.normpath(r"DBFA.db"))
print("Database flush completed!")
time.sleep(1)
print("Restarting DBFA")
time.sleep(1)
os.startfile(r"bleading_edge.py")
