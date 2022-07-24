# Treasure Island Game


from secrets import choice


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


step_1 = input("What direction would ypu choose to go? Left or Right. ")

if step_1 == "Left" or step_1 == "left" or step_1 =="LEFT" :
    step_2 = input("Would you like to swim or wait? ")

    if step_2 == "wait" or step_2 == "Wait" or step_2 == "WAIT" :
        step_3 = input("Which door would you like to choose? Red, Blue, or Yellow. ")

        if step_3 == "Yellow" or step_3 == "yellow" or step_3 == "YELLOW" :
            print("You Win!")
        elif step_3 == "Red" or step_3 == "red" or step_3 == "RED" :
            print("Burned by fire. \n Game Over. ")
        elif step_3 == "blue" or step_3 == "Blue" or step_3 == "BLUE" :
            print("Eaten by beasts. \n Game Over. ")
        else :
            print("Game Over. ")

    else :
        print("Attacket by trout. \n Game Over.")    

else :
    print("Fall into a hole \n Game Over.")
