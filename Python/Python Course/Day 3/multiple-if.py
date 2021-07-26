print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child Tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    want_photo = input("Do you want a photo taken? Y or N.\t")
    if want_photo == "Y":
        bill += 3

    print(f"Your Total Bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
