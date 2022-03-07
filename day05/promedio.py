student_heights = input("Input a list of student heights ").split()
sum_student_heights = 0
x = 0
for n in student_heights:
    sum_student_heights += int(n)
    x = x + 1
    
print(student_heights)
print(sum_student_heights)
print(x)  

average_student_heights = sum_student_heights / x
result = round(average_student_heights)
print("The average student height is", result)