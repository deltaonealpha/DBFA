import time, os
if os.path.exists(r'userblock.txt'):
    os.remove(r'userblock.txt')
if os.path.exists(r'userblock.zconf'):
    os.remove(r'userblock.zconf')

import PySimpleGUI as sg
sg.theme('DarkTeal7')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Login succesfull!')],
            [sg.Button('Proceed')] ]
# Create the Window
window = sg.Window('Login conf.', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    Proceed = "Proceed"
    event, values = window.read()
    if event in ('Proceed'):
        window.close()
        userblock = open(r"userblock.txt","a+") #Opening / creating (if it doesn't exist already) the .txt record file
        userblock.write('ed')
        time.sleep(2)
        userblock.close()
        print("logging success")
        os.startfile('bleading_edge.py')
        window.close()
        window.close()
        exit
        exit
        exit
        break