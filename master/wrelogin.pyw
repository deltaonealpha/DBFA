import os
import time
if os.path.exists(r'userblock.txt'):
    os.remove(r'userblock.txt')
if os.path.exists(r'userblock.zconf'):
    os.remove(r'userblock.zconf')
def Login():
    creds = 'tempfile.temp'
    with open(creds, 'r') as f:
        data = f.readlines() # This takes the entire document we put the info into and puts it into the data variable
        uname = data[0].rstrip() # Data[0], 0 is the first line, 1 is the second and so on.
        pword = data[1].rstrip() # Using .rstrip() will remove the \n (new line) word from before when we input it
        import PySimpleGUI as sgx
        sgx.theme('DarkTanBlue')	# Add a touch of color
        # All the stuff inside your window.
        layout = [  [sgx.Text('INVALID LOGIN. Please retry:')],
                    [sgx.Text('Username: '), sgx.InputText()],
                    [sgx.Text('Password (shh... secret): '), sgx.InputText()],
                    [sgx.Button('Send data to Russia'), sgx.Button('Cancel')] ]
        # Create the Window
        window = sgx.Window('pl0x gib password', layout)
        # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):	# if user closes window or clicks cancel
            window.close
            break
        window.close()
        window.close()
        if values[0] == 'ed' and values[1] == 'edd':
            #os.close(r'DDD.py')
            window.close()
            window.close()
            os.startfile('dlr.pyw')
            exit
            break
        else:
            os.startfile("wrelogin.pyw")
            exit
        #window.close
        #erraise()
import PySimpleGUI as sg
if os.path.exists(r'userblock.txt'):
    os.remove(r'userblock.txt')
if os.path.exists(r'userblock.zconf'):
    os.remove(r'userblock.zconf')

Login()
