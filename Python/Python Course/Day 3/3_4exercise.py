# Pizza Order Challenge

print("Welcome To Python Pizza Delieveries!")
size = input("What size pizza do you want? S,M or L ?  ")
add_pepperoni=input("Do you want add pepperoni in your pizza? Y or N  ")
extra_cheese=input("Do you want to add extra cheese in your pizza? Y or N  ")
pizza=0
pepperoni=0
cheese=0

if size=="S":
    pizza=15
    print("Small Size pizza: $15")
    if add_pepperoni=="Y":
        pepperoni=2
        print("Pepperoni for small pizza is: +$2")
    if extra_cheese=="Y":
        cheese=1
        print("Extra Cheese for this pizza is: +$1") 

    bill=pizza+pepperoni+cheese
    print(f"Your final bill for Small Pizza is: ${bill}")

elif size=="M":
    pizza=20
    print("Medium Size pizza: $20")
    if add_pepperoni=="Y":
        pepperoni=3
        print("Pepperoni for Medium pizza is: +$3")
    if extra_cheese=="Y":
        cheese=1
        print("Extra Cheese for this pizza is: +$1") 

    bill=pizza+pepperoni+cheese
    print(f"Your final bill for Medium Pizza is: ${bill}")

elif size=="L":
    pizza=25
    print("Medium Size pizza: $25")
    if add_pepperoni=="Y":
        pepperoni=3
        print("Pepperoni for small pizza is: +$2")
    if extra_cheese=="Y":
        cheese=1
        print("Extra Cheese for this pizza is: +$1") 

    bill=pizza+pepperoni+cheese
    print(f"Your final bill for Large Pizza is: ${bill}")

else:
    print("You entered Wrong Statement!!")