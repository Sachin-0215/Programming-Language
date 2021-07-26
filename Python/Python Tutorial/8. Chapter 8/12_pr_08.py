# WAP to print multiplication table of a given entered number ?


def mul_table(n):
    for i in range(1,11):
        print(n,"x",i, " = " ,n*i)

n = int(input("Enter Your Number to Prints its Multiplication Table : "))        
mul_table(n)
