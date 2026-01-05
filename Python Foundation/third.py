# Now we wil try loops in python
# first for loop

for i in range(1, 10):
    print(i)

# in range there is 2 condition range(start, stop, step)
for i in range(1, 10, 2):
    print(i)

# also there is some extra functions in range 
password = "1234"

for attempt in range(3):
    user_input = input("Enter password: ")

    if user_input == password:
        print("Login successful")
        break
    else:
        print("Wrong password")

#to skip  use contineu and break to get out from loop

# Now while loop
while True:
    password = input("Enter password: ")
    if password == "1234":
        break
 # it will run until break