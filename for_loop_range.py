#by adding the third element in the for loop it decides how much interval have to be in in between each number.If we donot add the range it will be consequently like 1 then 2 then 3 etc... but if we add range like 3 then it will go like 1 then 4 then 7 etc...
for i in range(1, 11):
    print(i)
for i in range(1, 50, 3):
    print(i)