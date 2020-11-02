import sqlite3
netprof = sqlite3.connect('recmaster.db')
netprofx = netprof.cursor()
netprofx.execute("SELECT * FROM recmasterx")
dataout = netprofx.fetchall()
rowheights = ()
leng = len(dataout)
for i in range(1, leng+2):
    rowheights += (20,)
