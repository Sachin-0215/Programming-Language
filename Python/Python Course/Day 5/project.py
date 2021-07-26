# Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
special_chararcters = ['!', '#', '$', '%', '&', '(', ')', '>', '<', '/', '@']

print("Welcome to Python Password Generator!")
pw_letters = int(input("How many letters would you like in your password?\n"))
pw_numbers = int(input("How many numbers would you like?\n"))
pw_symbols = int(input("How many symbols would you like?\n"))

# Easy level
# password1 = ""
# for char in range(1, pw_letters + 1):
#     # random_char = random.choice(letters)
#     # password1 += random_char
#     # print(random_char)
#     # print(password1)
#     password1 += random.choice(letters)

# for char in range(1, pw_numbers+1):
#     password1 += random.choice(numbers)

# for char in range(1, pw_symbols+1):
#     password1 += random.choice(special_chararcters)

# print(f"Here is your password: {password1}")


# Hard Level
password_list = []
for char in range(1, pw_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, pw_numbers+1):
    password_list += random.choice(numbers)

for char in range(1, pw_symbols+1):
    password_list += random.choice(special_chararcters)

print(f"Here is your password: {password_list}")
random.shuffle(password_list)
print(f"Here is your password: {password_list}")

password = ""
for char in password_list:
    password+=char

print(f"Your password is: {password}")

