import csv

#read and count documment

#opening file

file = open (r"C:\Users\Redford\Documents\Proyecto automatizacion\data1.txt") #open file
counter = 0
total_lines = len(file.readlines()) #count lines
#print('Total lines:', x)

#reading from file
content = file.read()
colist  = content.split ()
print(colist)





for i in colist:
    if i:
        counter += 1

print(counter) #cuenta cuatas lineas tine el documento txt
            

            
lines = open (r"C:\Users\Redford\Documents\Proyecto automatizacion\data1.txt")
arr = []
with open('readme.txt', 'w') as f:
    for line in lines:
        #f.write(line)
        #f.write('%d')
        #f.write(line)
        arr.append(line)
        f.write([line])
        #f.write(line + ' ')
        
        print ([arr])

        
        




        
#locating and reading file


#with open (r"C:\Users\Redford\Documents\Proyecto automatizacion\data.txt") as file:
# lines = [line.strip() for line in file]





