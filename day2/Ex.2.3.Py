## Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

##It will take your current age as the input and output a message with our time left in this format:

##You have x days, y weeks, and z months left.

##Where x, y and z are replaced with the actual calculated numbers.


##-----------------------------------------------------------------------------------------------------------------------------------------


# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

time_remaining = 90 - int(age)

w_left=  time_remaining *52       #calculate weeks remaining
d_left = time_remaining *365      #calculate days remaining   
m_left = time_remaining *12       #calculate month remaining



message = f"You have {d_left} days, {w_left} weeks, and {m_left} months left"

print (message)