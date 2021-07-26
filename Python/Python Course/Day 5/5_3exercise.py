# Adding Even Numbers

# Method 1:
even_number = 0
for number in range(2, 101, 2):
    # print(number)
    even_number += number

print(f"Sum of Even Numbers is: {even_number}")

# Method 2:
total = 0
for number2 in range(1,101):
    if number2 % 2==0:
        total+=number2

print(f"Sum of Even Numbers is: {total}")
