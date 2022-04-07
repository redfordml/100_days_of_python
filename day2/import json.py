from doctest import Example
import json


file = ./example.txt

#dictionary
dict = {}

#read file

with open (file) as fn:
    for d in fn:
        #read lines from file
        key, desc = d.strip().split(None,1)
        dict [key] = desc.strip()

otfile = open ("output.json", "w")
json.dump(dict,otfile,)
otfile.close()


