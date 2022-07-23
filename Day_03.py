# Control Flow/Logical Operators



# BMI 2.0

weight = float(input("What is your weight in kg? "))

height = float(input("What is your height in meter? "))

ratio = weight/height

bmi = ratio/height

if bmi < 18.5 :
    print("You are underweight")
elif  bmi < 25 :
    print("You have a normal weight")
elif bmi < 30 :
    print("You are overweight")
elif bmi < 35 :
    print("You are an obese")
else :
    print("You are clinically obese")






# Leap Year

# On every year that is evenly divisible by 4
    # except every year that is evenly divisible by 100
        #unless the year is also evenly divisible by 400

print("Welcome to Leap Year Dediction App!")

year = int(input("Enter the year you want to check. "))

if year % 4 == 0 :
    if year % 100 == 0:
        if year % 400 == 0 :
            print(f"{year} year is a leap year!")
        else :
            print(f"{year} year is not a leap year!")
    else :
        print(f"{year} year is not a leap year!")
else :
    print(f"{year} year is not a leap year!")
    






# Roller coaster ticket 

print("Welcome to Rollercoaster!")

height = int(input("What is your height in cm? "))

bill = 0

if height >= 120 :
    print("You can ride!")
    
    age = int(input("What is your age? "))
    if age < 12 :
        bill = 5
        print("Child ticket is $5.")
    elif age <= 18 :
        bill = 7
        print("Youth ticket is $7.")
    else :
        bill = 12
        print("Adult ticket is $12.")
    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your bill value is $ {bill}.")

else :
    print("Sorry, you have to grow taller before you ride.")







# Pizza order program

print("Welcome to Python Pizza Deliveries! ")

bill = 0

size = input("What size pizza do you want? S, M, or L. ")

if size == "S" :
    bill += 15
elif size == "M" :
    bill += 20
else :
    bill += 25
    
add_pepperoni = input("Do you want pepperoni? Y or N. ")

if add_pepperoni == "Y" :
    if size == "S" :
        bill += 2
    else :
        bill += 3

    
extra_cheeze = input("Do you want extra cheese? Y or N. ")

if extra_cheeze == "Y" :
    bill += 1


print(f"Your final bill is: ${bill}.")






# Love Calculator

print("Welcome to the Love Calculator! ")

girl = input("Enter girl's name: ")
boy = input("Enter boy's name: ")

girl = girl.lower()
boy = boy.lower()

name = girl + boy

T = name.count('t') 
R = name.count('r')
U = name.count('u')
E = name.count('e')

L = name.count('l')
O = name.count('o')
V = name.count('v')
E = name.count('e')

true = T+R+U+E
love = L+O+V+E

score = (true)*10 + (love)

if score < 10 or score > 90:
    print(f"Your score is {score}%, you go together like coke and mentos.")
elif score > 40 and score < 50 :
    print(f"Your score is {score}%, you are alright together.")
else :
    print(f"Your score is {score}%")
