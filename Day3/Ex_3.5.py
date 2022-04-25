"""_
    You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:

"Your score is **z**."


    
"""
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


both_names = name1.lower() + name2.lower()

phrase1 = ['t', 'r', 'u', 'e']
phrase2 = ['l', 'o', 'v', 'e']


count1 = 0
count2 = 0

for i in both_names:
    if str(i) in phrase1:
        count1 += 1
        

for j in both_names:
  if str(j) in phrase2:
    count2 += 1
    
score = int (str(count1) + str(count2)) #mix two counters

#score = int(score)

#print(score)

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
  
  
elif score < 50 and score > 40:
  print (f"Your score is {score}, you are alright together.")
  

else:
  print(f"Your score is {score}.")