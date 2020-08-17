#init
telethon = ""
writer = ""

import time, os, sqlite3, tabularprint, tabulate



# Pending Delivery Count
delcount = 0
filedel = open('./DBFAdeliveries.txt', 'r+')
for line in filedel:
    delcount+=1
filedel.close()
if delcount != 0:
    print("Number of pending deliveries: ", delcount)
else:
    print("No deliveries pending! ")





# Show data and Remove delivery record
print("Current delivery data::  \n")
filedel = open('./DBFAdeliveries.txt', 'r')
for line in filedel:
    print(line)
print("\n\n")
cleanstr = ""
deledid = input("Enter the delivery ID to remove (EXAMPLE: *del2*): ")
delcount = 0
filedel = open('./DBFAdeliveries.txt', 'r')
for line in filedel:
    if deledid in line:
        line = ""
    else:
        delcount+=1
    cleanstr+=line
filedel.close()
filedel = open('./DBFAdeliveries.txt', 'w+')
filedel.write(cleanstr)
filedel.close()
filedel = open('./DBFAdeliveries.txt', 'r')
print("Delivery", deledid, "completed! ")



'''

# Add a delivery
print("---- DBFA Deliveries ----")
delname = input("Customer's Name: ")
time.sleep(0.1)
print("Customer's Address:")
def getaddress():
    print("         Enter/paste the address. Press Ctrl-Z ( windows ) to save it.")
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    address = ""
    for i in contents:
        address += i+", "
    return address
addressx = getaddress()
print("Address entered: ", addressx)
addressfac = input("Confirm address or change? (y/n): ")
if addressfac == "y":
    # Count pending deliveries
    delcount = 0
    filedel = open('./DBFAdeliveries.txt', 'r')
    for line in filedel:
        delcount+=1
    filedel = open('./DBFAdeliveries.txt', 'a+')
    filedel.write("\ndel"+str(delcount+1) + "    " + addressx)
    filedel.close()
if addressfac == "n":
    getaddress()
elif addressfac not in ("y", "n"):
    print("Invalid option! ")
    pass

print("\n\n--- DBFA Delivery Ticket ---\n", delname,"\n", addressx,"\n\n----------------------------")

sfetch_values = ""
redeemindic = 0
writer += "\n\nDBFA Delivery\n\n"
telethon += "\n\nDBFA Delivery\n\n"

print("Deliveries only support pay-on-delivery.")