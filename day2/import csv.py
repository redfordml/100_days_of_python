import csv

with open("t.csv","w",newline="") as wr, open(r"C:\Users\Redford\Documents\GitHub\100_days_of_Python\Day2\data3.txt") as r:
    # create a csv writer
    writer = csv.writer(wr)

    person =[]
    for line in r: # could use enumerate as well, this works ok
        # collect line data minus the \n into list
        person.append(line.strip())

        # this person is finished, write, clear list
        if len(person) == 7:
            writer.writerow(person)
            person = [] # reset

    # something went wrong, your file is inconsistent, write remainder
    if person:
        writer.writerow(person)

print(open("t.csv").read())