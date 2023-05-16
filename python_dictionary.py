python_dictionary = {
    "Bug": "An error during which your program has logical or syntax error",
    "Function": "Defined specific set of code instructions",
    "Loop": "To perform a task again and again",
    123:"Numbers"
}
# creating an empty dictionary
empty_dictionary={}

print(empty_dictionary)
print(python_dictionary)

print(python_dictionary["Bug"])

# Add word to dictionary
python_dictionary["stackoverflow"] = "A site where people engage with each other and help them to code"
print(python_dictionary["stackoverflow"])
print(python_dictionary[123])
empty_dictionary["wipe"]="cleaning out everything"
print(empty_dictionary["wipe"])
for key in python_dictionary:
    print(key)
    print(python_dictionary[key])