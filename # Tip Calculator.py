# Tip Calculator

print("Welcome to the tip calculator!")

# Amount of bill
bill = float(input("What was the total bill? $"))

# Percentage of tip
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Number of person to split the bill
people = int(input("How many people to split the bill? "))

amount = bill*(1 + tip/100)

bill_per_person = amount/people

# Fomatting the final result to 2 decimal places number
result = "{: .2f}".format(bill_per_person)

print(f"Each person should pay: ${result}")