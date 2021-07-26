# WAP to input name,marks and phoneNumber of a student and format it using the format like below :
# The name of a student is Sachin , his marks are 72 and phone number is "999998885" 

name = input("Enter your name: ")
marks = input("Enter your marks: ")
phone = input("Enter you phone Number: ")

template = "The name of the student is {}, his marks are {} and phone number is {} "
output = template.format(name, marks, phone)
print(output)