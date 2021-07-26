# Average Height Exercise

# don't use sum() and len() 
# perform using for loop only

students_heights = input("Input the heights of all students: ").split()
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])

print(students_heights)    

total_height = 0
for height in students_heights:
    total_height+=height
    # total_height = sum(students_heights)

print(total_height)    

# number_of_students = len(students_heights)    
number_of_students = 0
for student in students_heights:
    number_of_students+=1

print(number_of_students)

average_height = round(total_height/number_of_students)
print(f"The average height of all students is: {average_height}")