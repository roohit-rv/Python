print("counting digits of any number")
num=int(input("enter any number"))
d=0
while num>0:
    d=d+1
    num=int(num/10)

print("numbers in the digit are ",d)