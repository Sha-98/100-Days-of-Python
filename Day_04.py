# Day 04

import random


# Random number

number = random.randint(1 , 10)
print(number)

random_float = random.random()
print(random_float)

love_score = random.randint(1,100)
print(love_score)





# Head or Tails

int = random.randint(0,1)

if int == 1 :
    print("Heads")
else :
    print("Tails")






# Who would pay the bill

names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

int = random.randint(0,4)

person = names[int]

print(f"{person} is going to buy the meal today!" )







# Where would you put the Treasure

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

#created a list of all the three rows to use the list manipulation later
map = [row1, row2, row3]

#printing the matrix
print(f"{row1}\n{row2}\n{row3}")

#taking the input for position to put treasure
position = input("Where do you want to put the treasure? ")

# mapping the input position as per our map
horizontal = int(position[0])
vertical = int(position[1])

#changing the value at the given coordinate
map[vertical-1][horizontal-1] = "X"

#printing the new map
print(f"{row1}\n{row2}\n{row3}")


