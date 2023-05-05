student_marks=input("enter the height of the students:- ").split()
for n in range(0,len(student_marks)):
    student_marks[n]=int(student_marks[n])
print(student_marks)
highest_score=0
for n in range(0,len(student_marks)):
    if(highest_score<student_marks[n]):
        highest_score=student_marks[n]
print("the highest score is - ",highest_score)