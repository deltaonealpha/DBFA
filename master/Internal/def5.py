import sqlite3
settings = sqlite3.connect(r'test2.db')
settingsx = settings.cursor()

# xa2 = input("wut: ")
# settingsx.execute("SELECT * FROM xtable WHERE a2 = (?)", (xa2,))
# print(settingsx.fetchall())

settingsx.execute("SELECT xtable.a1, xtable.a2, xtable2.b3 FROM xtable, xtable2 WHERE xtable.a2 = xtable2.b3")
print(settingsx.fetchall())

