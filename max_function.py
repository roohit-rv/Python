#max function is use to fetch out the biggest value from given values
student_marks=input("enter the height of the students:- ").split(",")
for n in range(0,len(student_marks)):
    student_marks[n]=int(student_marks[n])
print(student_marks)
maximum=max(student_marks)
print("highest marks is - ",maximum)