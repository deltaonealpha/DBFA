import os
import time
if os.path.exists(r'userblock.txt'):
    os.remove(r'userblock.txt')
if os.path.exists(r'userblock.zconf'):
    os.remove(r'userblock.zconf')
def Login():
    import PySimpleGUI as sgx
    sgx.theme('DarkRed')
    layout = [  [sgx.Text('INVALID LOGIN. Please retry:')],
                [sgx.Text('Username: '), sgx.InputText()],
                [sgx.Text('Password: '), sgx.InputText(password_char='*')],
                [sgx.Button('Authenicate'), sgx.Button('Cancel')] ]
    window = sgx.Window('deltaAuthenication Service', layout)
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
