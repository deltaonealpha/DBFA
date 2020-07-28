import time, os, sqlite3, csv
import pandas as pd
import PySimpleGUI as sg

if os.path.exists(r'userblock.txt'):
    os.remove(r'userblock.txt')
if os.path.exists(r'userblock.zconf'):
    os.remove(r'userblock.zconf')

conn = sqlite3.connect('DBFA.db')
cur = conn.cursor()
cur.execute("SELECT * FROM cust")
l = cur.fetchall()
flat_list = []
for sublist in l:
    flat_list.append(sublist)
mydf = pd.DataFrame(flat_list, columns=['Customer ID', 'Name', 'Email'])
mydf.pivot(index='Customer ID', columns='Name', values='Email').fillna(value='-')


cur.execute("select * from cust")
with open("cust_data.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter="\t")
    csv_writer.writerow([i[0] for i in cur.description])
    csv_writer.writerows(cur)
dirpath = os.getcwd() + "/cust_data.csv"



def table_example():
    filename = "cust_data.csv"
    data = []
    header_list = []
    if filename is not None:
        with open(filename, "r") as infile:
            reader = csv.reader(infile)
            header_list = next(reader)
            try:
                data = list(reader)  # read everything else into a list of rows
            except:
                sg.popup_error('Error reading file')
                return
    sg.set_options(element_padding=(0, 0))

    layout = [[sg.Table(values=data,
                            headings=header_list,
                            max_col_width=3500,
                            auto_size_columns=True,
                            justification='left',
                            num_rows=min(len(data), 200))]]


    window = sg.Window('Table', layout, grab_anywhere=False)
    event, values = window.read()

    window.close()

table_example()