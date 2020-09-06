import PySimpleGUI as sg


SYMBOL_UP =    '▲'
SYMBOL_DOWN =  '▼'


def collapse(layout, key):
    """
    Helper function that creates a Column that can be later made hidden, thus appearing "collapsed"
    :param layout: The layout for the section
    :param key: Key used to make this seciton visible / invisible
    :return: A pinned column that can be placed directly into your layout
    :rtype: sg.pin
    """
    return sg.pin(sg.Column(layout, key=key))


section1 = [[sg.Text('Name:')],
            [sg.Input(key='-IN1-')],
            #[sg.Input(key='-IN11-')],
            [sg.Text('Gender:')],
            [sg.Checkbox('Male', key='male'), sg.Checkbox('Female', key='female'), sg.Checkbox('Others', key='othergender')],
            [sg.Text('Date of Birth:')],
            [sg.InputCombo(('Select - ', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'), size=(20, 1))],
            [sg.Button('Proceed', button_color='white on black')]]

section2 = [[sg.Text('Email:')],
            [sg.I(k='-IN2-')],
            [sg.Text('Mobile Contact:')],
            [sg.I(k='-IN3-')],
            [sg.Text('Residential Address:')],
            [sg.I(k='-IN4-')],
            [sg.Text("Employee's UPI ID for salary payments:")],
            [sg.I(k='-IN5-')]]

section3 = [[sg.Text('Department Name:')],
            [sg.InputCombo(('Select - ', 'IT' ,'Administration', 'Sales', 'Care-taking', 'Logistics'), size=(20, 1))],
            #[sg.Input(key='-IN11-')],
            [sg.Text('Designation:')],
            [sg.Input(key='-IN32-')],
            [sg.Text('Salary:')],
            [sg.Input(key='-IN33-')]]


layout =   [[sg.Text('Hire an employee')],
            #### Section 1 part ####
            [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC1-', text_color='white'), sg.T('Personal Details', enable_events=True, text_color='yellow', k='-OPEN SEC1-TEXT')],
            [collapse(section1, '-SEC1-')],
            #### Section 2 part ####
            [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC2-', text_color='white'),
             sg.T('Personal Details', enable_events=True, text_color='white', k='-OPEN SEC2-TEXT')],
            [collapse(section2, '-SEC2-')],
            #### Buttons at bottom ####
            [sg.Button('Proceed'), sg.Button('Exit')]]
            

layout3 = [[sg.Text('Hire an employee')],
            [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC3-', text_color='white'), sg.T('Employment Details', enable_events=True, text_color='yellow', k='-OPEN SEC3-TEXT')],
            [collapse(section3, '-SEC3-')],
            [sg.Button('Complete Form >>>'), sg.Button('Exit')]]

window = sg.Window('deltaDBFA 8.2 - Add New Employee', layout)
arter = 0
opened1, opened2 = True, True

while True:             # Event Loop
    event, values = window.read()
    eventx, valuesx = event, values
    #print(event, values)
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
    
    if  event.startswith('Proceed'):
        axt = open(r"dbfaempre.txt", "w+")
        axt.write(str(eventx))
        axt.write(str(valuesx))
        window.close()
        window = sg.Window('deltaDBFA 8.2 - Add New Employee', layout3)
        opened1, opened2 = True, True
        while True:             # Event Loop
            event, values = window.read()
            eventr, valuesr = event, values
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
                break

            if event.startswith('Complete Form'):
                opened1 = not opened1
                arter = 1
                window.close()
                break

        

window.close()
if arter == 0:
    print("No data recieved! ")
if arter == 1:
    print("Data sets recieved! ")
    print(eventx, valuesx)
    #print(eventx, valuesx)
    print("_____\n\n________")
    print(eventr, valuesr)

