# Prime Number Checker

number = int(input("Check this number? "))

def prime_checker(n):
    is_Prime = True
    for i in range(2,number):
        if number%i==0:
                is_Prime=False
        if is_Prime:        
            print(f"{number} is a Prime Number.")
        else:
            print(f"{number} is not a Prime Number")

prime_checker(n=number)        