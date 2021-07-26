# Type error, Type Checking and Type Conversion

num_char = len(input("What is your Name?\n"))
# print("Your name has "+num_char + " Characters.") can only concatenate str (not "int") to str

# Type Checking
print(type(num_char))

# Type Conversion
new_num_char = str(num_char)
print("Your name has " + new_num_char + " Characters.")

a = (526)
print(type(a))
b = str(a)
print(type(b))
print(70+float("92.2"))
print(str(73)+str(37))
