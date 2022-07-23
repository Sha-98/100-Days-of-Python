#Day_02

# Data types



# ## Adding two numbers etered by the user

# #taking the input
number = str(input("Enter a two digit number "))

# #creating variables and changing them to int type
first_digit = int(number[0])
second_digit = int(number[1])

# # adding the variables to get the desired answer
result = first_digit + second_digit

print(result)




## BMI Calculator

weight = input("Enter your weight in kg ")
height = input("Enter your height in meter ")


w = float(weight)
h = float(height)

bmi = w / (h*h)

result = round(bmi, 2)

print(result)





# f-String

score = 0
height = 1.8
isWinning = True

print(f"Your score is {score} , your height is {height} and you are winning is {isWinning}" )






# Your life in weeks

age = input("What is your current age? ")

# The person lives for 90 years

#years left
year = 90 - int(age) 

#months left
months = year*12

#weels left
weeks = year*52

# days left 
days = year*365

print(f"You have {days} days, {weeks} weeks, {months} months and {year} years to live.")