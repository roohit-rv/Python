print("Rollercoaster")
h=int(input("enter your age "))
if h>=120:
    print("you can ride the rollercoaster")
    age=int(input("enter your age "))
    if age>18:
        print("pay $12")
        bill=12
    else:
        print("pay $7")
        bill=7
    pic=input("do you want to click a picture? y or n ")
    if pic=="y":
      bill+=3
      print("your ticket price is $", bill)
    else:
        print("your ticket price is $", bill)
    
else:
    print("your are too small in size to ride")