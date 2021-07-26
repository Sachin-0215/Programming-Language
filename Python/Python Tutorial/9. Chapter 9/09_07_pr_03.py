# WAP to generate multiplication tables from 2 to 20 and write it to the different files.
# Place these files in a folder for 13-years old


for i in range(2, 41):
    with open(f"tables/Multiplication_table_of_{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i}x{j}={i*j}")
            if j!=10:
                f.write('\n')
