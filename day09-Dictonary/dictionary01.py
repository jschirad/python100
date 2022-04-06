student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TO DO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TO DO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
    if student_scores[student] >= 90:
        student_grades[student] = "Oustanding"
    elif student_scores[student] >= 80 and student_scores[student] <= 89:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] >= 70 and student_scores[student] < 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Failed"

# 🚨 Don't change the code below 👇
print(student_grades)



