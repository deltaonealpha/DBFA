import csv

def writecsv(filename, data):
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def readcsv(filename):
    with open(filename) as file:
        xcsv = csv.reader(file)
        for row in xcsv:
            print(row)


writecsv(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\csv.csv', [['a', 1], ['b', 2]])

readcsv(r'C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master\csv.csv')