import mysql.connector

mydb = mysql.connector.connect(
        host="remotemysql.com", port = 3306,
        user="bZkgzPvgiG",
        passwd="lfDieKGBN6",
        database="bZkgzPvgiG")

mycursor = mydb.cursor()
namiex = ["TV 4K OLED 50", "TV FHD OLED 50", "8K QLED 80", "Redmi K20 PRO", "Redmi K20", "Redmi Note 9 PRO", "POCOPHONE F1", "Mi MIX ALPHA", "Wireless Headphones", "Noise-Cancelling Wireless Headphones", "Essentials Headphones", "Gaming Headphones", "Truly-Wireless Eadphones", "Neckband-Style Wireless Earphones", "Essentials Earphones", "Gaming Earphones", "30W Bluetooth Speakers", "20W Bluetooth Speakers", "Essentials Bluetooth Speaker", "BOSE QC35", "Essentials Home Theatre", "Wired Speaker - 5.1", "Essentials Wired Speaker - STEREO", "Tactical Series Power Bank 30000mah", "Essentials Power Bank 10000mah", "Essentials Mouse", "Logitech G604 LightSpeed Wireless", "Tactical Essentials Keyboard", "DROP GS21k RGB Gaming Keyboard", "Polowski Tactical Flashlight", "OneFiber Wi-Fi Router AX7", "Mijia Mesh Wi-Fi Router", "lapcare 45W Laptop Adapter", "lapcare 60W Laptop Adapter","Spigen Phone Case(s)", "Essentials Phone Charger 15W", "HyperPower Type-C Gallium-Nitride Charger 120W", "ASUS Zephyrus G4 Gaming Laptop", "DELL XPS 5 Content Creator's Laptop", "Hewlett-Packard Essential's Student's Laptop (Chromebook)"]
prodprofit = [2000, 4500, 5700, 2000, 2100, 1470, 300, 11000, 400, 2000, 100, 370, 450, 120, 50, 275, 649, 140, 50, 1050, 978, 150, 100, 320, 98, 75, 170, 60, 275, 90, 210, 780, 50, 35, 50, 30, 100, 8000, 9000, 1790]
prodsales = [65, 50, 27, 38, 52, 14, 25, 20, 20, 21, 20, 46, 2, 28, 7, 1, 27, 14, 6, 2, 14, 10, 5, 12, 14, 9, 22, 16, 17, 4, 6, 4, 4, 9, 3, 2, 6, 3, 4, 8]
netprof = [130000, 225000, 153900, 76000, 109200, 20850, 7500, 220000, 8000, 42000, 2000, 17020, 900, 3360, 350, 275, 17523, 1960, 300, 2100, 13692, 1500, 500, 3840, 1372, 675, 3740, 960, 4675, 360, 1260, 3120, 200, 315, 150, 60, 600, 24000, 36000, 14320]

arter = ("INSERT INTO `recmasterx`(`prodid`, `prodname`, `prodprofit`, `prodsales`, `netprof`) VALUES (%s, %s, %s, %s, %s)")

for i in range(1, 41):
    print(i, namiex[i-1], prodprofit[i-1], prodsales[i-1], netprof[i-1])
    arterx = (i, namiex[i-1], prodprofit[i-10], prodsales[i-1], netprof[i-1])
    mycursor.execute(arter, arterx)
mydb.commit()
mycursor.execute("SELECT * FROM recmasterx")
for x in mycursor:
  print(x)