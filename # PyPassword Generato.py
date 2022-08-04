#@# PyPassword Generator #@#

from operator import concat
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator")

nr_letter = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password? \n"))
nr_numbers = int(input("How many numbers would you like in your password? \n"))


password = " "
for i in range(1, nr_letter + 1):
    random_char = random.choice(letters)
    password += random_char

for i in range(1, nr_numbers + 1):
    random_num = random.choice(numbers)
    password += random_num

for i in range(1, nr_symbols + 1):
    random_sym = random.choice(symbols)
    password += random_sym


print(f"Your easy password is : {password}")




# ch_letters = str(random.choices(letters , k=nr_letter))
# ch_symbol = str(random.choices(symbols, k=nr_symbols))
# ch_numbers = str(random.choices(numbers, k=nr_numbers))

# password_1 = concat(ch_letters, ch_numbers)
# password = concat(password_1  ,ch_symbol)

# final_password =" "

# for char in password:
#     final_password += char 

# print(f"Your password is : {final_password} ")



password_list = []
for i in range(1, nr_letter + 1):
    random_char = random.choice(letters)
    password_list.append(random_char)

for i in range(1, nr_numbers + 1):
    random_num = random.choice(numbers)
    password_list.append(random_num)

for i in range(1, nr_symbols + 1):
    random_sym = random.choice(symbols)
    password_list.append(random_sym)

password_f = random.shuffle(password_list)

password =" "

for char in password_list:
    password += char

print(f"Your hard password is : {password}")