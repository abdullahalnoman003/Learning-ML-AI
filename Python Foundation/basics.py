# This is how a comment is written in pyhon

# Declare of Python variable,
name = "Abdullah Al Noman"
age = 22
dept = "Software Engineering"
cgpa = 3.92
active = True
# this are all types of variable, it stores automatically the type so no need to declare

print(name, age, dept, cgpa, active)

# Now to check the type of the variable 

print(type(name))
print(type(cgpa))
print(type(active))

#  Now to take input from user, we use input()

like = input("What do you like: ")
print(like)

# it is to be noted that input always returns string. so if we need number r anything we must typecast it

cgpa = float(input("Enter your cgpa: "))
print("Your Cgpa is: ", cgpa)
