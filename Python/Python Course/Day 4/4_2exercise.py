# Who will pay the bill

import random

# Split string method 
names_String = input("Give me everbody's names separated by a comma. ")
names = names_String.split(", ")

# Get total number of items in the list.
num_items = (len(names))

random_name = random.randint(0,num_items-1)
person_name_who_will_pay = names[random_name]
print(f"{person_name_who_will_pay} is going to pay today.  ")


#Shortcut method 
# person_name_who_will_pay = random.choice(names)
# print(f"{person_name_who_will_pay} is going to pay today.  ")

