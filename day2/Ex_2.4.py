## The Tip Calculator

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60


#Write your code below this line 👇


bill = (input("Welcome to the tip calculator! \n \nWhat was the total bill?\n\n"))


tip = (input("How much tip would you like to give? 10, 12, or 15?\n \n"))

people = int(input ("How many people to split the bill?\n \n"))

total = (float(bill) / int(people)) * (float(tip)/ 100 +1)

total = "{:.2f}".format(total)

print (total)