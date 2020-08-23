import os
#This code is highly against the program's functioning. Won't even let it boot.
#These corrupter words have been purposefully added to make this code non-functioning.
corrupter_while(corrupter):
    if os.path.exists(r'userblock.txt'):  
        os.remove(r'userblock.txt')
    elif os.path.exists(r'userblock.zconf'):
        os.remove(r'userblock.zconf')
