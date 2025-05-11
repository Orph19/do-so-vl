#!/usr/bin/env python3
import pathlib
import csv

f1 = pathlib.Path("int.txt")
f2 = pathlib.Path("out.txt")
f3 = pathlib.Path("README.md")
f4 = pathlib.Path("dts.csv")

a = [[f'name {b}',b] for b in range(46,100)]#generates list of list, each for a row
a.insert(0,['name','score']) #first row, name of the colums

class WR:
    def __init__(self):
        pass
    def start(self): #with the name of the columns on the first line
        with f4.open('w') as sheet:
            writer = csv.writer(sheet)
            writer.writerows(a)
        return print('done')
    def append(self): #generate new lines of names a numbers
            del a[0]
            writer = csv.writer(sheet)
            writer.writerows(a)
        return print('done')
    def read(self): #read all to the terminal
        with f4.open('r') as data:
            printer = csv.reader(data)
            i = 0
            for row in printer:
                if i == 0:
                    print("The colums are {}".format(', '.join(row)))
                else:
                    print("{} scored {}".format(row[0],row[1]))
                i += 1
    def clean(self): #empty all the file
        with f4.open('w') as cleaner:
            cleaner.truncate()
        return print('all cleaned')


vari = WR()
vari.start()
# vari.clean()

