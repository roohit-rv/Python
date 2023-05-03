import random
name=input("enter everybody's name: ")
names=name.split(",")
payer=random.choice(names)
print(payer, " will pay the bill")