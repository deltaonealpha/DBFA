import os
import time
if os.path.exists(r'userblock.txt'):
    os.remove(r'userblock.txt')
if os.path.exists(r'userblock.zconf'):
    os.remove(r'userblock.zconf')
def Login():
    import PySimpleGUI as sgx
    sgx.theme('DarkTeal10')
    #print("\nWARNING:  CAPS LOCK IS ENABLED!\n")
    layout = [  [sgx.Text('█▀▀█  █▀█  █▀▀ █▀█  █▀▀█')],
                [sgx.Text('█___█ █▀▀█ █▀  █▬█  ▄▄▄▄')],
                [sgx.Text(' ')],
                [sgx.Text('DBFA Client exited as the timeout period was attained')],
                [sgx.Text('(Client needs to be launched within a minute of completing primary login.)')],
                [sgx.Text(' ')],
                [sgx.Text('Error code: dtaec1103-authtimeout')],
                [sgx.Button('Exit')], [sgx.Text('DBFA crashed?')], [sgx.Button('Submit Crash Report')]]
    




    window = sgx.Window('delta ClientOAuth Handler', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):	# if user closes window or clicks cancel
            window.close()
            break
        if event in ('DBFA crashed?', 'Submit Crash Report'):
            print("crashreport")
            window.close
            break
        
        

import PySimpleGUI as sg
if os.path.exists(r'userblock.txt'):
    os.remove(r'userblock.txt')
if os.path.exists(r'userblock.zconf'):
    os.remove(r'userblock.zconf')

Login()
