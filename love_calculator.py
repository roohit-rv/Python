# Love Calculator
Your_name=input("what is your name? ")
his_her_name=input("what is your lover name? ")
print("Names are ", Your_name, his_her_name)
lower_case_your_name=Your_name.lower()
lower_case_his_her_name=his_her_name.lower()
both_name=lower_case_your_name+lower_case_his_her_name
t=both_name.count("t")
r=both_name.count("r")
u=both_name.count("u")
e=both_name.count("e")
l=both_name.count("l")
o=both_name.count("o")
v=both_name.count("v")
e=both_name.count("e")
true=t+r+u+e
love=l+o+v+e
total_char=int(str(true)+str(love))
if total_char>90 and total_char<10:
    print(total_char, "is your total score\n you both should do coke and mentos together")
elif 40<=total_char<=50:
    print(total_char, " is your total score\n you both are alright together")
else:
    print(total_char, " is your total score")