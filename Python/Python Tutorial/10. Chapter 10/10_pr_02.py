# Write a class Calculator capable of finding Square , cube and squareroot of a number.


class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The Value of {self.number} Square Is : {self.number **2}")

    def squareRoot(self):
        print(f"The Value of {self.number} Square_Root Is : {self.number **0.5}")

    def cube(self):
        print(f"The Value of {self.number} Cube Is : {self.number **3}")


a = Calculator(64)
a.square()
a.squareRoot()
a.cube()

