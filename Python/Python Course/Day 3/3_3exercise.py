# Leap Year Challenge

year = int(input("Which year you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"You entered {year} , it's a leap year")
        else:
            print(f"You entered {year} , it's not a leap year")
    else:
        print(f"You entered {year} , it's a leap year")

else:
    print(f"You entered {year} , it's not a leap year")
