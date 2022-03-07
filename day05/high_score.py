student_scores = input("Input a list of student scores ").split()
print(student_scores)
high_score = 0
for n in student_scores:
    if int(n) > high_score:
        high_score = int(n)

print("The highest score is", high_score)