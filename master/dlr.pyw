import time, os
if os.path.exists(r'userblock.txt'):
    os.remove(r'userblock.txt')
if os.path.exists(r'userblock.zconf'):
    os.remove(r'userblock.zconf')

import PySimpleGUI as sg
sg.theme('DarkTanBlue')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Login succesfull!')],
            [sg.Button('Proceed')] ]
# Create the Window
window = sg.Window('Login conf.', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in ('Proceed'):
        window.close()
        userblock = open(r"userblock.txt","a+") #Opening / creating (if it doesn't exist already) the .txt record file
        userblock.write('ed')
        userblock.close()
        print("logging success")
        time.sleep(2)
        window.close()
        window.close()
        time.sleep(1)
        from pathlib import Path
        p = Path('userblock.txt')
        p.rename(p.with_suffix('.zconf'))
        time.sleep(0.4)
        os.startfile('hms1.py')

'''while True:
    event, values = window.read()
    window.close()
    userblock = open(r"userblock.txt","a+") #Opening / creating (if it doesn't exist already) the .txt record file
    userblock.write('ed')
    userblock.close()
    print("logging success")
    time.sleep(2)
    window.close()
    window.close()
    time.sleep(1)
    from pathlib import Path
    p = Path('userblock.txt')
    p.rename(p.with_suffix('.zconf'))
    time.sleep(0.4)
    os.startfile('hms1.py')'''

