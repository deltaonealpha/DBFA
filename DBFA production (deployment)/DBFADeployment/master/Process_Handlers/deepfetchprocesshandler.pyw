import PySimpleGUI as sgx
sgx.theme('BlueMono')
#print("\nWARNING:  CAPS LOCK IS ENABLED!\n")
layout1 = [ [sgx.Text('DBFA Deep Archival VAULT')],
            [sgx.Text('A list of archived invoices will now be printed.')],
            [sgx.Text("Please note the required invoice ID,")],
            [sgx.Text("and enter the same when asked for. ")],
            [sgx.Button("Proceed> ")]]

window = sgx.Window('DBFA ProcessHandler', layout1, no_titlebar=True,  keep_on_top=True)
while True:
    event, values = window.read()
    if event in (None, 'Quit', 'Proceed> '):	# if user closes window or clicks cancel
        window.close()
        break
