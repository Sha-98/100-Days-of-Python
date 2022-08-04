# Rock-paper-scissors Game

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

if choice == "0" :
    print(rock)

    computer_choice = random.randint(0,2)
    
    if computer_choice == 0:
        print("Computer chose:\n")
        print(rock)
        print("Its a Tie!")
    elif computer_choice == 1:
        print("Computer chose:\n")
        print(paper)
        print("You Win!")
    else :
        print("Computer chose:\n")
        print(scissors)
        print("You Lose!")

elif choice == "1" :
    print(paper)

    computer_choice = random.randint(0,2)

    if computer_choice == 0:
        print("Computer chose:\n")
        print(rock)
        print("You Win!")
    elif computer_choice == 1:
        print("Computer chose:\n")
        print(paper)
        print("Its a Tie!")
    else :
        print("Computer chose:\n")
        print(scissors)
        print("You Lose!")

else :
    print(scissors)

    computer_choice = random.randint(0,2)

    if computer_choice == 0:
        print("Computer chose:\n")
        print(rock)
        print("You Lose!")
    elif computer_choice == 1:
        print("Computer chose:\n")
        print(paper)
        print("You Win!")
    else :
        print("Computer chose:\n")
        print(scissors)
        print("Its a Tie!")