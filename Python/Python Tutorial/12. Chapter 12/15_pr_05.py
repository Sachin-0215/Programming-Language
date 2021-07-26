# Store the multiplication tables generate in Problem 3 in a file read named Table.txt.

num = int(input("Enter your number: "))

table = [num*i for i in range(1, 11)]
print(table)
with open("tables.txt", "a") as f:
    f.write(str(table))
    f.write('\n')