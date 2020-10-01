import os
import time
import spotilib
from SwSpotify import spotify

from datetime import datetime  #for reporting the billing time and date

sysuser = 'balaj'
delpen = 14
prof_today = 1233
prof_week = 8765445
def Main():
    import PySimpleGUI as sgx
    sgx.theme('BlueMono')
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")  #datetime object containing current date and time
    #print("\nWARNING:  CAPS LOCK IS ENABLED!\n")
    try:
        #spacelock = (((60-6)-(len(spotify.current()[0])+len(spotify.current()[1])))*" ")
        layout = [  [sgx.Text('█▀▀█  █▀█  █▀▀ █▀█  █▀▀█'), sgx.Text('                                                                                                    The OG Store Manager', font='Arial 11')],
                    [sgx.Text('█___█ █▀▀█ █▀  █▬█  ▄▄▄▄'), sgx.Text('                                                                                                 CLIENT 8.552 DONNAGER', font='Arial 10')],
                    [sgx.Text('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')],
                    [sgx.Text('Profit (today):'), sgx.Text(prof_today), sgx.Text(int((149-(38+len(str(prof_today))+len(str(prof_week)))))*" "), sgx.Text('Profit (past week):'), sgx.Text(prof_week), ],
                    [sgx.Text('Deliveries pending:'), sgx.Text(delpen), sgx.Text(int((176-(48+len(sysuser)+len(str(delpen))))/3)*" "), sgx.Text('DBFA User:'), sgx.Text(sysuser), sgx.Text(int((176-(48+len(sysuser)+len(str(delpen))))/3)*" "), sgx.Text(dt_string)],
                    [sgx.Text("███████████████████████████████████████████████████████████████████████████████████")],
                    [sgx.Text('What would you like to do?\n' , text_color='black')],
                    [sgx.Text('Invoicing                       '), sgx.Button('Issue a Bill'), sgx.Text('                                                     Generate store report: '), sgx.Button('Store Report')],
                    [sgx.Text('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬     Store report list earned profits, stock analytics')],
                    [sgx.Text('Manage Customers'), sgx.Text('   '), sgx.Button('Register a Customer'), sgx.Button('Customer Registry'), sgx.Text('                            and records as logged by DBFA.')], 
                    [sgx.Text('                                   '), sgx.Button('Export data as CSV'), sgx.Button('Purchase Records'), sgx.Text('     '), sgx.Text('View/ mark deliveries: ') ,sgx.Button('Manage Deliveries')],
                    [sgx.Text('                                   '), sgx.Button('Find a Customer'), sgx.Text('                                          '), sgx.Text('Manager settings:      ') ,sgx.Button('DBFA Options')],
                    [sgx.Text('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  '), sgx.Text('Backup all data:        '), sgx.Button('DBFA Backup & Switch')],
                    [sgx.Text('Manage Store        '), sgx.Text('   '), sgx.Button('Manage Stock'), sgx.Button('DBFA Stock Master'), sgx.Text('            '), sgx.Text('Plot sales:                '), sgx.Button('Analyse Sales')], 
                    [sgx.Text('                                   '), sgx.Button('Manage Vouchers'), sgx.Button('Product Listing'), sgx.Text('              '), sgx.Text('Manage Employees   ') ,sgx.Button('Employee Manager', button_color=('lightyellow', 'black'))],
                    [sgx.Text('                                   '), sgx.Button('Sales Log'), sgx.Button('Export store data as CSV'), sgx.Text('          '), sgx.Text('View software license:'), sgx.Button('Licensing Information')],
                    [sgx.Text('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬      Build notes                ') ,sgx.Button('About DBFA')],
                    [sgx.Text("Currently playing:", text_color='darkred'), sgx.Text(spotify.current()[0], text_color='darkblue'), sgx.Text('by', text_color='darkred'), sgx.Text(spotify.current()[1], text_color='darkblue')],
                    [sgx.Text('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')],
                    [sgx.Button('Check for Updates'), sgx.Button('Mark Attendance') ,sgx.Button('Quit'), sgx.Text("                        DBFA Music Contols:"), sgx.Button(' < prev '), sgx.Text('|'), sgx.Button(' pause | | '), sgx.Text('|'), sgx.Button(' next > ')]]

    except:
        #print(Fore.MAGENTA, "No music playing. Use Spotify to play your favourite music and control it via DBFA", Fore.CYAN)
        layout = [  [sgx.Text('█▀▀█  █▀█  █▀▀ █▀█  █▀▀█'), sgx.Text('                                                                                                    The OG Store Manager', font='Arial 11')],
                    [sgx.Text('█___█ █▀▀█ █▀  █▬█  ▄▄▄▄'), sgx.Text('                                                                                                 CLIENT 8.552 DONNAGER', font='Arial 10')],
                    [sgx.Text('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')],
                    [sgx.Text('Profit (today):'), sgx.Text(prof_today), sgx.Text(int((149-(38+len(str(prof_today))+len(str(prof_week)))))*" "), sgx.Text('Profit (past week):'), sgx.Text(prof_week), ],
                    [sgx.Text('Deliveries pending:'), sgx.Text(delpen), sgx.Text(int((176-(48+len(sysuser)+len(str(delpen))))/3)*" "), sgx.Text('DBFA User:'), sgx.Text(sysuser), sgx.Text(int((176-(48+len(sysuser)+len(str(delpen))))/3)*" "), sgx.Text(dt_string)],
                    [sgx.Text("███████████████████████████████████████████████████████████████████████████████████")],
                    [sgx.Text('What would you like to do?\n' , text_color='black')],
                    [sgx.Text('Invoicing                       '), sgx.Button('Issue a Bill'), sgx.Text('                                                     Generate store report: '), sgx.Button('Store Report')],
                    [sgx.Text('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬     Store report list earned profits, stock analytics')],
                    [sgx.Text('Manage Customers'), sgx.Text('   '), sgx.Button('Register a Customer'), sgx.Button('Customer Registry'), sgx.Text('                            and records as logged by DBFA.')], 
                    [sgx.Text('                                   '), sgx.Button('Export data as CSV'), sgx.Button('Purchase Records'), sgx.Text('     '), sgx.Text('View/ mark deliveries: ') ,sgx.Button('Manage Deliveries')],
                    [sgx.Text('                                   '), sgx.Button('Find a Customer'), sgx.Text('                                          '), sgx.Text('Manager settings:      ') ,sgx.Button('DBFA Options')],
                    [sgx.Text('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  '), sgx.Text('Backup all data:        '), sgx.Button('DBFA Backup & Switch')],
                    [sgx.Text('Manage Store        '), sgx.Text('   '), sgx.Button('Manage Stock'), sgx.Button('DBFA Stock Master'), sgx.Text('            '), sgx.Text('Plot sales:                '), sgx.Button('Analyse Sales')], 
                    [sgx.Text('                                   '), sgx.Button('Manage Vouchers'), sgx.Button('Product Listing'), sgx.Text('              '), sgx.Text('Manage Employees   ') ,sgx.Button('Employee Manager', button_color=('lightyellow', 'black'))],
                    [sgx.Text('                                   '), sgx.Button('Sales Log'), sgx.Button('Export store data as CSV'), sgx.Text('          '), sgx.Text('View software license:'), sgx.Button('Licensing Information')],
                    [sgx.Text("No music playing. Play your favourite music and control it via DBFA            ", text_color='darkred'), sgx.Text('Build notes                ') ,sgx.Button('About DBFA')],
                    [sgx.Text('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')],
                    [sgx.Button('Check for Updates'), sgx.Button('Mark Attendance') ,sgx.Button('Quit'), sgx.Text("                        DBFA Music Contols:"), sgx.Button(' < prev '), sgx.Text('|'), sgx.Button(' pause | | '), sgx.Text('|'), sgx.Button(' next > ')]]


    window = sgx.Window('DBFA Manager Client 8.556', layout, no_titlebar=True,  keep_on_top=False)
    
    
    while True:
        event, values = window.read()
        if event in (None, 'Quit'):	# if user closes window or clicks cancel
            window.close()
            delche = 1
            break

        if event in ('Issue a Bill'):	# if user closes window or clicks cancel
            print('1')

        if event in ('Store Report'):	# if user closes window or clicks cancel
            print('2')
            import sqlite3, time, os, sys
            from reportlab.pdfbase import pdfmetrics
            from reportlab.pdfbase.ttfonts import TTFont
            pdfmetrics.registerFont(TTFont('MiLanProVF', r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\MiLanProVF.ttf'))
            from reportlab.pdfgen import canvas
            from reportlab.lib.pagesizes import A4
            from reportlab.platypus import SimpleDocTemplate, Paragraph
            from reportlab.lib.styles import getSampleStyleSheet
            from reportlab.lib.units import cm
            from reportlab.lib.enums import TA_JUSTIFY
            from reportlab.lib.pagesizes import letter
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib.units import inch
            from tabulate import tabulate
            from reportlab.lib import colors
            from reportlab.lib.pagesizes import letter
            from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
            import requests
            import cv2
            rec = sqlite3.connect(r'recmaster.db')
            recx = rec.cursor()

            class HiddenPrints:
                def __enter__(self):
                    self._original_stdout = sys.stdout
                    sys.stdout = open(os.devnull, 'w')
                def __exit__(self, exc_type, exc_val, exc_tb):
                    sys.stdout.close()
                    sys.stdout = self._original_stdout
                    print()

            def telegram_bot_sendtext(bot_message):
                with HiddenPrints():
                    bot_token = '1215404401:AAEvVBwzogEhOvBaW5iSpHRbz3Tnc7fCZis'
                    bot_chatID = '680917769'
                    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
                    response = requests.get(send_text)
                    return response.json()



            namiex = ["TV 4K OLED 50", "TV FHD OLED 50", "8K QLED 80", "Redmi K20 PRO", "Redmi K20", "Redmi Note 9 PRO", "POCOPHONE F1", "Mi MIX ALPHA", "Wireless Headphones", "Noise-Cancelling Wireless Headphones", "Essentials Headphones", "Gaming Headphones", "Truly-Wireless Eadphones", "Neckband-Style Wireless Earphones", "Essentials Earphones", "Gaming Earphones", "30W Bluetooth Speakers", "20W Bluetooth Speakers", "Essentials Bluetooth Speaker", "BOSE QC35", "Essentials Home Theatre", "Wired Speaker - 5.1", "Essentials Wired Speaker - STEREO", "Tactical Series Power Bank 30000mah", "Essentials Power Bank 10000mah", "Essentials Mouse", "Logitech G604 LightSpeed Wireless", "Tactical Essentials Keyboard", "DROP GS21k RGB Gaming Keyboard", "Polowski Tactical Flashlight", "OneFiber Wi-Fi Router AX7", "Mijia Mesh Wi-Fi Router", "lapcare 45W Laptop Adapter", "lapcare 60W Laptop Adapter","Spigen Phone Case(s)", "Essentials Phone Charger 15W", "HyperPower Type-C Gallium-Nitride Charger 120W", "ASUS Zephyrus G4 Gaming Laptop", "DELL XPS 5 Content Creator's Laptop", "Hewlett-Packard Essential's Student's Laptop (Chromebook)"]
            def repstockfetch(): 
                global tabarter
                ssh = sqlite3.connect('DBFA_handler.db')
                ssh.row_factory = lambda cursor, row: row[0]
                ssh7 = ssh.cursor()
                ssh7.execute("SELECT DISTINCT prodid FROM sshandler WHERE ssstock < 5;")
                axrows = ssh7.fetchall()
                tabarter = []
                for i in axrows:
                    ssh7.execute("SELECT DISTINCT ssstock FROM sshandler WHERE prodid = ?;", (i,))
                    a = [('%s'%(i)), namiex[i], "Stock Remaining: ", '%s'%(ssh7.fetchall()[0])]
                    tabarter.append(a)
                if tabarter == []:
                    tabarter.append("--")

            def repdatafetch():
                global charter, rows
                charter = ""
                charter += "DBFA STORE REPORT\n"
                rec = sqlite3.connect(r'recmaster.db')
                recx = rec.cursor()
                charter += "\nSales data:: \n\n"
                time.sleep(1)
                recx.execute("SELECT DISTINCT prodid, prodname, prodprofit, prodsales, netprof FROM recmasterx")
                rows = recx.fetchall()
                '''
                for row in rows:
                    print(row)
                '''
                ll = [("P.ID","Prod. Name","Profit P.U.","Qty. Sold","Net Profit")]
                rows = ll + rows
                time.sleep(0.1)
                #print(" ") 
                    


            command = "cls"
            os.system(command)
            repstockfetch()
            repdatafetch()
            findMaximum = "select max(prodsales) from recmasterx"
            recx.execute(findMaximum)
            # Print the maximum score
            netr = recx.fetchone()[0]
            findin = "select prodid, prodname, prodprofit, prodsales, netprof from recmasterx WHERE prodsales = ?"
            arterx = (str(int(netr)),)
            recx.execute(findin, arterx)
            arterxout = recx.fetchall()

            findMaximumProf = "select max(netprof) from recmasterx"
            recx.execute(findMaximumProf)
            xnetr = recx.fetchone()[0]
            findin = "select prodid, prodname, prodprofit, prodsales, netprof from recmasterx WHERE netprof = ?"
            xarterx = str(int(xnetr))
            xxarterx = (xarterx,)
            recx.execute(findin, xxarterx)
            xarterxout = recx.fetchall()

            isol = sqlite3.connect(r'DBFA_vend.db')
            isolx = isol.cursor()
            isolx = isol.cursor()
            isolx.execute(("SELECT prodid, prodname, ordqty, delstat, vendor from stock WHERE delstat = ?"), ("TBD", ))
            rowsrec = isolx.fetchall()
            col_labels = [("P. ID", "P. Name", "Qty. to be delivered", "Status", "Vendor")]
            rowsxtb = col_labels + rowsrec

            def add_page_number(canvas, doc):
                canvas.saveState()
                canvas.setFont('Times-Roman', 10)
                page_number_text = "%d" % (doc.page)
                canvas.drawCentredString(
                    0.75 * inch,
                    0.75 * inch,
                    page_number_text
                )
                canvas.restoreState()

            import sqlite3 as sql
            csvexx=sql.connect(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\DBFA_CUSTCC.db')
            cursorx = csvexx.cursor()
            axct = cursorx.execute("select * from custcc")
            axctx = []
            for i in axct:
                axctx.append(i)
            axctx = [("C. ID","C. Name","Purchases Made","Total Amount","Loyalty Points")] + axctx
            doc = SimpleDocTemplate("dbfastorerep.pdf", pagesize=A4,
                                                rightMargin=2*cm,leftMargin=1.5*cm,
                                                topMargin=1*cm,bottomMargin=2*cm)
            # container for the 'Flowable' objects
            elements = []
            telegram_bot_sendtext("Access alert: Store Report")
            t1dot = ("<b>DBFA Automatic Store Report: </b> <br />This report has been automatically generated. This lists the profit earned, stock analytics and customer records as logged by DBFA.<br /><br />")
            t2dot = ("DBFA synchronously updates its database alongwith algorithmic data interpretation to deliver these reports. <br />This report contains information from the start of using DBFA on this system.<br /><br />")
            t6dot = ("Report generated on: " + dt_string)
            t3dot = ("<br /><br /><b>Most sold listing: </b><br />")
            t4dot = ("<br /><br /><b>Total profit per listing: </b><br /><br />")
            t5dot = ("<br /><br /><b>Most profit making listing: </b><br /><br />")
            t8dot = ("<br /><br /><b>Customer purchases: </b><br /><br />")
            t10dot = ("<br /><br /><br /><br /><br /><br /><b>DBFA Stock Orders Report: </b><br />Product stock yet to be recieved: <br /><br />")
            t11dot = ("<br /><br /><b>DBFA Sales Analysis Plotter: </b><br />DBFA uses advanced data analysis algorithms to generate this plot. This is as per the latest data sets available. <br />")
            colas = (30, 300, 60, 50, 50)
            rowheights = (20, 20, 20, 20, 20,  20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20,20,20,20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20 )
            text1=Paragraph(t1dot)
            text2=Paragraph(t2dot)
            text3=Paragraph(t3dot)
            text4=Paragraph(t4dot)
            text5=Paragraph(t5dot)
            text6=Paragraph(t6dot)
            text8=Paragraph(t8dot)
            text10=Paragraph(t10dot)
            text11=Paragraph(t11dot)
            x=Table(rows, colas, rowheights)
            t=Table(arterxout)
            t2=Table(xarterxout)
            t4=Table(axctx)
            t5=Table(rowsxtb)
            if tabarter == ['--']:
                t7dot = ("<br /><br /><b>All listings currently in stock!</b><br /><br />")
            else:
                t7dot = ("<br /><br /><b>Products running low on stock: </b><br /><br />")

            os.startfile(r'Process_Handlers\\reportgenprocesshandler.pyw')
            tblStyle = TableStyle([('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                                ('VALIGN',(0,0),(-1,-1),'TOP'),
                                ('LINEBELOW',(0,0),(-1,-1),1,colors.black),
                                ('BOX',(0,0),(-1,-1),1,colors.black),
                                ('BOX',(0,0),(0,-1),1,colors.black)])
            tblStyle.add('BACKGROUND',(0,0),(1,0),colors.lightblue)
            tblStyle.add('BACKGROUND',(0,1),(-1,-1),colors.lightblue)
            GRID_STYLE = TableStyle(
                [('GRID', (0,0), (-1,-1), 0.25, colors.black),
                ('ALIGN', (1,1), (-1,-1), 'LEFT')]
                )
            text7=Paragraph(t7dot)
            t3=Table(tabarter)
            t.setStyle(GRID_STYLE)
            t2.setStyle(GRID_STYLE)
            t3.setStyle(GRID_STYLE)
            t4.setStyle(GRID_STYLE)
            t5.setStyle(GRID_STYLE)
            x.setStyle(GRID_STYLE)
            # -------------------------------------------------------------------------------
            import sqlite3, time
            import matplotlib.pyplot as plt
            salesr = sqlite3.connect(r'dbfasales.db')
            salesx = salesr.cursor()
            datefetch = []

            salesx.execute("SELECT DISTINCT date FROM sales")    
            for i in salesx.fetchall():
                datefetch.append((i[0]))

            netray = []
            for i in datefetch:
                salesx.execute(("SELECT sum(prof) FROM sales WHERE date = ?"), (i, ))
                netray.append(salesx.fetchall()[0][0])

            # Plotting
            plt.plot(datefetch, netray, color='purple', linestyle='dashed', linewidth = 3, 
                    marker='o', markerfacecolor='magenta', markersize=12) 
            # naming the x axis 
            plt.xlabel('Date') 
            # naming the y axis 
            plt.ylabel('Profit') 
            # Graph Title
            plt.title('DBFA Profit Report') 
            time.sleep(1)
            # Finally, display
            plt.savefig('DBFAplot.png', dpi=300, bbox_inches='tight')
            # -------------------------------------------------------------------------------

            delI = Image('DBFAplot.png')
            delI.drawHeight =  4.2*inch
            delI.drawWidth = 5.5*inch
            elements.append(text1)
            elements.append(text2)
            elements.append(text6)
            elements.append(text3)
            elements.append(t)
            elements.append(text5)
            elements.append(t2)
            elements.append(text7)
            elements.append(t3)
            elements.append(text4)
            elements.append(x)
            elements.append(text8)
            elements.append(t4)
            elements.append(text10)
            elements.append(t5)
            elements.append(text11)
            elements.append(delI)
            # write the document to disk
            doc.build(elements,
                onFirstPage=add_page_number,
                onLaterPages=add_page_number,)
            window.close()
            Main()
            time.sleep(0.5)
            os.startfile('dbfastorerep.pdf')
            time.sleep(2)

        if event in ('Register a Customer'):	# if user closes window or clicks cancel
            print('3')

        if event in ('Customer Registry'):	# if user closes window or clicks cancel
            print('4')

        if event in ('Export data as CSV'):	# if user closes window or clicks cancel
            print('5')


        if event in ('Purchase Records'):	# if user closes window or clicks cancel
            print('6')

        if event in ('Find a Customer'):	# if user closes window or clicks cancel
            print('7')

        if event in ('Manage Stock'):	# if user closes window or clicks cancel
            print('8')


        if event in ('DBFA Stock Master'):	# if user closes window or clicks cancel
            print('9')


        if event in ('Manage Vouchers'):	# if user closes window or clicks cancel
            print('10')


        if event in ('Product Listing'):	# if user closes window or clicks cancel
            print('11')


        if event in ('Sales Log'):	# if user closes window or clicks cancel
            print('12')


        if event in ('Export store data as CSV'):	# if user closes window or clicks cancel
            print('13')


        if event in ('Manage Deliveries'):	# if user closes window or clicks cancel
            print('14')


        if event in ('DBFA Options'):	# if user closes window or clicks cancel
            print('15')


        if event in ('DBFA Backup & Switch'):	# if user closes window or clicks cancel
            print('16')


        if event in ('Analyse Sales'):	# if user closes window or clicks cancel
            print('17')
            import os
            os.startfile(r'plotter.pyw')


        if event in ('Employee Manager'):	# if user closes window or clicks cancel
            print('18')


        if event in ('Licensing Information'):	# if user closes window or clicks cancel
            print('19')
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("DFBA Framework Runtime Broker", "©2020: DBFA by Pranav Balaji and Sushant Gupta", duration = 1.5)
            import webbrowser
            webbrowser.open('https://telegra.ph/DBFA-Licensing-Information-08-16')
            Main()

        if event in ('About DBFA'):	# if user closes window or clicks cancel
            print('20')
            import webbrowser
            webbrowser.open('https://telegra.ph/DBFA-8-RC2-Highlights-08-17')
            webbrowser.open('https://telegra.ph/DBFA-8-Release-Candidate---1-08-16')
            Main()

        if event in (' < prev '):	# if user closes window or clicks cancel
            try:
                spotilib.previous()
            except Exception as e:
                pass
            print('21')
            window.close()
            Main()


        if event in (' pause | | '):	# if user closes window or clicks cancel
            try:
                spotilib.pause()
            except Exception as e:
                pass
            print('22')
            window.close()
            Main()


        if event in (' next > '):	# if user closes window or clicks cancel
            try:
                spotilib.next()
            except Exception as e:
                pass
            print('23')
            window.close()
            Main()


        if event in ('Mark Attendance'):	# if user closes window or clicks cancel
            print('24')


        if event in ('Check for Updates'):	# if user closes window or clicks cancel
            print('25')


import PySimpleGUI as sg
if os.path.exists(r'userblock.txt'):
    os.remove(r'userblock.txt')
if os.path.exists(r'userblock.zconf'):
    os.remove(r'userblock.zconf')

Main()


