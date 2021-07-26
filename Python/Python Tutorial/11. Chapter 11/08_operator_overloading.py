


class Number:
    def __init__(self,num):
        self.num = num

    def __add__(self,num2):
        print("Let's Add")
        return self.num + num2.num 

    def __mul__(self,num2):
        print("Let's Multiply")
        return self.num * num2.num        

n1 = Number(45)
n2 = Number(5)        

sum = n1 + n2
multiply = n1 * n2


print(sum)
print(multiply)