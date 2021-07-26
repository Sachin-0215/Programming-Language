# Calculator

from art import logo
from clear import clear

# addition
def addition(n1, n2):
    return n1+n2

# Substaction
def subtraction(n1, n2):
    return n1-n2

# Multiply
def multiply(n1, n2):
    return n1*n2

# Division
def divide(n1, n2):
    return n1/n2


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiply,
    "/": divide
}

# Recursion concept
def calculator():
    print(logo)

    num1 = float(input("What's the first number?  "))
    for symbol in operations:
        print(symbol)
    should_Continue = True
    while should_Continue:    
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") =="y":
            num1=answer
        else:
            should_Continue=False  
            clear()  
            calculator()

calculator()