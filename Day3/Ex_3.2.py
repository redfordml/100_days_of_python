""" 
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.

Warning you should round the result to the nearest whole number. 
The interpretation message needs to include the words in bold from the interpretations above. e.g. underweight, normal weight, overweight, obese, clinically obese.

"""

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆
#Write your code below this line 👇

bmi_result = int (weight) / float(height) ** 2

if bmi_result < 18.5:
    print ("Your BMI is",round(bmi_result)," you are underweight")

elif bmi_result < 25:
    print("Your BMI is", round(bmi_result)," you have a normal weight")

elif bmi_result < 30:
    print("Your BMI is",round(bmi_result)," you are slightly overweight")

elif bmi_result < 35:
    print("Your BMI is", round(bmi_result)," you are obese")

elif bmi_result > 35:
    print("Your BMI is", round(bmi_result)," you are clinically obese.")


