# WAP using function which convert inches to cms
# Formula is -----> cm = in x 2.54

def cm(inch):
    cm = inch * 2.54
    return cm

inches = float(input('Enter the Height in inches to convert into centimeters : \n'))

cms = cm(inches)
print(inches,'Inches =', cms ,'Centimeters')

