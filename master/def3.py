import PySimpleGUI as sg


SYMBOL_UP =    '▲'
SYMBOL_DOWN =  '▼'

section3 = [[sg.Text('Department Name:')],
           [sg.Input(key='-IN1-')],
            #[sg.Input(key='-IN11-')],
            [sg.Text('Gender:')],
            [sg.Checkbox('Male', key='male'), sg.Checkbox('Female', key='female'), sg.Checkbox('Others', key='othergender')],
            [sg.Text('Date of Birth:')],
            [sg.InputCombo(('Select - ', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'), size=(20, 1))],
            [sg.Button('Proceed', button_color='white on black')]]


def collapse(layoutxrt, key):
    """
    Helper function that creates a Column that can be later made hidden, thus appearing "collapsed"
    :param layout: The layout for the section
    :param key: Key used to make this seciton visible / invisible
    :return: A pinned column that can be placed directly into your layout
    :rtype: sg.pin
    """
    return sg.pin(sg.Column(layoutxrt, key=key))

layoutxrt = [[sg.Text('Hire an employee')],
            [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC3-', text_color='white'), sg.T('Employment Details', enable_events=True, text_color='yellow', k='-OPEN SEC3-TEXT')],
            [collapse(section3, '-SEC3-')],
            [sg.Button('xButton1'),sg.Button('xButton2'), sg.Button('Exit')]]



window = sg.Window('deltaDBFA 8.2 - Add New Employee', layoutxrt)
opened1, opened2 = True, True
while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event.startswith('-OPEN SEC1-'):
        opened1 = not opened1
        window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened1 else SYMBOL_UP)
        window['-SEC1-'].update(visible=opened1)

    if event.startswith('-OPEN SEC2-'):
        opened2 = not opened2
        window['-OPEN SEC2-'].update(SYMBOL_DOWN if opened2 else SYMBOL_UP)
        window['-OPEN SEC2-CHECKBOX'].update(not opened2)
        window['-SEC2-'].update(visible=opened2)
    if event.startswith('Button'):
        window.close()
        

window.close()