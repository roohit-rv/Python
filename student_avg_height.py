student_height=input("enter the height of the students:- ").split(",")
for n in range(0,len(student_height)):
    student_height[n]=int(student_height[n])
print(student_height)
sum=0
l=0
for n in range(0,len(student_height)):
    sum=sum+student_height[n]
    l=l+1
avg_height=round(sum/l)
print("the avgerage height of the students are- ",avg_height)