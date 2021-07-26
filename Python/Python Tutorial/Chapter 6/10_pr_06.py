# WAP to calculate the grade of a student from his marks from the following scheme:
# 90-100 Excellent
# 80-90 A
# 70-80 B
# 60-70 C
# 50-60 D
# 40-50 E


marks = int(input("Enter Your Marks\n"))

if marks>=90:
    grade = "Excellent"
elif marks>=80:
    grade = "A"
elif marks>=70:
    grade = "B"
elif marks>=60:
    grade = "C"
elif marks>=50:
    grade = "D" 
else:
    grade = "F"

print("Your grade is " + grade)