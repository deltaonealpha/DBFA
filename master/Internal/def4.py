dbfaver = ((str(r.content)[6:-1]).replace("\\n", "")).replace(" ", "")
xdbfaver = ((str(r.content)[2:-3]).replace("\\n", "")).replace(" ", "")

with open(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\updates.txt', 'r+') as upread:
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
        print("This installation of DBFA is up-to date! ")

    elif spass1 != spass2:
        time.sleep(1)
