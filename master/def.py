import time, os, sqlite3
from colorama import init, Fore, Back, Style #color-settings for the partner/sponsor adverts

os.system("cls")

time.sleep(2)
print("---------------DBFA Settings---------------")
print("1:    Display boot image                               :", '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|')
print("2:    Email invoice to registered customers            :", '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|')
print("3:    Enable DBFA Music Controls (beta):               :", '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|')
print("4:    Open CSV when exported                           :", '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|')
print("5:    Enable database encryption                       :", ('|'+Fore.RED+'████'+Fore.WHITE+' OFF|')+Fore.RED)
#print(" ")
print(Fore.RED+"6:    Delete customer records                          :"+Fore.WHITE, '|'+Fore.RED+"██ Proceed > "+Fore.WHITE+"|")
print(Fore.RED+"7:    Delete store records                             :"+Fore.WHITE, '|'+Fore.RED+"██ Proceed > "+Fore.WHITE+"|")

print(Fore.MAGENTA+"8:    Check for updates                                :"+' |'+"██ Proceed > "+Fore.WHITE+"|" )

#print(('|'+Fore.MAGENTA+'████'+Fore.WHITE+' OFF|'))
#print('| ON '+Fore.MAGENTA+'████'+Fore.WHITE+'|')
