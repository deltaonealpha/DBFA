import os
import time
if os.path.exists(r'userblock.txt'):
    os.remove(r'userblock.txt')
if os.path.exists(r'userblock.zconf'):
    os.remove(r'userblock.zconf')
def Login():
    import PySimpleGUI as sgx
    sgx.theme('BlueMono')
    #print("\nWARNING:  CAPS LOCK IS ENABLED!\n")
    layout = [  [sgx.Text('█▀▀█  █▀█  █▀▀ █▀█  █▀▀█     ¯\_(⊙︿⊙)_/¯')],
                [sgx.Text('█___█ █▀▀█ █▀  █▬█  ▄▄▄▄     ¯\_(⊙︿⊙)_/¯')],
                [sgx.Text("delta Installation Integrity Validation Service")],
                [sgx.Text("████████████████████████████████████████████████")],
                [sgx.Text('Contacting DBFA servers')],
                [sgx.Text('Integrity checker result: ')],
                [sgx.Text("     DBFA's code has been tampered with! Please rectify this!")],
                [sgx.Text("     Further diagnosis details: ")],
                [sgx.Text('          Master Copy Error: dta=intl.err_undercommit?imp=buildahead')],
                [sgx.Text('\nError code: dta=intl.err_undercommit?imp=buildahead\n')],
                [sgx.Text('Analysis not correct?'), sgx.Button('Submit crash report'), sgx.Button('Exit')]]
    window = sgx.Window('delta Process Handler', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):	# if user closes window or clicks cancel
            window.close()
            delche = 1
            break
        if event in ('Analysis not correct?', 'Submit crash report'):
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


