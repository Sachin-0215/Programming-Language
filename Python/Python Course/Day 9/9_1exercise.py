# Grading Program Exercise

student_scores = {
    "Harry":81,
    "Rohan":90,
    "Jack":29,
    "Draco":74,
    "Neville":62,
}
student_grades = {}

for student in student_scores:
    # print(student)
    scores = student_scores[student]
    # print(scores)
    if scores >= 91 and scores<=100:
        student_grades[student]= "Outstanding."
    elif scores >= 81 and scores<=90:
        student_grades[student]= "Exceeds Expectations."
    elif scores >= 71 and scores<=80:
        student_grades[student]= "Acceptable."
    else:
        student_grades[student]= "Fail."

print(student_grades)
        
        
        