# BMI Calculator

height = float(input("Enter your height in m : "))
weight = int(input("Enter your weight in kg : "))


BMI = (weight/height**2)
int_BMI = int(BMI)
print(int_BMI)
