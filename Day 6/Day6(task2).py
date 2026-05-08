student_names=['ismail','Ali','ahmed','sara','laila']
student_grades=[90,85,78,92,88]
top_grades =max(student_grades)
top_student_rank= student_grades.index(top_grades)
top_student_name=student_names[top_student_rank]
print(f"The top student is {top_student_name} with a grade of {top_grades}.")
lowest_grades =min(student_grades)
lowest_student_rank= student_grades.index(lowest_grades)
lowest_student_name=student_names[lowest_student_rank]
print(f"The lowest student is {lowest_student_name} with a grade of {lowest_grades}.")
average_grade = sum(student_grades) / len(student_grades)
print(f"The average grade is {average_grade:.2f}.")
print("passing students:")
for i in range(len(student_names)):
    if student_grades[i] >= 50:
        print(f"{student_names[i]}: {student_grades[i]}")