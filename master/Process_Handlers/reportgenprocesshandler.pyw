import os
import time

import PySimpleGUI as sgx
sgx.theme('BlueMono')
#print("\nWARNING:  CAPS LOCK IS ENABLED!\n")
layout1 = [  [sgx.Text('DBFA Process Handler')],
            [sgx.Text('Process: Creating Report        ')],
            [sgx.Text("████                           |")]]

layout2 = [  [sgx.Text('DBFA Process Handler')],
            [sgx.Text('Process: Creating Report        ')],
            [sgx.Text("██████                          ")]]

layout3 = [  [sgx.Text('DBFA Process Handler')],
            [sgx.Text('Process: Creating Report        ')],
            [sgx.Text("██████████                      ")]]

layout4 = [  [sgx.Text('DBFA Process Handler')],
            [sgx.Text('Process: Creating Report        ')],
            [sgx.Text("██████████████                  ")]]
layout5 = [  [sgx.Text('DBFA Process Handler')],
            [sgx.Text('Process: Creating Report        ')],
            [sgx.Text("██████████████████              ")]]
layout6 = [  [sgx.Text('DBFA Process Handler')],
            [sgx.Text('Process: Creating Report        ')],
            [sgx.Text("████████████████████████        ")]]
layout7 = [  [sgx.Text('DBFA Process Handler')],
            [sgx.Text('Process: Creating Report        ')],
            [sgx.Text("███████████████████████████████|")]]


window = sgx.Window('DBFA ProcessHandler', layout1, no_titlebar=True, location=(1149, 673),  keep_on_top=True)
event, values = window.read(timeout = 220)
window = sgx.Window('DBFA ProcessHandler', layout2, no_titlebar=True, location=(1149, 673),  keep_on_top=True)
event, values = window.read(timeout = 220)
window = sgx.Window('DBFA ProcessHandler', layout3, no_titlebar=True, location=(1149, 673),  keep_on_top=True)
event, values = window.read(timeout = 220)
window = sgx.Window('DBFA ProcessHandler', layout4, no_titlebar=True, location=(1149, 673),  keep_on_top=True)
event, values = window.read(timeout = 220)
window = sgx.Window('DBFA ProcessHandler', layout5, no_titlebar=True, location=(1149, 673),  keep_on_top=True)
event, values = window.read(timeout = 220)
window = sgx.Window('DBFA ProcessHandler', layout6, no_titlebar=True, location=(1149, 673),  keep_on_top=True)
event, values = window.read(timeout = 220)
window = sgx.Window('DBFA ProcessHandler', layout7, no_titlebar=True, location=(1140, 673),  keep_on_top=True)
event, values = window.read(timeout = 220)
#time.sleep(2)
window.close()
delche = 1



