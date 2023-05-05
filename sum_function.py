#sum functions is used to calculate all the sum for all the values of integers
height=input("enter the height for boys").split(",")
print(height)
for n in range(0,len(height)):
    height[n]=int(height[n])
s=sum(height)
print("sum of all the heights- ",s)