print("enter three numbers")
num1=int(input())
num2=int(input())
num3=int(input())
if (num1>num2 and num1>num3):
    print("The greatest number is=",num1)
elif (num2>num1 and num2>num3):
    print("The greatest number is=",num2)
elif (num3>num1 and num3>num2):
    print("The greatest number is=",num3)