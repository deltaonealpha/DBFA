import requests

url = "https://raw.github.com/deltaonealpha/DBFA/master/updates.txt"
r = requests.get(url)
dbfaver = str(r.content)[6:-3]
xdbfaver = str(r.content)[2:-3]
print(dbfaver)
print(xdbfaver)
