import sqlite3, time
import matplotlib.pyplot as plt
salesr = sqlite3.connect(r'dbfasales.db')
salesx = salesr.cursor()
datefetch = []

salesx.execute("SELECT DISTINCT date FROM sales")    
for i in salesx.fetchall():
    datefetch.append((i[0]))

netray = []
for i in datefetch:
    salesx.execute(("SELECT sum(prof) FROM sales WHERE date = ?"), (i, ))
    netray.append(salesx.fetchall()[0][0])

# Plotting
plt.plot(datefetch, netray, color='purple', linestyle='dashed', linewidth = 3, 
        marker='o', markerfacecolor='magenta', markersize=12) 
# naming the x axis 
plt.xlabel('Date') 
# naming the y axis 
plt.ylabel('Profit') 
# Graph Title
plt.title('DBFA Profit Report') 
time.sleep(1)
# Finally, display
plt.show() 