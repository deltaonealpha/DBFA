def dictgetlisting():
    import sqlite3
    settings = sqlite3.connect(r'dbfasettings.db')
    settingsx = settings.cursor()

    xnamiex = []
    xdatax = []
    settingsx.execute("SELECT Name FROM listing")
    for i in settingsx.fetchall():
        xnamiex.append(i[0])
    settingsx.execute("SELECT Cost FROM listing")
    for i in settingsx.fetchall():
        xdatax.append(i[0])
    namiex, datax = xnamiex, xdatax
    lenx = []
    for i in range(1, len(namiex)+1):
        lenx.append(i)
    print(lenx)
    res = {} 
    for key in lenx: 
        for value in namiex: 
            res[key] = value 
            namiex.remove(value) 
            break  
    #print("Resultant dictionary is : " +  str(res))
    res = {}
    for key in lenx: 
        for value in datax: 
            res[key] = value 
            datax.remove(value) 
            break   
    #print("Resultant dictionary is : " +  str(res)) 

print(dictgetlisting())