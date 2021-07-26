# Print high score in the list
# don't use max or min function

student_scores = input("Enter the score of all students: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

print(student_scores)

highest_score = 0
for score in student_scores:
    # highest_score = max(student_score)
    if score > highest_score:
        highest_score = score

print(f"Highest Score is: {highest_score}")
