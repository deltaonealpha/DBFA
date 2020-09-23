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
                [sgx.Text('¯\_(⊙︿⊙)_/¯¯\_(⊙︿⊙)_/¯')],
                [sgx.Text('Error: dbfa.exe is confused           ')],
                [sgx.Text('Input logic/ code/ runtime error!')],
                [sgx.Text(' ')],
                [sgx.Text('Troubleshooter: ')],
                [sgx.Text('- Entered an invalid input?')],
                [sgx.Text('- Modified the code?')],
                [sgx.Text("- Changed something in DBFA's installation directory?")],
                [sgx.Text('- Recently updated Windows or installed a software?')],
                [sgx.Text(' ')],
                [sgx.Text('Error code: dtaec1207-unexpectedcrash')],
                [sgx.Button('Exit')], [sgx.Button('Submit Crash Report')]]
    
    window = sgx.Window('delta Process Handler', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):	# if user closes window or clicks cancel
            window.close()
            delche = 1
            break
        if event in ('DBFA crashed?', 'Submit Crash Report'):
            print("crashreport")
            window.close()
            delche = 1
            import PySimpleGUI as sgx
            sgx.theme('DarkTeal10')
            #print("\nWARNING:  CAPS LOCK IS ENABLED!\n")
            layout = [  [sgx.Text('█▀▀█  █▀█  █▀▀ █▀█  █▀▀█')],
                        [sgx.Text('█___█ █▀▀█ █▀  █▬█  ▄▄▄▄')],
                        [sgx.Text(' ')],
                        [sgx.Text('Crash report has been submited! ')],
                        [sgx.Button('Exit')]]
            window = sgx.Window('delta ClientOAuth Handler', layout)
            while True:
                event, values = window.read()
                if event in (None, 'Exit'):	# if user closes window or clicks cancel
                    window.close()
                    break

            
            
        

import PySimpleGUI as sg
if os.path.exists(r'userblock.txt'):
    os.remove(r'userblock.txt')
if os.path.exists(r'userblock.zconf'):
    os.remove(r'userblock.zconf')

Login()


