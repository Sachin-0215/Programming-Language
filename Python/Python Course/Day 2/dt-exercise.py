# task is to enter two digit number and print its sum. 
# Example : Type a two digit number : 82 
# 10

# Don't  change the code below
two_digit_number = input("Type a two digit integer : ")
# Don't  change the code above

# check the datatype of two_digit_number
print(type(two_digit_number))

# get the first and second digits using substring then convert string to int
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# Add two digits together
result = first_digit+second_digit

# print result
print(result)
