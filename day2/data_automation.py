import numpy as np

#read and count documment

#opening file

file = open(r"C:\Users\Redford\Documents\Proyecto automatizacion\data.txt")
counter = 0

#reading from file

content = file.read()
colist  = content.split ("\n")


for i in colist:
    if i:
        counter += 1
        print(colist)


print(counter)

        
#locating and reading file


with open (r"C:\Users\Redford\Documents\Proyecto automatizacion\data.txt") as file:
    lines = [line.strip() for line in file]